#!/usr/bin/env python3
"""Verify all .tile.talk embed sections have correct structure."""
import sys
import subprocess
import time
import urllib.request
from html.parser import HTMLParser

PORT = 8787


class TalkTileParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tiles = []
        self._stack = []       # tag stack for depth tracking
        self._tile_idx = None  # stack index where current tile started
        self._wrap_idx = None  # stack index where current frame-wrap started
        self._current = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        self._stack.append(tag)

        if tag == 'section' and 'tile' in classes and 'talk' in classes:
            self._tile_idx = len(self._stack) - 1
            self._wrap_idx = None
            self._current = {
                'has_frame_wrap': False,
                'iframe_count': 0,
                'iframe_inside_wrap': False,
                'iframe_has_fixed_size': False,
                'iframe_src': '',
            }

        if self._current is not None:
            if tag == 'div' and 'frame-wrap' in classes:
                self._current['has_frame_wrap'] = True
                self._wrap_idx = len(self._stack) - 1

            if tag == 'iframe':
                self._current['iframe_count'] += 1
                self._current['iframe_src'] = attrs_dict.get('src', '')[:70]
                if self._wrap_idx is not None:
                    self._current['iframe_inside_wrap'] = True
                if 'width' in attrs_dict or 'height' in attrs_dict:
                    self._current['iframe_has_fixed_size'] = True

    def handle_endtag(self, tag):
        if not self._stack:
            return
        depth = len(self._stack) - 1

        if self._tile_idx is not None and depth == self._tile_idx and tag == 'section':
            self.tiles.append(self._current)
            self._current = None
            self._tile_idx = None
            self._wrap_idx = None

        if self._wrap_idx is not None and depth == self._wrap_idx and tag == 'div':
            self._wrap_idx = None

        self._stack.pop()


def verify(html):
    parser = TalkTileParser()
    parser.feed(html)

    print('=== EMBED VERIFICATION ===\n')
    all_pass = True

    for i, tile in enumerate(parser.tiles, 1):
        checks = {
            '.frame-wrap present': tile['has_frame_wrap'],
            'iframe in .frame-wrap': tile['iframe_inside_wrap'],
            'no fixed width/height': not tile['iframe_has_fixed_size'],
            'iframe present': tile['iframe_count'] > 0,
        }
        passed = all(checks.values())
        if not passed:
            all_pass = False

        print(f'Tile {i}: {"✓ PASS" if passed else "✗ FAIL"}')
        for label, ok in checks.items():
            print(f'  {"✓" if ok else "✗"} {label}')
        print(f'  src: {tile["iframe_src"]}')
        print()

    print(f'Result: {"✓ ALL PASS" if all_pass else "✗ FAILURES FOUND"}')
    return all_pass


if __name__ == '__main__':
    proc = subprocess.Popen(
        ['python3', '-m', 'http.server', str(PORT)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    time.sleep(0.5)

    try:
        resp = urllib.request.urlopen(f'http://localhost:{PORT}/', timeout=5)
        html = resp.read().decode('utf-8')
    except Exception as e:
        print(f'Server error: {e}')
        proc.terminate()
        sys.exit(1)

    ok = verify(html)

    subprocess.run(['open', f'http://localhost:{PORT}/'], check=False)
    print(f'\nBrowser opened: http://localhost:{PORT}/')
    print('Press Ctrl+C to stop server.')

    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()

    sys.exit(0 if ok else 1)

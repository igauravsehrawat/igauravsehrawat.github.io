import puppeteer from 'puppeteer';
import { spawn } from 'child_process';
import { setTimeout as sleep } from 'timers/promises';

const PORT = 8787;
const BASE = `http://localhost:${PORT}`;

// Start python HTTP server
const server = spawn('python3', ['-m', 'http.server', String(PORT)], {
  cwd: new URL('.', import.meta.url).pathname,
  stdio: 'pipe',
});
await sleep(800);

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 1280, height: 900 });

console.log('Loading page...');
await page.goto(BASE, { waitUntil: 'networkidle2', timeout: 30_000 });

// Check all .tile.talk sections
const results = await page.evaluate(() => {
  const tiles = [...document.querySelectorAll('.tile.talk')];
  return tiles.map((tile, i) => {
    const wrap = tile.querySelector('.frame-wrap');
    const iframe = tile.querySelector('iframe');
    const meta = tile.querySelector('.talk-meta h3')?.textContent;
    const wrapRect = wrap?.getBoundingClientRect();
    const iframeRect = iframe?.getBoundingClientRect();
    return {
      index: i + 1,
      title: meta,
      hasFrameWrap: !!wrap,
      iframePresent: !!iframe,
      iframeSrc: iframe?.src?.slice(0, 60),
      wrapHeight: Math.round(wrapRect?.height ?? 0),
      iframeWidth: Math.round(iframeRect?.width ?? 0),
      iframeHeight: Math.round(iframeRect?.height ?? 0),
      iframeVisible: (iframeRect?.width > 0 && iframeRect?.height > 0),
    };
  });
});

console.log('\n=== EMBED VERIFICATION ===');
let allPass = true;
for (const r of results) {
  const pass = r.hasFrameWrap && r.iframeVisible;
  if (!pass) allPass = false;
  const status = pass ? '✓ PASS' : '✗ FAIL';
  console.log(`\nTile ${r.index}: ${r.title}`);
  console.log(`  ${status}`);
  console.log(`  .frame-wrap: ${r.hasFrameWrap}`);
  console.log(`  iframe visible: ${r.iframeVisible} (${r.iframeWidth}x${r.iframeHeight}px)`);
  console.log(`  wrap height: ${r.wrapHeight}px`);
  console.log(`  src: ${r.iframeSrc}`);
}

// Full-page screenshot
await page.screenshot({ path: 'verify-screenshot.png', fullPage: true });
console.log('\nScreenshot saved: verify-screenshot.png');
console.log(`\nResult: ${allPass ? '✓ ALL PASS' : '✗ FAILURES FOUND'}`);

await browser.close();
server.kill();
process.exit(allPass ? 0 : 1);

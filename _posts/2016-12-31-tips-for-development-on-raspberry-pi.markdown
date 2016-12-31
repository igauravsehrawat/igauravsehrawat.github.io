---
layout: post
permalink: "/tips-for-development-on-raspberry-pi/"
title: "Tips for development on raspberry pi"
description: "Some tips and tricks while writing code for raspberry pi."
tags: ["Raspberry pi,"]
comments: true
share: true
---

Tips while using raspberry pi for development.
Let's face it, it's cumbersome to ssh into raspberry pi and write code there.

1. Configure your ssh keys for direct login instead of password based login.

2. Use Rsync to sync folder from working location to remote location.
For example:
``` rsync manual-interface/ -azP pi@192.168.43.34:/home/pi/Projects/manual-interface/ ```
This command will sync the content of `manual-interface` on host computer to remote location which is at raspberry pi. If ssh keys are configured, one won't need to enter password for raspberry pi.


3. Usage of watchdog for automatic syncing the code to raspberry pi.
`watchdog` is wonderful python package for monitoring events on file system.
One can write a python script using watchdog package or simply use `watchmedo` shell command.
For example:
```
watchmedo shell-command \
    --patterns="*.py;*.txt;*.js;*.css;*.html" \
    --recursive \
    --command='rsync . -azP pi@192.168.43.34:/home/pi/Projects' \
    . \
```
Here I am looking for pattern recursive inside the current location, on detection of changes on file system, `rsync` comes to rescue for syncing.


4. Using VNC viewer for accessing GUI interface.
VNC is excellent software for remote accessing the desktop, this can save extra monitor configuration.

These are few tips which are helpful to me, while working on an exciting project. Till next time.

See you in 2017. Happy New Year. Best wishes.

Cheers



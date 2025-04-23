#!/bin/bash

# Capture environment variables and store them for cron
printenv | sed 's/^\(.*\)$/export \1/g' > /root/env_vars.sh

# Restart cron to apply changes
service cron restart

# Keep container running
Xvfb :99 -screen 0 1024x768x24 & tightvncserver :1 -geometry 1024x768 -depth 24
tail -f /dev/null

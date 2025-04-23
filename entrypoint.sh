#!/bin/bash

# Capture environment variables and store them for cron
printenv | sed 's/^\(.*\)$/export \1/g' > /home/appuser/env_vars.sh;

tail -f /dev/null

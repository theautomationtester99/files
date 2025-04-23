#!/bin/bash
export DISPLAY=:0
/root/build/runner --start-parallel >> /proc/1/fd/1 2>> /proc/1/fd/2


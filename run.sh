#!/bin/bash
. myenv/bin/activate
nohup uvicorn main:app --host 0.0.0.0 --port 8123 --reload > log.log 2>&1 &
echo $!
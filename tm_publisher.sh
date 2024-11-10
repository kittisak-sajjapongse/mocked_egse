#!/usr/bin/env bash
pip3 install nats-py
echo "Start running publisher"
python3 /app/tm_publisher.py
echo "End running publisher"


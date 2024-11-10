#!/usr/bin/env bash
pip3 install nats-py
echo "Start running subscriber"
python3 /app/tm_subscriber.py
echo "End running subscriber"


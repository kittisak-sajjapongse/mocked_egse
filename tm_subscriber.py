import json
import os
import sys
import time
import nats

async def message_handler(msg):
    data = json.loads(msg.data.decode())
    print(f"Received message: {data}")

async def main():
    nats_hostname = os.environ.get('NATS_HOSTNAME', 'localhost')
    nc = await nats.connect(f"nats://{nats_hostname}:4222")
    print(f"Connected to NATS at {nats_hostname}:4222")
    sub = await nc.subscribe("tm_publish")
    while True:
        try:
            async for msg in sub.messages:
                data = json.loads(msg.data.decode())
                print(f"Received a message with data: '{data}")
                sys.stdout.flush()
        except Exception as e:
            pass

    # while True:
    #     time.sleep(0.1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
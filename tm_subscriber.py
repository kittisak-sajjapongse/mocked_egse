import json
import os
import sys
import time
import nats

async def message_handler(msg):
    data = json.loads(msg.data.decode())
    print(f"Received message: {data}")

async def subscribe_tm_packages():
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

async def subscribe_tm_params():
    nats_hostname = os.environ.get('NATS_HOSTNAME', 'localhost')
    nc = await nats.connect(f"nats://{nats_hostname}:4222")
    print(f"Connected to NATS at {nats_hostname}:4222")
    sub = await nc.subscribe("tm_param")
    while True:
        try:
            async for msg in sub.messages:
                data = json.loads(msg.data.decode())
                print(f"Received a message with data: '{data}")
                sys.stdout.flush()
        except Exception as e:
            pass

if __name__ == "__main__":
    import asyncio
    
    async def main():
        # Run both generators concurrently
        await asyncio.gather(
            subscribe_tm_packages(),
            subscribe_tm_params()
        )
    
    asyncio.run(main())
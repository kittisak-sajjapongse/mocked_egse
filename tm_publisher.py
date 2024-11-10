import json
import os
import random
import sys
import time
import nats

nats_hostname = os.environ.get('NATS_HOSTNAME', 'localhost')

async def publish_message(nc):
    delay = random.randint(1, 1)
    await nc.publish("tm_publish", json.dumps({
        "tm_id": "id_" + str(random.randint(1, 100)),
        "tm_name": "name_" + str(random.randint(1, 100)),
        "generation_time": int(time.time()),
        "creation_time": int(time.time()) + 1000
    }).encode())
    await nc.flush() # This is required. Otherwise the messagge won't be sent
    print(f"Published message with delay of {delay} seconds")
    sys.stdout.flush()
    time.sleep(delay)

async def main():
    nc = await nats.connect(f"nats://{nats_hostname}:4222")
    print(f"Connected to NATS at {nats_hostname}:4222")
    while True:
        await publish_message(nc)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
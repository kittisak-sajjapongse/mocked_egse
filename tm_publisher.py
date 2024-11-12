import json
import os
import random
import sys
import time
import nats

nats_hostname = os.environ.get('NATS_HOSTNAME', 'localhost')

async def publish_tm_package(nc):
    delay = random.randint(1, 1)
    await nc.publish("tm_publish", json.dumps({
        "tm_id": "id_" + str(random.randint(1, 100)),
        "tm_name": "name_" + str(random.randint(1, 100)),
        "generation_time": int(time.time()),
        "creation_time": int(time.time()) + 1000
    }).encode())
    await nc.flush() # This is required. Otherwise the messagge won't be sent
    print(f"Published TM package with delay of {delay} seconds")
    sys.stdout.flush()
    await asyncio.sleep(delay)

tm_list = [
    {"tm_id": "id_001", "tm_name": "tm_001"},
    {"tm_id": "id_002", "tm_name": "tm_002"},
    {"tm_id": "id_003", "tm_name": "tm_003"},
    {"tm_id": "id_004", "tm_name": "tm_004"},
    {"tm_id": "id_005", "tm_name": "tm_005"},
    {"tm_id": "id_006", "tm_name": "tm_006"},
    {"tm_id": "id_007", "tm_name": "tm_007"},
    {"tm_id": "id_008", "tm_name": "tm_008"},
    {"tm_id": "id_009", "tm_name": "tm_009"},
    {"tm_id": "id_010", "tm_name": "tm_010"},
]

async def publish_tm_params(nc):
    delay = random.randint(1, 1)
    tm_selection = random.choice(tm_list)
    await nc.publish("tm_param", json.dumps({
        "tmpk_name": "TMPACKET01",
        "tm_id": tm_selection["tm_id"],
        "tm_name": tm_selection["tm_name"],
        "raw_value": random.randint(1, 100),
        "eng_value": random.uniform(1.0, 100.0),
        "generation_time": int(time.time()),
        "creation_time": int(time.time()) + 1000
    }).encode())
    print(f"Published TM param with delay of {delay} seconds")
    sys.stdout.flush()
    await asyncio.sleep(delay)

async def generate_tm_packages():
    nc = await nats.connect(f"nats://{nats_hostname}:4222")
    print(f"Connected to NATS at {nats_hostname}:4222")
    while True:
        await publish_tm_package(nc)

async def generate_tm_params():
    nc = await nats.connect(f"nats://{nats_hostname}:4222")
    print(f"Connected to NATS at {nats_hostname}:4222")
    while True:
        await publish_tm_params(nc)

if __name__ == "__main__":
    import asyncio

    async def main():
        # Run both generators concurrently
        await asyncio.gather(
            generate_tm_packages(),
            generate_tm_params()
        )
    
    asyncio.run(main())
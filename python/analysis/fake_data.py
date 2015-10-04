#! /usr/bin/python
from datetime import datetime, timedelta, date, time
from copy import deepcopy
import random
import requests
from time import sleep
import json

apps = ['TallyTots Counting',
        'Kids ABC Phonics',
        '123 ABC Kids Handwriting HWTP',
        'Sketch-a-aSong-$-Kids',
        'Paint Kids',
        'Finger Paint',
        'Walk Band',
        'Paper Planes',
        'Play Store',
        'RescueTime',
        'Fireworks Arcade',
        'Epic!',
        'F2B Enterprise',
        'Kids ABC Letter Trains (Lite)',
        'Bebop Band1',
        'Bebop Band3',
        'Learning Songs For Toddlers',
        'FieteBauernhof',
        'Kids Stickers Lite',
        'Season of Tree',
        'Toca Kitchen 2',
        'Antonyms',
        'Charadas',
        'First Words',
        'Starfall ABCs',
        'Block Puzzle',
        'Shapes',
        'Curious Kid Toy Car',
        'Flow Free',
        'Marble Mania',
        'Numeros 0-10 Spanish Numbers',
        'Shapres Mosaic Puzzle',
        'Tell the difference',
        'LumiKids Backyard',
        'LumiKids Beach',
        'LumiKids Park',
        'Chrome', 'TabPilot File Browser', 'PBS Parents Play and Learn',
        'ReadyRosie', 'WiFi Manager', 'Animal Sounds', 'Shadow Play', 'Waste Sorting',
        'Breathe Think Do']

use_time_start = 30
use_time_end = 1800

device_uuids = [
    "452aee44-c485-4b0a-ad51-8c9a1b883bfe",
    "b6e3e54f-fa8d-4a0d-a663-f8b43a55370f",
    "bc09f79b-4ffe-4b1d-bc9d-946dd3a04af9",
    "bf337d75-943c-4840-9327-263434ec9c47",
    "cbabd8f6-b290-4320-8d2a-70e8b1848afd",
    "dcd1f125-b083-41de-ab35-01971d77822f",
    "2c3fbc71-ff3e-479a-b81a-80a929a512ab",
    "e857d43f-5bef-4be2-9bae-29ffdb14e49b",
    "368f74b3-52a6-4245-ae4c-4c14e863b43e",
    "95d9e60e-05c6-48d2-b0f8-64263150fe6d",
    "35876564-9d03-4a26-8959-4629f36912a8",
    "6031411f-049f-4991-97b1-f3a425970de6",
    "10645f1d-65ff-4d5f-bf62-967b68ab1b03",
    "e6785440-cebb-4a06-ae76-e7b979b64051",
    "5bcd3eb0-f1bd-4cbb-af48-5eb4a37c9a63",
    "659c423e-185f-4f05-b936-16347feb1f76",
    "8ab22807-8eba-4062-bb1b-359e6b30eeeb",
    "83b9d05b-8819-4926-b592-55c3483f24c7",
    "f797d6f7-acc4-4651-a68a-c15434fd6e80",
    "7f6dbabd-1789-45f8-af31-0c7074647132",
    "31ffca08-c3bb-4499-bfe4-f4dad004a88a",
    "6a0a90e5-f857-40eb-abdc-5fb8d68a4a66",
    "8ceff646-b653-4fd2-a157-b9ea809f2b40",
    "86ed64e6-0633-4fbb-a7e6-53ce9f8293f0",
    "29a745be-f82c-4daa-989d-8ce43c6997a3",
    "74587b43-0c98-4e82-aead-4acb43143566",
    "0b250601-f9c3-4ebb-8821-aeecb38b4abd",
    "706a53a5-2c04-4dd6-bc05-6fc0d9fe3d86",
    "efe9345c-3907-45bf-9ee5-44fd38a32b1c",
    "26973935-27e3-4e9b-8fdb-11d6cb888f3f",
    "8b55bbff-32de-4089-ba04-23b66bfdde7b",
    "2fd7667b-5396-4fe8-8754-fb1188dc2902",
    "2d5fc76f-d511-400e-9b5b-7b8ba4491d56",
    "75f653f3-a6b9-4085-b734-c859efdd56dd",
    "08907ec8-4efe-4d92-94ef-f4ba6b179b1c",
    "0d51d9a4-e00e-4856-b743-956ac9eb0f40",
    "5fff78f4-d2dd-4ae6-b544-211903f5db47",
    "4905610f-90a4-47ff-92da-6456daac7349",
    "957035af-4695-4ea0-ab3a-6c5b2f7d0330",
    "d5124b5b-bba9-43fa-b461-676708da7655",
    "edf39e0e-3fa2-47f3-988b-e29214dc5a22",
    "2012f4e7-2697-415b-9d76-70b60d4056cc",
    "067ba588-bf3e-4a50-a761-548d1c938386",
    "0fa47247-e0a7-4a19-89fc-271e29ba3a7a",
    "55d6d873-fd4c-422f-af7c-084c064a66e1",
    "9b58dc17-88ce-4f7b-acdd-dba74be30952",
    "bc071e9d-c509-4df8-9c92-77155384c60d",
    "354f9f4b-60e3-418c-bf81-1294de458fd0",
    "d8087b74-1fae-4bc0-a002-1dc4db7e94eb",
    "e8d3eb51-4dba-4b42-a0f1-5c40a6cd7b58",
    "33958579-9deb-4601-8bd3-02e965330ec8",
    "6479b9ea-8e1b-4569-a393-5cbe40c10b9c",
    "9918bb2d-7aee-43f2-bdd8-76e5d2b585b7",
    "7a20e3f0-6b8a-47cd-8274-a8571e7d37bd",
    "2404544b-b657-4dc3-8962-18b46c333961",
    "d7d4e976-db7f-4227-92f7-3a04908d9114",
    "17d2c50a-a7ab-4c9f-a6c6-a77c98260d11",
    "df553bf4-566e-460e-aab8-47f1cbf7235c",
    "2cc7bc7a-fa56-4aa7-8956-f85bada1b189",
    "5e10a49b-6bfa-4765-bdbc-0e58627a97b2",
    "fc24fffe-8406-4431-aac8-dd4d5d759e30",
    "cc387283-4c9c-4dcc-b1e6-59b1a6aaa1c9",
    "2355dacd-5f91-4c70-9cfd-0e6ed7948b94",
    "bfc6cb00-a8c6-427f-abd4-d8d6bb559f43",
    "be0dfd62-ac16-4b07-95cb-d2be2b16f5de",
    "c3cd8295-ff3e-4e05-a126-06f7950042b4",
    "539bce70-e5ee-467f-a023-9fa9b29a2651",
    "58106433-32c0-4bdf-8fa5-9ded5bd36bb1",
    "dce76c83-9e16-43c6-8a81-e9b5dc7cc71f",
    "da254fa0-49c3-4f14-ac45-159caccaef7f",
    "d3ae259c-44d8-4074-b199-c7b7af50c08e",
    "721c4877-53d5-45fe-a4bd-69c70eb0bc27",
    "fd4f8336-a5da-4580-81da-4293d55e04be",
    "6fe28e1a-e472-4d1b-9a36-7823f143bc42",
    "404dbf88-2394-4e2a-9022-497c3ff7142a",
    "b07c7325-9b35-46c4-a8c9-17cbc3abaa4e",
    "f85bb461-e697-4b4a-9c5e-7b35e4e68e86",
    "dbf8e291-cec7-4ebc-9a98-17a9957ba256",
    "0bc0d455-a3a1-42a7-a472-d2136fa7059b",
    "647662e1-4e3c-4e3d-aad3-ee0d97404a9a",
    "26895af6-5e4e-4913-a893-c0c723c2fb15",
    "4aef4875-69da-488f-822c-2b768b9c852b",
    "ac9d91da-c1b4-494c-b490-2770fd4c0026",
    "e8dc280a-9ff0-4c7c-9d15-e6b07579fab6",
    "a7858c87-ab75-42a9-a848-1cac54138228",
    "9040bbcc-0d62-41d2-8aff-ed19dd98ba59",
    "52d6e484-9817-4de8-857e-4a93646aca01",
    "680c929f-b783-420d-b448-412df65df5ba",
    "2c5a16d0-68f7-418c-84d1-d4d9c039b12d",
    "2463186a-30c6-4947-84aa-b6a6bf324099",
    "4b0959ae-2bba-4bfb-ba6f-80fee08ecf67",
    "5de59d1d-1c25-47d5-b12b-b35d3bab3675",
    "e2720879-2322-4020-a122-0c1bd09525b6",
    "f11b58e2-fbe8-4905-9524-53a9d61542a5",
    "019f69cf-a3cd-4edd-ad87-e371248a9c6a",
    "9822aeb8-7187-4d3e-8a68-5094883b6c49",
    "e5e56c4a-c559-4bbf-b5cd-fdbd24115884",
    "3a530023-6416-40e5-b2c8-a2346747c3eb",
    "0997771e-c62a-44cc-9214-09e0ed312eb7",
    "82150bf0-306c-40f8-a279-6dee33686e88",
    "b1a8354a-1a58-4d60-a184-cbe96c7376e7",
    "76b2deab-9bdb-4136-b4af-29ffe0ec6b8f",
    "e9292d49-63f1-47e6-b8da-550e4d8af067",
    "e9886055-cfeb-4e77-8d80-f96afa9fe0b7",
    "b65db307-aa64-475c-bc5b-373118852120",
    "5263b253-2db6-4b74-92f5-c064a47af3e5",
    "8402be7a-6667-4d44-a4ed-3822c1a89473",
    "75c757bb-2d74-4d4d-b413-0c61e93de3ec",
    "96eb3591-cce4-406a-b3c6-573d3e17e541",
    "73c6f8e2-2812-486c-a17c-a1a0f5c0fafe",
    "cc95be8e-9239-4c61-b3cd-eb600af49cce",
    "a83ebe3c-ee25-4c56-8026-ef7ff2538c8d",
    "d71f9220-98ee-4378-a730-9b8363bd2378",
    "7583c65a-3ce5-4906-9091-0171df8dc33b",
    "8fb83740-756c-4d49-9495-f5f60d02e039",
    "8cddfbca-3f00-4350-b44e-b96ba04f2aa2",
    "3df1ce2a-5e4e-4284-b684-492306e958e8",
    "88978edc-f9cf-4af3-b798-32e30c413b75",
    "f3a38015-a7ad-45fb-83c5-0db2b4151d51",
    "88a39f0b-03a1-40cf-8711-cf8f878fba66",
    "06392446-e868-438c-af2e-e15c3490b6c5",
    "8849b165-1c6d-42ba-8875-6447b3ae1197",
    "69a33c85-4f94-4017-a246-367b4cf57577",
    "358e576e-4246-44c4-a4ea-76fd70450ea4",
    "f8e549ed-1d59-4863-abaf-6fb6a97ea3c2",
    "2286d490-2ae8-4cfa-8bbe-997aa2c02ece",
    "70c39861-e1f2-4816-9c2a-86dff3b12747",
    "34a9dbee-73ee-4dad-be96-2fb3e533d12a",
    "24c5d384-1269-4be0-ab71-24e25dbe4c0f",
    "255004f4-3a88-4494-bb45-117851ced0de",
    "20331cfe-022f-4523-829a-2175e9dc718f",
    "45ca8f66-d8bb-4bf5-ab07-b611b7ea2ffc",
    "85dc9861-f9ad-4d90-8846-70fb3045d9cc",
    "d990f24e-47e3-447f-a2f7-c423e66e90ad",
    "fc3b036e-f5cf-4c4b-a4a7-2ab8aad1e275",
    "7ebd0647-16ab-4f28-acf8-1c014a396463",
    "7ee47406-ef41-4f79-939c-31fe515176f2",
    "7bd45474-224e-4e1f-b6fa-3f63fd35c9cf",
    "bd7926a5-3dbe-4432-abcd-164d35fe64a2",
    "8aee0f56-3b5e-4151-a965-fd0647d1cc30",
    "52fd9003-4941-4f96-bdfe-f93271cadea5",
    "ee998f86-3240-4e7d-a826-8f3728c77a4a",
    "c85ad91b-95cb-45f7-9dfb-d42195aa8d17",
    "ad0b07a6-094d-4064-9e57-ed9766d08961",
    "f5cf68e8-1d83-44cb-96e8-b00fac64427e",
    "7cd700a2-f524-4b20-bcb9-b5111173b9af",
    "338e98b6-9d45-494a-bcb0-a50898fe6427",
    "eb0809ce-f4fd-4ddc-8c10-37107f3dc970",
    "5cb81083-0a99-46ae-bbea-c9db32154fd1",
    "f0cb6bc2-e4b1-4b6b-8901-893c0fb24096"
]

def generate_sample_set():
    temp_device_uuids = deepcopy(device_uuids)
    temp_int = random.randint(1,120)
    for i in xrange(temp_int):
        temp = random.choice(temp_device_uuids)
        temp_device_uuids.remove(temp)
        yield temp

records = []

def timeBetween(start,end,offset):
    #start = start.total_seconds()
    start = (start - W_EPOCH).total_seconds()
    end = (end - W_EPOCH).total_seconds()
    return start + (offset* (end-start))


W_EPOCH = datetime(1601, 1, 1)
day_start = date(year=2015, month=9, day=3)
day_end = date(year=2015, month=10, day=4)
daily = timedelta(days=1)
hourly = timedelta(hours=1)
while day_start < day_end:
    start_time = datetime.combine(day_start, time(7))
    end_time = datetime.combine(day_start, time(12))
    while start_time < end_time:
        for uuid in generate_sample_set():
            record = {}
            record['device'] = uuid
            minutes = timedelta(minutes=random.randint(0, 20))
            app_use_time = start_time + minutes
            #record['access_time'] = app_use_time.strftime('%s')
            record['access_time2'] = timeBetween(start_time,start_time + hourly,random.random())
            record['use_time'] = random.randint(use_time_start, use_time_end)
            record['app_name'] = random.choice(apps)
            records.append(record)
        start_time = start_time + hourly
    day_start = day_start + daily


with open('../data/data.json', 'w') as outfile:
    json.dump(records,outfile)
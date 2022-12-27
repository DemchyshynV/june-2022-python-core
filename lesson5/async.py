# import asyncio
#
# @asyncio.coroutines
# def print_nums():
#     num =1
#     while True:
#         print(num)
#         num+=1
#         yield from asyncio.sleep(0.1)
#
# @asyncio.coroutines
# def print_time():
#     time =1
#     while True:
#         print(time)
#         time+=1
#         yield from asyncio.sleep(1)
#
#
# @asyncio.coroutines
# def main():
#     task1 = asyncio.ensure_future(print_nums())
#     task2 = asyncio.ensure_future(print_time())
#     yield from asyncio.gather(task1, task2)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
##############################################################################
# NOT WORKING
##############################################################################

import asyncio

async def print_nums():
    num =1
    while True:
        print('NUM',num)
        num+=1
        await asyncio.sleep(0.1)

async def print_time():
    time =1
    while True:
        print('TIME',time)
        time+=1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task2)


asyncio.run(main())

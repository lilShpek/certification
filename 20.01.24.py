import requests
import time
import os
import threading
from multiprocessing import Process
import asyncio
from urllib.request import urlretrieve
import aiohttp

folder = 'data_task_2'
if not os.path.exists(folder):
    os.mkdir(folder)

def download_image(url):
    urlretrieve(url, os.path.join(folder, os.path.basename(url)))

async def async_download_image(session, url):
    async with session.get(url) as response:
        data = await response.read()
        filename = os.path.join(folder, os.path.basename(url))
        with open(filename, 'wb') as f:
            f.write(data)

def download_with_threads(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        tr = threading.Thread(target=download_image, args=(url,))
        threads.append(tr)
        tr.start()
    for i in threads:
        i.join()
    print(f'Threading downloaded in {time.time() - start_time:.2f} seconds')

def download_with_processes(urls):
    start_time = time.time()
    pr = []
    for url in urls:
        process = Process(target=download_image, args=(url,))
        pr.append(process)
        process.start()
    for i in pr:
        i.join()
    print(f'Multiprocessing downloaded in {time.time() - start_time:.2f} seconds')

async def download_with_async(urls):
    start_time = time.time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = async_download_image(session, url)
            tasks.append(task)
        await asyncio.gather(*tasks)
    print(f'Asyncronic downloaded in {time.time() - start_time:.2f} seconds')

if __name__ == '__main__':
    urls = [
        'https://i.pinimg.com/236x/93/ed/3a/93ed3af6411e1e8b997038c74c287a8a.jpg',
        'https://img.razrisyika.ru/kart/10/37936-ayu-dlya-detey-34.jpg',
        'https://bm.img.com.ua/img/prikol/images/large/0/0/307600.jpg'
    ]

    download_with_threads(urls)
    download_with_processes(urls)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_with_async(urls))

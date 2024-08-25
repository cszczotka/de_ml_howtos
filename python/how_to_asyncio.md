### Run procedure in asynchronous way

```python
import asyncio

async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello, Async World!")

asyncio.run(say_hello_async())
```


```python
import asyncio

async def say_hello_async():
    await asyncio.sleep(2)  # Simulates waiting for 2 seconds
    print("Hello, Async World!")

async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)  # Simulates doing something else for 1 second
    print("Finished another task!")

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )

asyncio.run(main())

```


### Run synchronus function in asyncio

```python
import asyncio
import time

def sync_task():
    print("Starting a slow sync task...")
    time.sleep(5)  # Simulating a long task
    print("Finished the slow task.")

async def async_wrapper():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sync_task)

async def main():
    await asyncio.gather(
        async_wrapper(),
        # Imagine other async tasks here
    )

asyncio.run(main())

```


### Execute http requests - aiohttp

```python
import requests
import time
import aiohttp
import asyncio

start_time = time.time()

def fetch(url):
    return requests.get(url).text

async def fetch_async(url, session):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        page1 = asyncio.create_task(fetch_async('http://example.com', session))
        page2 = asyncio.create_task(fetch_async('http://example.org', session))
        await asyncio.gather(page1, page2)

page1 = fetch('http://example.com')
page2 = fetch('http://example.org')

print(f"Done in {time.time() - start_time} seconds")


start_time = time.time()
asyncio.run(main())
print(f"Done async in {time.time() - start_time} seconds")
```


### Read files - aiofiles

```python
import asyncio
import aiofiles
import time

# Asynchronously reading a single file
async def read_file_async(filepath):
    async with aiofiles.open(filepath, 'r') as file:
        return await file.read()

async def read_all_async(filepaths):
    tasks = [read_file_async(filepath) for filepath in filepaths]
    return await asyncio.gather(*tasks)

# Running the async function
async def main():
    start_time = time.time()
    filepaths = ['data.csv', 'data2.csv']
    data = await read_all_async(filepaths)
    print(f"Done async read in {time.time() - start_time} seconds")
    print(data)


def read_file_sync(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def read_all_sync(filepaths):
    return [read_file_sync(filepath) for filepath in filepaths]

asyncio.run(main())

start_time = time.time()
filepaths = ['data.csv', 'data2.csv']
data = read_all_sync(filepaths)
print(f"Done sync read in {time.time() - start_time} seconds")
print(data)
```
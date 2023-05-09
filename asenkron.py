from dataclasses import dataclass
import aiohttp
import asyncio

async def get_page(session,url):
    async with session.get(url) as r:
        return await r.text()

async def get_all(session , url):
    tasks=[]
    for url in urls:
        task = asyncio.create_task(get_page(session,url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data

if __name__ == '__main__':
    urls=['https://www.usom.gov.tr/url-list.txt']
    results = asyncio.run(main(urls)) 
    for result in results:
        print(result)
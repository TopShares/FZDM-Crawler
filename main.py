#!/usr/bin/env python3

import asyncio
import re
import signal
import sys
import urllib.parse

import aiohttp


class Crawler:

    def __init__(self, rooturl, loop, maxtasks=100):
        self.rooturl = rooturl
        self.loop = loop
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.tasks = set()
        self.sem = asyncio.Semaphore(maxtasks, loop=loop)

        # connector stores cookies between requests and uses connection pool
        self.session = aiohttp.ClientSession(loop=loop)

    async def run(self):
        t = asyncio.ensure_future(self.addurls([(self.rooturl, '')]), loop=self.loop)
        await asyncio.sleep(1, loop=self.loop)
        while self.busy:
            await asyncio.sleep(1, loop=self.loop)

        await t
        await self.session.close()
        self.loop.stop()

    async def addurls(self, urls):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            if (url.startswith(self.rooturl) and
                    url not in self.busy and
                    url not in self.done and
                    url not in self.todo):
                self.todo.add(url)
                await self.sem.acquire()
                task = asyncio.ensure_future(self.process(url), loop=self.loop)
                task.add_done_callback(lambda t: self.sem.release())
                task.add_done_callback(self.tasks.remove)
                self.tasks.add(task)

    async def process(self, url):
        print('processing:', url)
        self.todo.remove(url)
        self.busy.add(url)
        try:
            resp = await self.session.get(url)
        except Exception as exc:
            print('...', url, 'has error', repr(str(exc)))
            self.done[url] = False
        else:
            if (resp.status == 200 and
                    ('text/html' in resp.headers.get('content-type'))):
                html = (await resp.read()).decode('utf-8', 'replace')  # html

                # urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', html)
                
                
                html = etree.HTML(html)
                urls = html.xpath('//*[@id="content"]//li//a//@href') # urls

                for u in urls:
                    
                    print("this page urls is " + u)
                # asyncio.Task(self.addurls([(u, url) for u in urls]))

            resp.close()
            self.done[url] = True

        self.busy.remove(url)
        print(len(self.done), 'completed tasks,', len(self.tasks), 'still pending, todo', len(self.todo))

    # TODO

    async def DetailProcess(self, url):
        pass


def main():
    loop = asyncio.get_event_loop()
    
    baseUrl = 'https://manhua.fzdm.com/56/'   # 七原罪
    c = Crawler(baseUrl, loop)
    asyncio.ensure_future(c.run(), loop=loop)

    try:
        loop.add_signal_handler(signal.SIGINT, loop.stop)
    except RuntimeError:
        pass
    loop.run_forever()
    print('todo:', len(c.todo))
    print('busy:', len(c.busy))
    print('done:', len(c.done), '; ok:', sum(c.done.values()))
    print('tasks:', len(c.tasks))


if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("total time: ", time.time() - start)

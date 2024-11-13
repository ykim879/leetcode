from threading import Thread, Lock
from queue import Queue # A thread-safe Queue 

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # Extract the host of the start URL
        f = lambda url: url.split('/')[2]
        hostname = f(startUrl)
        
        def worker():
            while not queue.empty():
                current_url = queue.get()
                with visited_lock:
                    # Skip if already visited
                    if current_url in visited:
                        continue
                    visited.add(current_url)

                # Crawl the current URL
                for url in htmlParser.getUrls(current_url):
                    if f(url) == hostname:  # Ensure same host
                        with visited_lock:
                            if url not in visited:
                                queue.put(url)

                queue.task_done()

        # Shared data structures
        visited = set([startUrl])  # To track visited URLs
        visited_lock = Lock()  # To synchronize access to the `visited` set
        queue = Queue()  # To manage URLs to crawl
        for url in htmlParser.getUrls(startUrl):
                if f(url) == hostname:  # Ensure same host
                        if url != startUrl:
                            queue.put(url)
        # Start threads
        num_threads = queue.qsize()
        threads = [Thread(target=worker) for _ in range(num_threads)]
        
        for thread in threads:
            thread.start()
        # Wait for all threads to finish
        for thread in threads:
            thread.join() 
        
        return list(visited)

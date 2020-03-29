import concurrent.futures
import requests
import threading
import time
#import psutil


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        res = f"Read {len(response.content)} from {url}"
        if debug:
            print(end='')
        time.sleep(.1)


def download_all_sites(sites, no_of_threads=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_threads) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    for no_of_threads in range(1, 50, 2):
        thread_local = threading.local()
        debug = True
        start_time = time.time()
        download_all_sites(sites, no_of_threads)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds using {no_of_threads} Threads")
        # print(f"Memory used:{psutil.virtual_memory()}")
"""

Prerequisites:
pip install requests
pip install beautifulsoup4
"""
import collections
import argparse

from timeit import default_timer
from urllib.parse import urldefrag, urljoin, urlparse
from threading import Thread, active_count
import time

import bs4
import requests

wrong_files = []
remove_http_get = False
pages_q = collections.deque()


def crawler(page_queue, pages, failed, crawled, domain):
    global pages_q
    sess = requests.session()
    while page_queue:
        url = page_queue.popleft()

        try:
            response = sess.get(url)
        except (requests.exceptions.MissingSchema,
                requests.exceptions.InvalidSchema):
            print("*FAILED*:", url)
            failed += 1
            continue
        if not response.headers['content-type'].startswith('text/html'):
            continue

        soup = bs4.BeautifulSoup(response.text, "html.parser")

        crawled.append(url)
        pages += 1
        pages_q.append([response.text, url])
        links = get_links(url, domain, soup)
        for link in links:
            if not url_in_list(link, crawled) and not url_in_list(link, page_queue):
                page_queue.append(link)
    print('{0} pages crawled, {1} links failed.'.format(pages, failed))


def get_links(page_url, domain, soup):
    global wrong_files, remove_http_get
    links = []
    bad_flag = False
    for a in soup.select('a[href]'):
        link = urldefrag(a.attrs.get('href'))[0]
        if link:
            for w_file in wrong_files:
                if link.find(w_file) >= 0:
                    bad_flag = True
                    break
            if bad_flag:
                bad_flag = False
                break
            if remove_http_get:
                link = link.split('?')[0]
            link = link if bool(urlparse(link).netloc) else urljoin(page_url, link)
            if same_domain(urlparse(link).netloc, domain):
                links.append(link)
    return links


def page_handler(response_text, url, i):
    print(url)
    path = 'D:\\links\\' + str(i) + '.html'
    new_file = open(path, 'w', encoding='utf8')
    new_file.write(str(response_text))
    new_file.close()


def split_domain(domain):
    count = domain.count('.')
    if count > 3:
        return domain.split('.')[-3] + '.' + domain.split('.')[-2] + '.' + domain.split('.')[-1]
    elif count > 1:
        return domain.split('.')[-2] + '.' + domain.split('.')[-1]


def same_domain(netloc1, netloc2):
    """
    samedomain('www.microsoft.com', 'microsoft.com') == True
    samedomain('google.com', 'www.google.com') == True
    """
    domain1 = split_domain(netloc1.lower())

    domain2 = split_domain(netloc2.lower())

    return domain1 == domain2


def url_in_list(url, listobj):
    http_version = url.replace('https://', 'http://')
    https_version = url.replace('http://', 'https://')
    return (http_version in listobj) or (https_version in listobj)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-rHttp', action='store_true', default=False,
                        dest='boolean_switch', help='Remove HTTP GET params')
    parser.add_argument('-sUrl', action='store', dest='url_value',
                        help='Store a main url value')
    parser.add_argument('-a', action='append', dest='collection',
                        default=[], help='Append wrong files')

    global pages_q, wrong_files, remove_http_get
    START = default_timer()
    THREADS_COUNT = 4
    results = parser.parse_args()
    remove_http_get = results.boolean_switch
    wrong_files = results.collection
    start_page = results.url_value
    page_queue = collections.deque()
    page_queue.append(start_page)
    crawled = []
    domain = urlparse(start_page).netloc

    pages = 0
    failed = 0
    i = 0

    for _ in range(THREADS_COUNT):
        thread_ = Thread(target=crawler, args=(page_queue, pages, failed, crawled, domain))
        thread_.start()
        time.sleep(0.5)

    while active_count() > 1:
        if len(pages_q):
            resp_data = pages_q.popleft()
            thread = Thread(target=page_handler, args=(resp_data[0], resp_data[1], i))
            thread.start()
            i += 1
        else:
            continue
    print("FINISHED")

    END = default_timer()
    print('Speed in pages per second = ' + str((END - START) / i))


if __name__ == "__main__":
    main()

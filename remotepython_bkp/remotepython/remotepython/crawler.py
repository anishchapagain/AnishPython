from typing import Tuple, List
from urllib.parse import urljoin
from parsel.selector import Selector, SelectorList
from requests import Session
import csv

def crawl_pagination(url, session) -> Tuple[List, str]:
    """download pagination page and return job and next page url if possible"""
    print(f'crawling page: {url}')
    response = session.get(url)
    job_urls, next_page_url = parse_pagination(response.text)
    # convert relative urls to absolute urls
    job_urls = [urljoin(url, job_url) for job_url in job_urls]
    if next_page_url:
        next_page_url = urljoin(url, next_page_url)
    print(f'  found {len(job_urls)} jobs')
    return job_urls, next_page_url


def parse_pagination(html) -> Tuple[List, str]:
    """find all job links and next page link in pagination html"""
    sel = Selector(text=html)
    jobs = sel.css('div.item h3 a::attr(href)').extract()
    next_page = sel.css('a[aria-label=Next]::attr(href)').extract_first()
    return jobs, next_page


def crawl_job(url, session) -> dict:
    """download individual job page and return job and next page url if possible"""
    print(f'    crawling job: {url}')
    response = session.get(url)
    return {
        'url': url,
        **parse_job(response.text)
    }


def parse_job(html) -> dict:
    """find job details in job listing page"""
    sel = Selector(text=html)
    # setup some processing helpers
    join = lambda css, sep='': sep.join(sel.css(css).extract()).strip()
    first = lambda css: sel.css(css).extract_first(' ').strip()

    item = {}
    item['title'] = sel.css('h2.title::text').extract_first()
    item['location'] = join('.job-meta a::text', ', ')
    item['job_type'] = join('ul.list-unstyled a::text')
    item['posted_date'] = join('div#affix-box p:contains("Posted:")::text').split(': ')[1]
    item['saved_times'] = join('div#affix-box div:contains("Saved ")>strong::text')
    item['description'] = join('div.box-item-details p ::text')
    item['views'] = first('div#affix-box li:contains("unique views")>strong::text')
    item['unique_views'] = first('div#affix-box li:contains("views")>strong::text')

    bullets = lambda css: [''.join(bullet.css('::text').extract()) for bullet in sel.css(css)]
    h4_bullet = 'div.box-item-details h4:contains("{}")+ul>li'.format
    h3_bullet = 'div.box-item-details h3:contains("{}")+ul>li'.format
    item['about_you'] = bullets(h4_bullet('About You'))
    item['your_role'] = bullets(h4_bullet('Your role'))
    item['requirements'] = bullets(h4_bullet('Requirements'))
    item['nice_to_have'] = bullets(h4_bullet('Nice to have'))
    item['why_work_with_us'] = bullets(h4_bullet('Why work with us'))
    item['desired_skills'] = bullets(h3_bullet('Desired Skills'))
    item['contact'] = bullets(h3_bullet('Contact Info'))

    return item


def crawl(start_url,total):    
    """
    Main crawl function - crawl all jobs from starting url
    e.g. https://www.remotepython.com/jobs/
    """
    page=1
    with Session() as session:
        next_page = start_url
        print("Crawl beginning with >> ",next_page)
        while next_page and page<=total:
            print(f"Crawling page {page} of {total}")
            job_urls, next_page = crawl_pagination(next_page, session)
            page+=1
            print(job_urls)
            
            i=0
            for job_url in job_urls:
                i+=1
                print(" >> Next Page >> ",next_page)
                yield crawl_job(job_url, session)
                
            print("Crawler Exiting!")

                
if __name__ == '__main__':
    totalPage=1 #No of pages to Search
    BASE_URL = 'https://www.remotepython.com/jobs/?q={}'.format
    start_url = BASE_URL('python') #Search Keyword
    csv_writer = None
    outfile = open("listings.csv","w") #output file 
    for job in crawl(start_url,totalPage):
        if not csv_writer:
            csv_writer = csv.DictWriter(outfile, job)
            csv_writer.writeheader()
        csv_writer.writerow(job)      

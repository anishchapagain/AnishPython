import csv
#import click
from lxml import etree, html
from remotepython.crawler import crawl
import remotepython as r


#BASE_URL = 'https://www.remotepython.com/jobs/?q={}'.format
BASE_URL = 'https://www.remotepython.com/jobs/'
BASE_URL = 'https://www.google.com/jobs/'
outfile = open('sample.csv',"w")

#@click.command()
#@click.argument('outfile', type=click.File('w'))
#@click.argument('search_keyword', required=False)
def main(outfile, search_keyword):
    """Crawler for remotepython.com jobs"""
    start_url = BASE_URL#(search_keyword)
    csv_writer = None
    for job in crawl(start_url):
        print(job)
        if not csv_writer:
            csv_writer = csv.DictWriter(outfile, job)
            csv_writer.writeheader()
        csv_writer.writerow(job)


if __name__ == '__main__':
    #print(dir(r).__spec__)
    main(outfile,'')

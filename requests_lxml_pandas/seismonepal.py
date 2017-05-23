import csv
from urllib.request import urlopen
import requests
import lxml.html as html
from lxml.etree import XPath
from pyquery import PyQuery as pq

BASE_URL = "http://www.seismonepal.gov.np"


def read_url(url):
    """ Read given Url , Returns pq() of page"""
    html = urlopen(url).read()
    return pq(html)


def get_page_rows(page):
    response = read_url(page)
    rows = response.find('div.block2-content table tr')
    print("count >> ", rows.__len__())
    data = list()
    for row in rows.items():
        edate = row.find('td').eq(0).find('span').text()
        etime = row.find('td').eq(1).find('span').text()
        elatitude = row.find('td').eq(2).find('span').text()
        elongitude = row.find('td').eq(3).find('span').text()
        emagnitude = row.find('td').eq(4).find('span').text()
        epicentre = row.find('td').eq(5).find('span').text().strip()
        if edate:
            data.append([edate, etime, elatitude, elongitude, emagnitude, epicentre])
    return data


def write_csv(mydict):
    with open('earthquake.csv', 'w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in mydict.items():
            if type(value) is not list:
                value = value.encode('utf-8')
                writer.writerow([key, value])


def writeto_csv(mydict):
    with open('earthquake.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["Date", "Time", "Latitude", "Longitude", "Magnitude", "Epicentre"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for list in mydict:
            writer.writerows(list)


if __name__ == '__main__':
    pages = ["http://www.seismonepal.gov.np/index.php?action=earthquakes&show=recent&page=%s" % page for page in
             range(1, 3)]
    data = list()
    for page in pages:
        scrape_page = get_page_rows(page)
        print("Finding Page >> ", page)
        data.append(scrape_page)

    writeto_csv(data)
    print('Completed')

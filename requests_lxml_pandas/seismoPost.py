import csv
import requests
from pyquery import PyQuery as pq

BASE_URL = "http://www.seismonepal.gov.np"

def read_url(url,year):
    """ Read given Url , Returns pq() of page"""
    #html = requests.get(url).content
    posting = {'year':year}
    headersValue ={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US,en;q=0.8',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'www.seismonepal.gov.np',
        'Origin':'http://www.seismonepal.gov.np',
        'Referer':'http://www.seismonepal.gov.np/index.php?action=earthquakes&show=past',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
    html = requests.post(url,data=posting,headers=headersValue).content
    return pq(html)

def get_page_rows(url,year):
    response = read_url(url,year)
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


def writeto_csv(mydict):
    with open('earthquake.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["Date", "Time", "Latitude", "Longitude", "Magnitude", "Epicentre"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for list in mydict:
            writer.writerows(list)


if __name__ == '__main__':
    years = [2018,2017,2016,2015]#,2014,2010,2001,2000,2012]
    postUrl = "http://www.seismonepal.gov.np/index.php?action=earthquakes&show=past"
    data = list()
    for year in years:
        scrape_page = get_page_rows(postUrl,year)
        print("Finding Page >> ", year)
        data.append(scrape_page)

    writeto_csv(data)
    print('Completed')

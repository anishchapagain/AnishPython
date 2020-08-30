import csv
import requests
from pyquery import PyQuery as pq

RAW_FILE = 'test.html'
BASE_URL = "http://events.sulekha.com/new-york-metro-area"

def get_page_rows(url,referer):
    headersValue ={
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Referer':referer
    }
    html = requests.get(url,headers=headersValue)
    print(type(html))
    response = pq(html.content)
    #print(response)
    print(type(response))
    with open('test.html', 'w') as f:
        f.write(response)

    '''rows = response.find('div.block2-content table tr')
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
    '''


def writeto_csv(mydict):
    with open('sulekha_events.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["Date", "Time", "Latitude", "Longitude", "Magnitude", "Epicentre"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for list in mydict:
            writer.writerows(list)


if __name__ == '__main__':
    mainUrl = "http://events.sulekha.com/new-york-metro-area"
    referer = 'http://events.sulekha.com/'
    data = list()
#    scrape_page = get_page_rows(mainUrl,referer)
    get_page_rows(mainUrl,referer)
    print("Finding Page >> ")
    #data.append(scrape_page)

    #writeto_csv(data)
    print('Completed')

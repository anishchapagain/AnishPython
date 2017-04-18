import lxml.html
from lxml.etree import XPath as xpath
from lxml import etree
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt

def earthquake(page):
    response = requests.get(page)
    print("Finding >>> ", page)
    print("Status : ",response.status_code)
    # print("Response Type >>> ", response.content)

    details = []
    response = lxml.html.parse(page)
    rows = response.xpath("//div[@class='block2-content']//table[contains(.,'Date')]/tr[position()>1]")
    print("count >> ", rows.__len__())

    count=0
    for row in rows:
        edate = row.xpath('td[1]/span//text()')[0]
        etime = row.xpath('td[2]/span//text()')[0]
        elatitude = row.xpath('td[3]/span//text()')[0]
        elongitude = row.xpath('td[4]/span//text()')[0]
        emagnitude = row.xpath('td[5]/span//text()')[0]
        epicentre = row.xpath('td[6]/span/a//text()')[0]
        if edate:
            # details.append([edate[0], etime[0], elatitude[0], elongitude[0], emagnitude[0], epicentre[0]])
            details.append([edate, etime, elatitude, elongitude, emagnitude, epicentre])
            count = count + 1

        if count > 5:
            print(details)
            break


    return details

def writeto_csv(quakedata):
    with open('earthquake.csv', 'wb') as csv_file:

        writer = csv.DictWriter(csv_file,
        fieldnames=["Date", "Time", "Latitude", "Longitude", "Magnitude", "Epicentre"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for eachRow in quakedata:
            writer.writerows(eachRow)

def plot_data():
    df = pd.read_csv('earthquake.csv',parse_dates=['Date'],index_col=['Date'],dayfirst=True)
    ax = df[['Magnitude']].plot(kind='bar',title ="Magnitude Date Wise", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Magnitude", fontsize=12)
    plt.show()


if __name__ == '__main__':
    quakeLists=[]
    pages = ["http://www.seismonepal.gov.np/index.php?action=earthquakes&show=recent&page=%s" %
             page for page in xrange(1, 2)]
    # for page in pages:
    #     rows = earthquake(page)
    #     quakeLists.append(rows)

    print("Completed Scraping Pages")
    # writeto_csv(quakeLists) # using csv
    plot_data()





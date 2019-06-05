from lxml.html import parse,fromstring,document_fromstring
import requests
from lxml.etree import XPath
url = "http://hamrobazaar.com/latestfull.php"
date = '2016-11-06'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
doc = requests.get(url, headers=headers)
print(doc.status_code)
html = fromstring(doc.content)

#Try loop for table[5] and above
rows_xpath = XPath("//html//text()")
#/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table[5]/tbody/tr[1]/td[3]/a[1]/font/b
#rows_xpath = XPath("//table[1]/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table[5]")
name_xpath = XPath("tr[1]/td//text()")
#name_xpath = XPath("tr[1]/td[3]/a[1]/font/b//text()")

#seller_xpath = XPath("tr[1]/td[3]/a[2]/text()")
#date_xpath = XPath("tr[1]/td[4]/text()")
#price_xpath = XPath("tr[1]/td[5]/b/text()")

#html = fromstring(text)
print(rows_xpath(html))
quit()

import lxml.html
from lxml.etree import XPath
# url = "http://gbgfotboll.se/information/?scr=table&ftid=51168"
url = "http://gbgfotboll.se/information/?scr=table&ftid=62068"
date = '2016-11-06'

rows_xpath = XPath("//*[@id='content-primary']/table[1]/tbody/tr[td[1]/span/span//text()='%s']" % (date))
time_xpath = XPath("td[1]/span/span//text()[2]")
team_xpath = XPath("td[2]/a/text()")
result_xpath = XPath("td[3]/a/span/text()")
place_xpath = XPath("td[4]/a/text()")

html = lxml.html.parse(url)
details = []
for row in rows_xpath(html):
    time = time_xpath(row)[0].strip()
    team = team_xpath(row)[0]
    score = result_xpath(row)[0]
    venue = place_xpath(row)[0]
    details.append([time,team,score,venue])

print(details)
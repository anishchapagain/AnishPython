# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:54:33 2016
@author: PETERCHAPAGAIN
"""

import requests
import json


def get_reviews(url, product_id, limit, offset_value, page_break):
    temp_data = []
    total_page = 1
    page = 1
    while total_page:  # True
        response = requests.get(url.format(product_id, limit, offset_value))
        content = response.content.decode("utf8")
        js = json.loads(content)

        total_results = js['BatchedResults']['q0']['TotalResults']
        reviews = js['BatchedResults']['q0']['Results']

        if page == 1:
            print ("Total Results : " + str(page))
            print (total_results)
            total_page = int(round(total_results / 100))

        print ("Page " + str(page) + " of " + str(total_page) + "\n")
        i = 0
        if total_results > 0:
            for review in reviews:
                i += 1
                print (str(review['Title']) + " >> " + str(review['Rating']))
                temp_data.append(review['Title'])
                # if i == 10:
                #      break

        offset_value += 100
        page += 1
        if page_break:
            if page == page_break:
                break
    return temp_data

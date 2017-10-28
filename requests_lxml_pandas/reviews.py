import requests
import json
import readapi
import pickle

# #100106145   100307497
# List for All Review
data = []
product_id = limit = offset_value = page_break = ''
url = 'http://api.bazaarvoice.com/data/batch.json?' \
      'passkey=bai25xto36hkl5erybga10t99&apiversion=5.5&resource.q0=reviews' \
      '&filter.q0=productid%3Aeq%3A{0}' \
      '&filter.q0=contentlocale%3Aeq%3Aen_CA%2Cen_US&sort.q0=submissiontime%3Adesc&stats.q0=reviews&filteredstats.q0=reviews' \
      '&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_CA%2Cen_US' \
      '&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_CA%2Cen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_CA%2Cen_US' \
      '&limit.q0={1}&offset.q0={2}&limit_comments.q0=1'


def main():
    """ Enter Product Id """
    global product_id
    product_id = raw_input("Enter Product ID >> ")


def write_output(list):
    fp = open('text.txt','wb')
    json.dump(list, fp)
    # fp.write("\n".join(list))


if __name__ == '__main__':
    # main()
    # print main.__doc__
    print product_id
    temp_data = readapi.get_reviews(url, product_id=100106145, limit=23, offset_value=0, page_break=2)
    data = temp_data[:]
    print "Length >> " + str(len(data))
    write_output(data)
    # print data

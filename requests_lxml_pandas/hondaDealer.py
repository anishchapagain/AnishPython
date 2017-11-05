import requests
import json
import csv
import os

url='https://www.honda.com.br/concessionarias/api/'
filename='hondaDealer.csv'

response = requests.get(url)
content = response.content
print("Searching Dealers from Honda......")
dealersContent = response.content.decode("utf8")
print("\n Dealers Content [0]: ",dealersContent[0])
print("Converting JSON information for python json lib......")
dealers = json.loads(dealersContent)
totalDealers = len(dealers)

if totalDealers>0:
    print("Total Dealers Found: ",totalDealers)
    print("\n Dealers [0]: ",dealers[0])    
    print("\nLoop through Dealers-Json Data and collect required info for CSV")
    with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'w+',newline='') as f:
        writer = csv.writer(f)#csv.writer using file
        #Providing Column Names for Selected Data
        writer.writerow(['ID', 'Title', 'City', 'State','Latitude','Longitude']) 
        for i in range(0,totalDealers):
            if i==0:
                print("\n Writing Data to CSV starting...")
            #preparing row of Data for CSV
            row = [
                i + 1,
                dealers[i]['title'],
                dealers[i]['field_dealer_cidade'],
                dealers[i]['field_dealer_estado'],
                dealers[i]['field_geolocation'],
                dealers[i]['field_geolocation_1']
                ]
            writer.writerow(row)
            if i==totalDealers:
                print("\n Writing Data to CSV ending now...")
            if i==10:
                break
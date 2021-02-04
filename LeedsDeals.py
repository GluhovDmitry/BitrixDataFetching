from fast_bitrix24 import Bitrix
import csv 
from webtoken import webhook
import time

while 1:
    #get webhook from file
    b = Bitrix(webhook)
    #get leads to list
    leads = b.get_all('crm.lead.list')
    #get deals to list
    deals = b.get_all('crm.deal.list')
    #function that imports data from list to csv
    def to_csv(path, data):
        with open(path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(data[0])
            for line in data:
                writer.writerow(line.values())

    to_csv('leads.csv', leads)

    to_csv('deals.csv', deals)
    
    #the script works 1 time in 1 hour
    time.sleep(60*60)
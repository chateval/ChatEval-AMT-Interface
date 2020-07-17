import boto3
import sys
import xmldict
import csv
import pandas as pd



#create a HIT on sandbox
#endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
#create a live HIT
endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'
#joao's login
joao_id = ""
joao_key = ""
#lyle's login
lyle_id = ""
lyle_key = ""
mturk = boto3.client(
	'mturk',
	endpoint_url = endpoint_url,
	aws_access_key_id = lyle_id,
	aws_secret_access_key = lyle_key,
	region_name ='us-east-1')

def notify():
	workers = []
	with open('3A9LA2FRWSE8QTZ2VA8EORMX7CWXH2.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if 'WorkerId' in row:
				continue
			else:
				workers.append(row[0])
	mturk.notify_workers(
		Subject='Empathic Conversation HIT',
		MessageText='Hello, you have just been given a qualification for the Empathic Conversation HITs, please look to the following form for information on the HIT https://docs.google.com/forms/d/e/1FAIpQLSe193IyA1IPAPZOfRXW9D_ak1WZ0pupRWy3a6dAFKV51vfztg/viewform?usp=pp_url',
		WorkerIds=workers)


		

if __name__=="__main__":
        # notigy workers
        notify()






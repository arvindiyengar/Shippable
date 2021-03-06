'''
	This script takes the github url and displays count of open isues for past 24 hrs , 1 week and greater than 1 week 
'''
import os
import sys
import uuid
import json
import datetime

githubLink=sys.argv[1]
count={"24hrs":0,"1week":0,"greater1week":0}


abc=githubLink[8:].split('/')
page_id=1
#Generate the unique filename which can be consumed later on
filename="curl_output_"+str(uuid.uuid4())+".json"
curlString='curl -XGET https://api.github.com/repos/'+abc[1]+'/'+abc[2]+"/issues?page=1 > "+filename
os.system(curlString)
f=open(filename)
json_object={}
json_object=json.load(f)
tmp=json_object
f.close()
os.remove(filename)

while(len(json_object)>0):
#Get the current datetime in ISO format 
	currentdate=datetime.datetime.now()

	for a in json_object:
		#print (a)
		d=datetime.datetime.strptime(a['created_at'],"%Y-%m-%dT%H:%M:%SZ")
		current=currentdate-(d)
		
		if(current.days==0):
			count["24hrs"]=count["24hrs"]+1
		elif(current.days>7):
			count["greater1week"]=count["greater1week"]+1
			count["24hrs"]=count["24hrs"]+1
		else:
			count["1week"]=count["1week"]+1

	

	
	
	filename="curl_output_"+str(uuid.uuid4())+".json"
	print (curlString)
	page_id=page_id+1
	curlString='curl -XGET https://api.github.com/repos/'+abc[1]+'/'+abc[2]+"/issues?page="+str(page_id)+" > "+filename

	os.system(curlString)
	f=open(filename)
	
	json_object=json.load(f)

	tmp=json_object
	
	f.close()
	os.remove(filename)

print("\nOpenIssues count for Past 24 hrs : ",count["24hrs"])
print("OpenIssues count for Past 1 week : ",count["1week"])
print("OpenIssues count for greater than 1 week : ",count["greater1week"])

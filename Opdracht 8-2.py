thisdict = {
    "First name": input("First name:"),
    "Last name": input("Last name:"),
    "Job title ": input("Job Title:"),
    "Company": input("Company:")
    }
#print(thisdict)
#for x,y in thisdict.items():
    #print(x,y)
import csv
#with open('newkv.csv','w',encoding= 'UTF8') as f:
    #writer=csv.writer(f)
    #writer.writerow(thisdict.items())
with open('newkv.csv','a') as f:
    writer=csv.writer(f)
    writer.writerow(thisdict.items())

import pandas as pd
import numpy as np
import math
import csv

data = pd.read_csv("Pre.csv", sep=',', header=None)
comfortList = [x for x in data[0] if str(x) != 'nan']
mainComfortList = []

importanceList = [x for x in data[1] if str(x) != 'nan']
mainImportanceList = []

understandingList = [x for x in data[2] if str(x) != 'nan']
mainUnderstandingList = []

agreementList = [x for x in data[3] if str(x) != 'nan']
mainAgreementList = []

for i in comfortList:
    realList = []
    temp = i.split(":")
    temp.pop(0)
    for x in temp:
        holder = x.split(",")
        realList.append(holder[0])
    mainComfortList.append(realList)
mainComfortList.pop(0)
print(mainComfortList[0])


fields = ['Accessing UW Libraries to study', 'Working with other students to understand course materials', 'Working with other students to explain course materials', 'Working with other students to prepare for an exam, quiz, or large assignment']
filename = "Comfort.csv"

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
        
    csvwriter.writerow(fields) 
        
    csvwriter.writerows(mainComfortList)

for i in importanceList:
    realList = []
    temp = i.split(":")
    temp.pop(0)
    for x in temp:
        holder = x.split(",")
        realList.append(holder[0])
    mainImportanceList.append(realList)
mainImportanceList.pop(0)
print(mainImportanceList[0])


fields = ['Accessing UW Libraries to Study', 'Establishing a Study Group', 'Identifying a Study Location', 'Understanding Frequency and Duration for Successful Studying', 'Time Management']
filename = "Importance.csv"

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
        
    csvwriter.writerow(fields) 
        
    csvwriter.writerows(mainImportanceList)


for i in understandingList:
    realList = []
    temp = i.split(":")
    temp.pop(0)
    for x in temp:
        holder = x.split(",")
        realList.append(holder[0])
    mainUnderstandingList.append(realList)
mainUnderstandingList.pop(0)
print(mainUnderstandingList[0])


fields = ['Strategies for distributing your work evenly throughout the semester', 'Techniques to implement specific test strategies for before, during and after a test', 'Strategies for better understanding and retention of course content', 'Methods for creating short and long-term study goals', 'Strategies for maintaining an up-to-date calendar', 'Setting priorities for each day, week, month, and year']
filename = "Understanding.csv"

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
        
    csvwriter.writerow(fields) 
        
    csvwriter.writerows(mainUnderstandingList)


for i in agreementList:
    realList = []
    temp = i.split(":")
    temp.pop(0)
    for x in temp:
        holder = x.split(",")
        realList.append(holder[0])
    mainAgreementList.append(realList)
mainAgreementList.pop(0)
print(mainAgreementList[0])


fields = ['I know how to access UW Libraries to find information', 'I know that UW Academic Support Services (tutoring, Writing Center, etc.) can help me to succeed', 'I know how to access UW Academic Support Services', 'I know how to access the UW Wellness Center', 'I know UW Student Support Services (Counseling, Financial Aid, etc.) can support my overall wellbeing', 'I know how to access UW Student Support Services']
filename = "Agreement.csv"

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
        
    csvwriter.writerow(fields) 
        
    csvwriter.writerows(mainAgreementList)

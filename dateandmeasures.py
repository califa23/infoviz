import csv

from datetime import datetime


sheet = open('readings.csv')
csv_sheet = csv.reader(sheet)
next(csv_sheet)
sample_id = [] #0
#Sample value is located in index 1 however for this script its unnecessary to populate
sample_locations = [] #2
string_dates = [] #3
sample_measure = [] #4
datetime_dates = []

for row in csv_sheet:
    sample_id.append(row[0])
    sample_locations.append(row[2]) 
    string_dates = row[3]
    datetime_dates.append(datetime.strptime(string_dates, '%d-%b-%y'))
    sample_measure.append(row[4])

for i in range(len(sample_id)):
    if datetime_dates[i] not in dates:
        dates.append(datetime_dates[i])


dateandmeasures = {}

for date in dates:
    dateandmeasures[date] = 0
    
for date in dates:
    for row in datetime_dates:
        if date == row:
            dateandmeasures[date] = dateandmeasures[date] + 1
print(dateandmeasures)

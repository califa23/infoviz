import csv
import sys
import argparse
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


#for argument passing
parser = argparse.ArgumentParser()
#arg 1 is sample location
parser.add_argument('--location', help='yields net sample count for a specific location (use all for all locations)')
#parser.add_argument('--sampleCount', help='yields net sample count for a specific location (use all for all locations)')
#arg 2 is sample chemical

#arg 3 specify algorithm
parser.add_argument('--alg', help='counts amount of consecutive 0s for given location (use all for all locations)')

#arg 4 toggle visualization
parser.add_argument('--v', help='toggle visualization')



#returns number of readings per week for all locations
def netSampleCount():
    #enddate = datetime_dates[len(datetime_dates)-1]
    sample_counts = [] 
    startyear = datetime_dates[0].year
    startweek = datetime_dates[0].isocalendar()[1]
    for date in datetime_dates:
        week = date.isocalendar()[1] + ((date.isocalendar()[0] - startyear) * 52)
        while len(sample_counts) < week:
         sample_counts.append(0)
        sample_counts[week-startweek] += 1
    return sample_counts


#takes location of sensors
#returns number of readings per week
def sampleCountForSensor(location):
    samplelocation = location
    sample_counts = [] 
    startyear = datetime_dates[0].year
    startweek = datetime_dates[0].isocalendar()[1]
    x = 0
    for date in datetime_dates:
        currLocation = sample_locations[x]
        week = date.isocalendar()[1] + ((date.isocalendar()[0] - startyear) * 52)
        while len(sample_counts) < week:
            sample_counts.append(0)
        if samplelocation == currLocation:
            sample_counts[week-startweek] += 1
        x += 1
    return sample_counts


#takes set of all readings
#returns highest amount of consecutive weeks with no readings
def countConsecZeros(samples):
    highestCount = 0
    count = 0
            
    for i in range(len(samples)):
        if samples[i] == 0:
            count += 1
            if count > highestCount:
                highestCount = count
        else:
            count = 0
    return highestCount


#open data
sheet = open('readings.csv')
csv_sheet = csv.reader(sheet)
next(csv_sheet)

#create lists for each column
sample_id = [] #0
#Sample value is located in index 1 however for this script its unnecessary to populate
sample_locations = [] #2
string_dates = [] #3
sample_measure = [] #4

datetime_dates = []#for date transform
distinct_locatiions = ['Boonsri', 'Kannika', 'Chai', 'Kohsoom', 'Somchair', 'Sakda', 'Busarakhan', 'Tansanee', 'Achara', 'Decha']

#append data to corresponding column
for row in csv_sheet:
    sample_id.append(row[0])
    sample_locations.append(row[2]) 
    string_dates = row[3]
    datetime_dates.append(datetime.strptime(string_dates, '%d-%b-%y'))
    sample_measure.append(row[4])







args = parser.parse_args()

#if visual is toggled show correct visualization
if args.v:
    #if consecutive 0 count is selected
    if args.alg == 'cZero':
        if args.location:
            print(countConsecZeros(sampleCountForSensor(args.location)))
        else:
            locationsMissCount = []
            for location in distinct_locatiions:
                locationsMissCount.append(countConsecZeros(sampleCountForSensor(location)))
            plt.xlabel('Locations')
            plt.ylabel('Consecutive Weeks')
            plt.title('Highest Consecutive Weeks of No Readings Per Location')
            plt.bar(distinct_locatiions,locationsMissCount)
            plt.show()

    #if sample count selected
    if args.alg == 'sampleC':
        if args.location:
            print(sampleCountForSensor(args.location))
            plt.plot(sampleCountForSensor(args.location))
            plt.show()
        else:
            print(netSampleCount())
            plt.plot(netSampleCount())
            plt.show()


    
        

#if args.zeroCount:
#    if args.v:
#        if args.zeroCount == 'all':
#            locationsMissCount = []
#            for location in distinct_locatiions:
#                locationsMissCount.append(countConsecZeros(sampleCountForSensor(location)))
#            plt.xlabel('Locations')
#            plt.ylabel('Consecutive Weeks')
#            plt.title('Highest Consecutive Weeks of No Readings Per Location')
#            plt.bar(distinct_locatiions,locationsMissCount)
#            plt.show()
#        else:
#            print(countConsecZeros(arg.zeroCount))
#    else:
#        if args.zeroCount == 'all':
#            for location in distinct_locatiions:
#                print(location,": ", countConsecZeros(sampleCountForSensor(location)))
#        else:
#            print(countConsecZeros(arg.zeroCount))
#
#    
#if args.sampleCount:
#    if args.sampleCount == 'all':
#        for location in distinct_locatiions:
#            print(location,": ", sampleCountForSensor(location))
#    else:
#        print(sampleCountForSensor(args.sampleCount))




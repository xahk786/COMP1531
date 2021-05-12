import datetime
from datetime import datetime
import csv

def weather(date, location):
    av_max_list = []
    av_min_list = []
    
    check_loc_list = []
    check_date_list = []

    
    try:
        datetime.strptime(date, '%d-%m-%Y')        
    except ValueError:
        return (None, None)       
        
        
    #og = datetime.strptime(date, '%d-%m-%Y')
    convert = datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
    #convert = og.strftime('%Y-%m-%d')

    with open('weatherAUS.csv') as f:
        reader = csv.reader(f)
        
        for row in reader:
            check_loc_list.append(row[1])
            check_date_list.append(row[0])
        
        if location not in check_loc_list:
            return (None, None)
        
        if convert not in check_date_list:
            return (None, None)        
        
                    
    
    with open('weatherAUS.csv') as f:
        reader = csv.reader(f)
        
        
        for row in reader:
        
            if row[1] == location:
                if row[2] == 'NA' or row[3] == 'NA':
                    av_max_list.append(0.0)
                    av_min_list.append(0.0)
                else:
                    av_max_list.append(float(row[3]))
                    av_min_list.append(float(row[2]))
            
            if str(row[0]) == convert and row[1] == location:
                maximum = float(row[3])
                minimum = float(row[2])


        denominator_max = len(av_max_list)
        denominator_min = len(av_min_list)
        
        average_max = sum(av_max_list)/denominator_max
        average_min = sum(av_min_list)/denominator_min
        
        final_max = maximum - average_max
        final_min = average_min - minimum
    
    
    return round(final_min,1), round(final_max,1)

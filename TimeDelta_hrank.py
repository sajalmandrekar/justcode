#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def to_num(month):
    month_name = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
    for i in range(12):
        if month_name[i]==month:
            return i+1

def days_in_month(n,year):
    if(n == 1 or n==3 or n==5 or n == 7 or n==8 or n == 10 or n==12):
        return 31
    elif (n==2):
        if(year%4==0):
            return 29
        else:
            return 28
    else:
        return 30

def time_delta(t1, t2):
    #for timestamp t1
    t1_day = t1[0:3]
    t1_date = int(t1[4:6])
    t1_month = to_num(t1[7:10])
    t1_year = int(t1[11:15])
    t1_hour = int(t1[16:18])
    t1_min = int(t1[19:21])
    t1_sec = int(t1[22:24])
    t1_tzone = int(t1[25:30])

    t1_time_sec = t1_hour*3600 + t1_min*60 + t1_sec
    t1_time_sec -= (t1_tzone//100)*3600 + (t1_tzone%100)*60
    
    if t1_time_sec<0:
        t1_time_sec = 86400 - t1_time_sec
        t1_date -= 1
    else:
        t1_date += t1_time_sec//86400
        t1_time_sec = t1_time_sec % 86400

    if t1_date > days_in_month(t1_month,t1_year):
        t1_date=1
        t1_month+=1
        if t1_month>12:
            t1_month = 1
            t1_year +=1
    elif t1_date==0 :
        t1_month -=1
        if t1_month==0:
            t1_month = 12
            t1_year -= 1
        t1_date = days_in_month(t1_month,t1_year)
    

    #for timestamp t2
    t2_day = t2[0:3]
    t2_date = int(t2[4:6])
    t2_month = to_num(t2[7:10])
    t2_year = int(t2[11:15])
    t2_hour = int(t2[16:18])
    t2_min = int(t2[19:21])
    t2_sec = int(t2[22:24])
    t2_tzone = int(t2[25:30])

    t2_time_sec = t2_hour*3600 + t2_min*60 + t2_sec
    t2_time_sec -= (t2_tzone//100)*3600 + (t2_tzone%100)*60    
    


    t_delta = 0
    dif_years = t2_year-t1_year
    dif_month = dif_years*12 + t2_month-t1_month
    
    # I left here
    X = 0
    i=t1_month
    while i<t2_month and i<=12:
        X += days_in_month(i,t1_year)
    
    

    dif_days = dif_month*X + t2_day-t1_day
    
    
    return t_delta



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

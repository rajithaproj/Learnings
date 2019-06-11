# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:52:32 2019

@author: Rajit
"""
#changes made
#Updated by Rajitha
# This is added by Monu
#yearOfBirth =int( input("enter your year of birth : "))
#
#present_year = 2019
#
#age = present_year - yearOfBirth
#
#print("person age is: ",age)

#person = "Python"
# #is_friend = True
#aggresive = True
#if (is_friend and not aggresive):
#    print("Invite "+person +" to party")
#
#else:
#    print("don't invite "+ person + " to part")
#    
#length =int( input("enter the lenth="))
#unit = str(input ("enter the units in 'C','M'")).lower()
#
#
#
#if unit == "m" :
#    length= length*100
#    
#    print("length in cms="+str(length) +" cms")
#    
#elif unit == "c" :
#    print("length="+str(length/100)+" M")
#    
#else:
#    print("Unknown value")

#for i in range(0,5):
#    for j in range(0,5):
#        print ((i ,j))

#list1 = [3,6,4,8,9,10]
##maxim = list1[0]
#
##for i in list1:
##    if i>maxim :
##        maxim = i
#        
#print(max(list1))
is_car_started = False
while True:
    command = (input("enter either car need to 'start' or 'stop' or you need any 'help' ")).upper()
    
    if command == 'START':
        if is_car_started:
            print("car has already started")
        else:
            print("START THE CAR")
            is_car_started =True
    elif command == 'STOP':
        if is_car_started:
            print("STOP THE CAR")
            is_car_started = False
        else:
            print("Car already 'STOPED' just give 'start' to contine")
            
    elif command == 'HELP':
        print("You need help so type either START or STOP")
        
    elif command == 'EXIT':
        print("EXIT")
        break
    
    else:   
        print("Enter valid command")


    
































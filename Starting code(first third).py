import time    
import pickle
import os
class Hospital:
    def _init_(self):
        self.name=" "
        self.age=0
        self.sex=" "
        self.doctor=" "
        self.med=" "
        self.allergies=" "
        self.fdrink=" "
        self.temp=" "
        self.rtemp=" "
        self.plevel=" "

    def Input(self):
        self.name=raw_input("Enter Patinet's Name:")
        self.age=input("Enter Patinet's Age:")
        self.sex=raw_input("Enter Patinet's Sex (Male/Female):")
        self.doctor=raw_input("Enter Doctor's Name:")
        self.med=raw_input("Enter Prescribed Medicine:")
        self.allergies=raw_input("Enter Known Allergies:")
        self.fname=raw_input("Enter Favorite Drink:")
        self.temp=raw_input("Enter last known Temperature:")
        self.rtemp=raw_input("Enter Preferred Room Temperature:")
        self.plevel=raw_input("Enter Pain Level:")
 def Output(self):
        print ("PATIENT'S NAME:-"),self.name
        print ("PATIENT'S AGE:-"),self.age
        print ("PATIENT'S SEX:-"),self.sex
        print ("DOCTOR'S NAME:-"),self.doctor
        print ("PRESCRIBED MEDICINES:-"),self.med
        print ("KNOWN ALLERGIES:-"),self.allergies
        print ("FAVORITE DRINK:-"),self.fdrink
        print ("LAST KNOWN TEMP:-"),self.temp
        print("PREFERRED ROOM TEMP:-"),self.rtemp
        print("PAIN LEVEL:-"),self.plevel

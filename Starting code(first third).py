import time    
import pickle
import os
class Hospital:
    def _init_(self):
        self.name=" "
        self.age=0
        self.sex=" "
        self.fdrink=" "
        self.doctor=" "
        self.med=" "
        self.allergies=" "

    def Input(self):
        self.name=raw_input("Enter Patinet's Name:")
        self.age=input("Enter Patinet's Age:")
        self.sex=raw_input("Enter Patinet's Sex (Male/Female):")
        self.fname=raw_input("Enter Favorite Drink:")
        self.doctor=raw_input("Enter Doctor's Name:")
        self.med=raw_input("Enter Prescribed Medicine:")
        self.allergies=raw_input("Enter Known ALlergies:")
 def Output(self):
        print ("PATIENT'S NAME:-"),self.name
        print ("PATIENT'S AGE:-"),self.age
        print ("PATIENT'S SEX:-"),self.sex
        print ("FAVORITE DRINK:-"),self.fdrink
        print ("DOCTOR'S NAME:-"),self.doctor
        print ("PRESCRIBED MEDICINES:-"),self.med
        print ("Known Allergies:-"),self.allergies
        
        

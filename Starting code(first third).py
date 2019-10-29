import time    
import pickle
import os
class Hospital:
    def _init_(self):
        self.name=' '
        self.age=0
        self.sex=""
        self.email=" "
        self.fdrink=" "
        self.address=''
        self.city=''
        self.state=''
        self.height=0
        self.weight=0
        self.doctor=''
        self.med=''
        self.bill=0
        self.paymethod=''
        self.pno=0
        self.dname=''

 def Input(self):
        self.name=raw_input("Enter Patinet's Name:")
        self.age=input("Enter Patinet's Age:")
        self.sex=raw_input("Enter Patinet's Sex (Male/Female):")
        self.height=input("Enter Patinet's Height:")
        self.weight=input("Enter Patinet's Weight(In Kgs):")
        self.fname=raw_input("Enter Favorite Drink:")
        self.address=raw_input("Enter Address:")
        self.city=raw_input("Enter City:")
        self.state=raw_input("Enter State:")
        self.pno=input("Enter Phone number:")
        self.email=raw_input("Enter E-Mail:")
        self.doctor=raw_input("Enter Doctor's Name:")
        self.dname=raw_input("Enter Disease Name:")
        self.med=raw_input("Enter Prescribed Medicine:")
        self.bill=input("Enter Bill Amount: Rs.")
        self.paymethod=raw_input("Enter Payment Method(Cash/Cheque/Card):")
 def Output(self):
        print ("PATIENT'S NAME:-"),self.name
        print ("PATIENT'S AGE:-"),self.age
        print ("PATIENT'S SEX:-"),self.sex
        print ("PATIENT'S HEIGHT:-"),self.height
        print ("PATIENT'S WEIGHT:-"),self.weight
        print ("FAVORITE DRINK:-"),self.fdrink
        print ("ADDRESS:-"),self.address
        print ("CITY:-"),self.city
        print ("STATE:-"),self.state
        print ("CONTACT NUMBER:-"),self.pno
        print ("E-MAIL ADDRESS:-"),self.email
        print ("DISEASE NAME:-"),self.dname
        print ("DOCTOR'S NAME:-"),self.doctor
        print ("PRESCRIBED MEDICINES:-"),self.med
        print ("BILL AMOUNT:-"),self.bill
        print ("PAYMENT METHOD:-"),self.paymethod
        

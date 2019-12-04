list_patientID = ["4554", "8861", "9254"]
list_name = [ "Nixon", "English", "Prutzman"]
list_age = ["18", "21", "35"]
list_sex = ["Male", "Female", "Male"]
list_doctor = ["Anand", "Sharon", "Melissa"]
list_med = ["Cholesterol", "Adderall", "Steriod"]
list_allergies = ["Nuts", "Chocolate", "Fish"]
list_fav_drink = ["Coke", "Pwerade", "Sweet Tea"]
list_temp = ["99", "101", "97"]
list_pain_level = ["Excrutiating", "Moderate", "None"]
list_heart_rate = ["50", "75", "85"]
list_blood_pressure = ["120", "140", "100"]
list_blood_type = ["O","A","B"]
def patientquestionaireer():
   


    print(""" 
    ########################################################
    # ====================================================== # 
    # ======== Welcome To Emergency Room Questionaire ======== #
    # ====================================================== #
    ########################################################
    First enter your clearance level
    Enter 1 if you have level one clearance 
    Then: 
    Enter A To search for a patient  
    Enter B To add a new patient record
        
            """)


    clearance_level = input("Please enter your clearance level here: ")
    if clearance_level=="1":
        print("You are allowed to add a patient record or search for a patinet record")
        option_one = input("Enter 'A', or 'B': ")
        if option_one.upper()=="A":
            name_or_ID = input("Enter 'C' if you would like to seach using a last name or 'D' to search with ID number: ")
            if name_or_ID.upper()=="C":
                last_name = input("Enter the last name of the patient: ")
                index = list_name.index(last_name)
                patient_age = list_age[index]
                patient_sex = list_sex[index]
                patient_doctor = list_doctor[index]
                patient_med = list_med[index]
                patient_allergies = list_allergies[index]
                patient_fav_drink = list_fav_drink[index]
                patient_temp = list_temp[index]
                patient_pain_level = list_pain_level[index]
                patient_heart_rate = list_heart_rate[index]
                patient_blood_pressure = list_blood_pressure[index]  
                blood_type = list_blood_type[index]
                patient_id = list_patientID[index]
                print("Age: " , patient_age)
                print("Sex: " , patient_sex)
                print("Doctor: ", patient_doctor)
                print("Medicine: ", patient_med)
                print("Allergies: ", patient_allergies)
                print("Favorite Drink: ", patient_fav_drink)
                print("Temperature: ", patient_temp)
                print("Pain Level: ", patient_pain_level)
                print("Heart Rate: ", patient_heart_rate)
                print("Blood Pressure: ", patient_blood_pressure)
                print("Blood Type: ", blood_type)
                print("Patient ID: ", patient_id)
            elif name_or_ID.upper()=="D":
                patient_id = input("Enter the patinet ID please: ")
                index = list_patientID.index(patient_id)
                last_name = list_name[index]
                patient_age = list_age[index]
                patient_sex = list_sex[index]
                patient_doctor = list_doctor[index]
                patient_med = list_med[index]
                patient_allergies = list_allergies[index]
                patient_fav_drink = list_fav_drink[index]
                patient_temp = list_temp[index]
                patient_pain_level = list_pain_level[index]
                patient_heart_rate = list_heart_rate[index]
                patient_blood_pressure = list_blood_pressure[index]  
                blood_type = list_blood_type[index]
                print("Patient's last name: ", last_name)
                print("Age: ", patient_age)
                print("Sex: ", patient_sex)
                print("Doctor: ", patient_doctor)
                print("Medicine: ", patient_med)
                print("Allergies: ", patient_allergies)
                print("Favorite Drink: ", patient_fav_drink)
                print("Temperature: ", patient_temp)
                print("Pain Level: ", patient_pain_level)
                print("Heart Rate: ", patient_heart_rate)
                print("Blood Pressure: ", patient_blood_pressure)
                print("Blood type: ", blood_type)
            else:
                print("That is an invalid input, please try again")
                pass
            
        elif option_one.upper()=="B":
            print("Enter the new comma separated record like this: 'PatientID,LastName,Age,Sex,Doctor,Medicine,Allergies,FavoriteDrink,Temperature,PainLevel,HeartRate,BloodPressure,Bloodtype,OccupancyTime' ")
            record = input("Enter a new patient record: ")
            list_values = record.split(",")
            list_patientID.append(list_values[0])
            list_name.append(list_values[1])
            list_age.append(list_values[2])
            list_sex.append(list_values[3])
            list_doctor.append(list_values[4])
            list_med.append(list_values[5])
            list_allergies.append(list_values[6])
            list_fav_drink.append(list_values[7])
            list_temp.append(list_values[8])
            list_pain_level.append(list_values[9])
            list_heart_rate.append(list_values[10])
            list_blood_pressure.append(list_values[11])
            list_blood_type.append(list_values[12])
            print(list_patientID)
            print(list_name)
            print(list_age)
            print(list_sex)
            print(list_doctor)
            print(list_med)
            print(list_allergies)
            print(list_fav_drink)
            print(list_temp)
            print(list_pain_level)
            print(list_heart_rate)
            print(list_blood_pressure)
            print(list_blood_type)
        else:
            print("That is an invalid input, please read the instructions and try again ")
            pass
        
    

            
            
            
           
    else:
        pass
    restart = input("Would you like to start again? Type 'yes' or 'no' ").lower()
    if restart=="yes":
        patientquestionaireer()
    else:
        exit()
patientquestionaireer()

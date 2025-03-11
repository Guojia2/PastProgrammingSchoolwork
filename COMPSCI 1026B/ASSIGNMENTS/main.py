from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    #######################
    try:
        f = open(fileName, 'r')  
    except FileNotFoundError:  ##handles the error if the file patients.txt is not found
        print("The file '{}' could not be found.".format(fileName)) #Prints error message
        return patients

    for line in f:  ## goes over every line in the file and turns it into a list
        data = line.strip().split(",")

        if len(data)!= 8: ## checks that the fields for tthe patient are correct. 
            print("Invalid number of fields ({}) in line: {}".format(len(data), line))
            continue # allows the code to continue even if data is in incorrect format

        try: ## converts all fields into the proper datatype
            patientId = int(data[0])
            dateOfVisit = str(data[1])
            bodyTemp= float(data[2])
            heartRate= int(data[3])
            respiratoryRate = int(data[4])
            bloodPressureSystolic = int(data[5])
            bloodPressureDiastolic = int(data[6])
            oxygenSaturation = int(data[7])
        except ValueError: #handles the error, in case a datum can't be converted. For example, a non-digit element being converted into an integer
                    print("Invalid data type in line: {}".format(line))
                    continue


        # checcks all the biometric data and prints an error message if any of them are out of the normal range
        if bodyTemp < 35 or bodyTemp > 42:
            print("Invalid temperature value ({}) in line: {}".format(bodyTemp, line))
            continue
        if heartRate < 30 or heartRate > 180:
            print("Invalid heart rate value ({}) in line: {}".format(heartRate, line))
            continue
        if respiratoryRate < 5 or respiratoryRate > 40:
            print("Invalid respiratory rate value ({}) in line: {}".format(respiratoryRate, line))
            continue
        if bloodPressureSystolic < 70 or bloodPressureSystolic > 200:
            print("Invalid systolic blood pressure value ({}) in line: {}".format(bloodPressureSystolic, line))
            continue
        if bloodPressureDiastolic < 40 or bloodPressureDiastolic > 120:
            print("Invalid diastolic blood pressure value ({}) in line: {}".format(bloodPressureDiastolic, line))
            continue
        if oxygenSaturation < 70 or oxygenSaturation > 100:
            print("Invalid oxygen saturation value ({}) in line: {}".format(oxygenSaturation, line))
            continue
        # makes a new key and vale for the patient if it's a new patient
        if patientId not in patients:
            patients[patientId] = []
        patients[patientId].append([dateOfVisit, bodyTemp, heartRate, respiratoryRate, bloodPressureSystolic, bloodPressureDiastolic, oxygenSaturation])
        ## appends the new visit to any returning patient's record
    f.close()
    return patients

#######################  


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #######################
    if patientId == 0:
        for patientId in patients: ## goes over all the patients in the dicionary
            visits = patients[patientId]  # takes each value tied to the key called patientId and appends them to the list called visits
            print(f"Patient ID: {patientId}")  
            for visit in visits: # for every visit in the list visists, prints all data for the visit
                print(f" Visit Date: {visit[0]}")      
                print("  Temperature:", "%.2f" % visit[1], "C")
                print(f"  Heart Rate: {visit[2]} bpm")
                print(f"  Respiratory Rate: {visit[3]} bpm")
                print(f"  Systolic Blood Pressure: {visit[4]} mmHg")
                print(f"  Diastolic Blood Pressure: {visit[5]} mmHg")
                print(f"  Oxygen Saturation: {visit[6]} %")
    elif patientId in patients: # if the patientId is in the records, print only teh data for that patient
        print(f"Patient ID: {patientId}")
        for visit in patients[patientId]:
                print(f" Visit Date: {visit[0]}")      
                print("  Temperature:", "%.2f" % visit[1], "C")
                print(f"  Heart Rate: {visit[2]} bpm")
                print(f"  Respiratory Rate: {visit[3]} bpm")
                print(f"  Systolic Blood Pressure: {visit[4]} mmHg")
                print(f"  Diastolic Blood Pressure: {visit[5]} mmHg")
                print(f"  Oxygen Saturation: {visit[6]} %")
    elif patientId not in patients: # returns an error message if requested patientId does not match with records
        print(f"Patient with ID {patientId} not found.")

    #######################


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    ####################### 
    if type(patients) != dict: #handles the error if pateints is not a dictioanry
        print("Error: 'patients' should be a dictionary.")
        return
    if patientId.isdigit() == False: # ensures that patientId is entered as an integer
        print("Error: 'patientId' should be an integer.")
        return
    elif patientId.isdigit():
        
        if int(patientId) == 0: ## retrieves the vital signs from all visits and calculates their averages and then prints them
            num_patients = len(patients)
            if num_patients == 0:
                print("No data found.")
                return
            temp_sum = 0    ## initializing variables to be used in the average calculations
            hr_sum= 0
            resp_sum = 0 
            sbp_sum= 0
            dbp_sum= 0
            o2_sum = 0
            num_visits = 0
            for visits in patients.values():
                for visit in visits:      ### counting up the relevant values
                    temp_sum += visit[1]
                    hr_sum += visit[2]
                    resp_sum += visit[3]
                    sbp_sum += visit[4]
                    dbp_sum += visit[5]
                    o2_sum += visit[6]
                    num_visits += 1
            print("Vital Signs for All Patients:")  ## performing the calculations in the same line as the print statements. If these average values had to be reused multiple times, we could consider making a list called "Averages" and then using "Average[i]" to retrieve a specific average vital sign.
            print("  Average temperature:", "%.2f" % (temp_sum / num_visits), "C")
            print("  Average heart rate:", "%.2f" % (hr_sum / num_visits), "bpm")
            print("  Average respiratory rate:", "%.2f" % (resp_sum / num_visits), "bpm")
            print("  Average systolic blood pressure:", "%.2f" % (sbp_sum / num_visits), "mmHg")
            print("  Average diastolic blood pressure:", "%.2f" % (dbp_sum / num_visits), "mmHg")
            print("  Average oxygen saturation:", "%.2f" % (o2_sum / num_visits), "%")
        if int(patientId) in patients:
            ## Takes the average vitals across visits for a specific patient and prints them.
            visits = patients[int(patientId)]
            num_visits = len(visits)
            if num_visits == 0:
                    print("No data found for patient with ID {}.".format(patientId))
                    return
            temp_sum, hr_sum, resp_sum, sbp_sum, dbp_sum, o2_sum = 0, 0, 0, 0, 0, 0
            for visit in visits:
                temp_sum += visit[1]
                hr_sum += visit[2]
                resp_sum += visit[3]
                sbp_sum += visit[4]
                dbp_sum += visit[5]
                o2_sum += visit[6]
            ## printing the relevant infomration:
            print("Vital Signs for Patient {}:".format(patientId))
            print("  Average temperature:", "%.2f" % (temp_sum / num_visits), "C")
            print("  Average heart rate:", "%.2f" % (hr_sum / num_visits), "bpm")
            print("  Average respiratory rate:", "%.2f" % (resp_sum / num_visits), "bpm")
            print("  Average systolic blood pressure:", "%.2f" % (sbp_sum / num_visits), "mmHg")
            print("  Average diastolic blood pressure:", "%.2f" % (dbp_sum / num_visits), "mmHg")
            print("  Average oxygen saturation:", "%.2f" % (o2_sum / num_visits), "%")
            
        elif patientId not in patients:
           print(f"No data found for patient with ID {patientId}.")


    #######################



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    #######################
    

   
        # Ensure the inputted values are valid
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])        
    if len(date) != 10:
        print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
        return 
    if date[4] != '-' or date[7] != '-':
        print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
        return
 
    if year < 1900 or month < 1 or month > 12 or day < 1 or day > 31:
        print("Invalid date. Please enter a valid date.")
        return
    
        
    if not (35.0 <= float(temp) <= 42.0):
        print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        return
    if not (30 <= int(hr) <= 180):
        print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        return
    if not (5 <= int(rr) <= 40):
        print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        return
    if not (70 <= int(sbp) <= 200):
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        return
    if not (40 <= int(dbp) <= 120):
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        return
    


    # once all data has been validated, the following code will be run:
    patientData =  [patientId,date,temp,hr,rr,sbp,dbp,spo2] # creating a list to house patient data
    f = open(fileName, "a")# open the file in append mode, so the cursor will automatically go to the end of the file

    # turns the list into a string and strips off the punctuation to convert the data into a format that the readPatientsFromFile() function can recognize
    patientData = str(patientData).strip(" ").strip("[").strip("]").replace("'","") 
    f.write(patientData) #writes the patient data

    print(f"Visit is saved successfully for Patient {patientId}")     
    f.close()
    
    return
    #######################



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    #######################

    for patientId, patientVisits in patients.items():
        for visit in patientVisits:
            date = visit[0] #identifies the element in the list that corresponds to the date
            if not date:  # ignore visits that don't have a date
                continue
            visitYear, visitMonth, _ = date.split("-") # turns the date into a list of strings
            if year is not None and int(visitYear) != year: # checks the year of visit against the inputted year
                continue
            if month is not None and int(visitMonth) != month:
                continue
            visits.append((patientId, visit)) # as long as none of the "continue" are triggered, the visit will be appended
    ###################
    return visits

def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #######################
    for patientId, data in patients.items():
        for visit in data:
            hr, sbp, dbp, spo2 = visit[2], visit[4], visit[5], visit[6]  #assigns the variables to the indices in the list for readability
            if hr > 100 or hr < 60 or sbp > 140 or dbp > 90 or spo2 < 90: # if any vital signs are out of normal ranges,then append the patient to the followup list
                followup_patients.append(patientId)

    #######################
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #######################
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}.")
        return
    else:
        patients.pop(patientId) ## deletes both the key and value from the dictionary
        print(f"Data for patient {patientId} has been deleted.")
        f =open(filename, 'w') # opens the file in write, thus deleting all data
        for patientId, visits in patients.items():
            for visit in visits:
                line = str(patientId) + ',' + ','.join(str(v) for v in visit) + '\n' # rewrites all data, except for the patient we want to delete
                f.write(line)
        f.close()
    return
    #######################




###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientId = int(input("Enter patient ID: "))
            displayPatientData(patients, patientId)
        elif choice == '3':
            patientId = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            #try:
            temp = float(input("Enter temperature (Celsius): "))
            hr = int(input("Enter heart rate (bpm): "))
            rr = int(input("Enter respiratory rate (breaths per minute): "))
            sbp = int(input("Enter systolic blood pressure (mmHg): "))
            dbp = int(input("Enter diastolic blood pressure (mmHg): "))
            spo2 = int(input("Enter oxygen saturation (%): "))
            addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, 'ASSIGNMENTS/patients.txt')
           # except ValueError:
               # print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientId = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientId)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientId = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientId), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
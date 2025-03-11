## FUNCTION 1:
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
    f = open(fileName, 'r')
    for line in f:
        data = line.strip().split(",")
        
        patientId = int(data[0])
        dateOfVisit = str(data[1])
        bodyTemp= float(data[2])
        heartRate= int(data[3])
        respiratoryRate = int(data[4])
        bloodPressureSystolic = int(data[5])
        bloodPressureDiastolic = int(data[6])
        oxygenSaturation = int(data[7])
        if bodyTemp < 35 or bodyTemp > 42:
            raise ValueError("Invalid temperature value (%f) in line: %s" %(bodyTemp, line))
        if heartRate < 30 or heartRate > 180:
            raise ValueError("Invalid heart rate value (%d) in line: %s"%(heartRate, line))
        if respiratoryRate < 5 or respiratoryRate > 40:
            raise ValueError("Invalid respiratory rate value (%d) in line: %s"%(respiratoryRate, line))
        if bloodPressureSystolic < 70 or bloodPressureSystolic > 200:
            raise ValueError("Invalid systolic blood pressure value (%d) in line: %s "%(bloodPressureSystolic, line))
        if bloodPressureDiastolic < 40 or bloodPressureDiastolic > 120:
            raise ValueError("Invalid diastolic blood pressure value (%d) in line: %s" %(bloodPressureDiastolic, line))
        if oxygenSaturation < 70 or oxygenSaturation > 100:
            raise ValueError("Invalid oxygen saturation value (%d) in line: %s" %(oxygenSaturation, line))
        if patientId not in patients:
            patients[patientId] = []

        patients[patientId].append([dateOfVisit, bodyTemp, heartRate, respiratoryRate, bloodPressureSystolic, bloodPressureDiastolic, oxygenSaturation])
    #######################
    return patients
readPatientsFromFile("ASSIGNMENTS/patients.txt")
###






def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    if patientId == 0:
        # if 0 is entered as the patient id, then the program loops through all patientIds and prints their data
        # patientId is the key and the value is the list of visits for that patient
        for patient_id, visits in patients.items():
            print("Patient ID: %d" % patient_id)
            for visit in visits:
                print("Date of visit: %s" % visit["date"])
                print("Body temperature: %0.1f" % visit["body_temp"])
                print("Heart rate: %d" % visit["heart_rate"])
                print("Respiratory rate: %d" % visit["respiratory_rate"])
                print("Systolic blood pressure: %d" % visit["blood_pressure_systolic"])
                print("Diastolic blood pressure: %d" %visit["blood_pressure_diastolic"])
                print("Oxygen saturation: %d" % visit["oxygen_saturation"])
                print("-------------------------")
    else:
        # prints the 
        if patientId in patients:
            visits = patients[patientId]
            print(f"Patient ID: {patientId}")
            for visit in visits:
                print("Date of visit: %s" % visit["date"])
                print("Body temperature: %0.1f" % visit["body_temp"])
                print("Heart rate: %d" % visit["heart_rate"])
                print("Respiratory rate: %d" % visit["respiratory_rate"])
                print("Systolic blood pressure: %d" % visit["blood_pressure_systolic"])
                print("Diastolic blood pressure: %d" % visit["blood_pressure_diastolic"])
                print("Oxygen saturation: %d" % visit["oxygen_saturation"])
                print("-------------------------")
        else:
            print("No patient found with ID: %s" %(patientId))

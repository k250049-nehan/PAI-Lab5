import csv


def create_file():
    with open("patients.csv","w",newline="") as file:
        writer=csv.writer(file)

        writer.writerow(["ID","Age","BMI","BloodPressure","Glucose","Diabetes"])

        writer.writerow([1,45,28.5,130,180,"Positive"])
        writer.writerow([2,30,24.2,120,110,"Negative"])
        writer.writerow([3,55,31.1,140,200,"Positive"])
        writer.writerow([4,25,22.5,115,95,"Negative"])


def display_records():
    with open("patients.csv","r") as file:
        reader=csv.reader(file)

        for row in reader:
            print(row)


def count_cases():
    positive=0
    negative=0

    with open("patients.csv","r") as file:
        reader=csv.DictReader(file)

        for row in reader:
            if row["Diabetes"]=="Positive":
                positive+=1
            elif row["Diabetes"]=="Negative":
                negative+=1

    print("Positive cases:",positive)
    print("Negative cases:",negative)


def high_glucose(threshold):
    print("\nPatients with high glucose:")

    with open("patients.csv","r") as file:
        reader=csv.DictReader(file)

        for row in reader:
            if float(row["Glucose"])>threshold:
                print(row)


def calculate_average():
    total_bmi=0
    total_glucose=0
    count=0

    with open("patients.csv","r") as file:
        reader=csv.DictReader(file)

        for row in reader:
            total_bmi+=float(row["BMI"])
            total_glucose+=float(row["Glucose"])
            count+=1

    print("Average BMI:",total_bmi/count)
    print("Average Glucose:",total_glucose/count)


def add_record():
    with open("patients.csv","a",newline="") as file:
        writer=csv.writer(file)

        id=input("Enter ID: ")
        age=input("Enter age: ")
        bmi=input("Enter BMI: ")
        bp=input("Enter blood pressure: ")
        glucose=input("Enter glucose level: ")
        diabetes=input("Enter diabetes label: ")

        writer.writerow([id,age,bmi,bp,glucose,diabetes])

    print("Record added.")


def update_record(patient_id):
    with open("patients.csv","r") as file:
        reader=csv.DictReader(file)
        records=list(reader)

    found=False

    for row in records:
        if row["ID"]==patient_id:
            row["Age"]=input("Enter new age: ")
            row["BMI"]=input("Enter new BMI: ")
            row["BloodPressure"]=input("Enter new blood pressure: ")
            row["Glucose"]=input("Enter new glucose: ")
            row["Diabetes"]=input("Enter new diabetes label: ")
            found=True

    if found:
        with open("patients.csv","w",newline="") as file:
            fieldnames=["ID","Age","BMI","BloodPressure","Glucose","Diabetes"]

            writer=csv.DictWriter(file,fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(records)

        print("Record updated.")
    else:
        print("Patient ID does not exist.")


create_file()

display_records()

count_cases()

high_glucose(150)

calculate_average()

add_record()

update_record("2")

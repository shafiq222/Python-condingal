medical_cause=input("Do you have a medical cause Y or N")
attendence=int(input("Enter the attendence record:"))

if medical_cause=="Y":
    print("Acsses granted")
else:
    if attendence >=75:
        print("Acsses granted")
    else:
        print("Acess denied")
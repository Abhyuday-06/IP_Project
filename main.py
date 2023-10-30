from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import re
import time
from random import randint   

flight_details = pd.read_csv(r"D:\Programming\IP_Project\flight_data.csv")
user_details = pd.DataFrame({'S_No':[],'Passenger_Name':[], 'Flight_No':[],'PNR_No':[],'Departure':[],'Arrival':[]})

def main():
    choice = int(input("""
                   Please choose any option from the following using (1,2,3,4,5 and 6 as inputs):

                   1. Live flight status
                   2. Flight booking
                   3. Flight availability
                   4. Cancel flight
                   5. Current schedule of flights
                   6. Your flight info
                   """))
    if choice == 1:
         f_status()
    elif choice == 2:
         f_book(user_data)
    elif choice == 3:
         f_avail()
    elif choice == 4:
         f_cancel(user_data)
    elif choice == 5:
        user_flight(user_data)

    return choice

def f_book(user_data):
    f_no = input("Enter the correct flight no:")
    if f_no in flight_details['Flight_No']:
            print("Seats Available are: ", flight_details[flight_details['Flight_No'] == f_no]['Seats_Available'])
            print("Flight starts from:", flight_details[flight_details['Flight_No'] == f_no]['From'])
            print("Flight's destination is:", flight_details[flight_details['Flight_No'] == f_no]['To'])
            print("It departs at time: ", flight_details[flight_details['Flight_No'] == f_no]['Departure'])
            print("The arrival time is:", flight_details[flight_details['Flight_No'] == f_no]['Arrival'])
            print("The flight will be live for:", flight_details[flight_details['Flight_No'] == f_no]['Duration'])
            print("The number of stops are:", flight_details[flight_details['Flight_No'] == f_no]['Stops'])
            print("Ticket per person:", flight_details[flight_details['Flight_No'] == f_no]['Price'])
        
    else:
        print("Invalid flight number entered. Please try again.")
        return -1
    tickets = int(input("How many seats ticket you want to book?:"))

    print(f"You need to pay {tickets* int(flight_details[flight_details['Flight_No'] == f_no]['Price'].split('.')[1])}")
    c = input("Do you want to confirm the booking?: (y/n)")
    if c == 'y':
        pnr = randint(100000, 999999)
        user_data = pd.concat([user_data, pd.DataFrame([{'PNR': pnr, 'Tickets': tickets }])])
        print(user_data)
        user_data = user_data.to_csv(r'D:\Programming\IP_Project\user_data.csv')
        user_data = pd.read_csv(r'D:\Programming\IP_Project\user_data.csv')
        print("Your ticket has been booked successfully.")

    else:
         print("Thanks for visting. You've been logged out.")




def f_avail():
    location = """Agartala (IXA)
Agra (AGR)
Ahmedabad (AMD)
Aizawl (AJL)    
Amritsar (ATQ)
Aurangabad (IXU)
Bagdogra (IXB)
Bareilly (BEK)
Belagavi (IXG)
Bengaluru (BLR)
Bhopal (BHO)
Bhubaneswar (BBI)
Chandigarh (IXC)
Chennai (MAA)
Coimbatore (CJB)
Darbhanga (DBR)
Dehradun (DED)
Delhi (DEL)
Deoghar (DGH)
Dibrugarh (DIB)
Dimapur (DMU)
Durgapur (RDP) NEW
Gaya (GAY)
Goa (GOI)
Gorakhpur (GOP)
Guwahati (GAU)
Gwalior (GWL)
Hubli (HBX)
Hyderabad (HYD)
Imphal (IMF)
Indore (IDR)
Itanagar (HGI)
Jabalpur (JLR)
Jaipur (JAI)
Jammu (IXJ)
Jodhpur (JDH)
Jorhat (JRH)
Kadapa (CDP)
Kannur (CNN) NEW
Kanpur (KNU)
Kochi (COK)
Kolhapur (KLH)
Kolkata (CCU)
Kozhikode (CCJ)
Kurnool (KJB)
Leh (IXL)
Lucknow (LKO)
Madurai (IXM)
Mangaluru (IXE)
Mumbai (BOM)
Mysuru (MYQ)
Nagpur (NAG)
North Goa (GOX) NEW
Pantnagar (PGH)
Patna (PAT)
Port-Blair (IXZ)
Prayagraj (IXD)
Pune (PNQ)
Raipur (RPR)
Rajahmundry (RJA)
Rajkot (RAJ)
Ranchi (IXR)
Shillong (SHL)
Shirdi (SAG)
Silchar (IXS)
Srinagar (SXR)
Surat (STV)
Thiruvananthapuram (TRV)
Tiruchirappalli (TRZ)
Tirupati (TIR)
Tuticorin (TCR)
Udaipur (UDR)
Vadodara (BDQ)
Varanasi (VNS)
Vijayawada (VGA)
Visakhapatnam (VTZ)

"""
    departure = input(f"{location}\n Choose your departure location from the following(Enter full city name without code):")
    arrival = input(f" {location}\n Choose your arrival location from the following(Enter full city name without code):")
    date = input("Enter the date of your flight in (DD/MM/YYYY) format:")
    day,month,year = date.split('/')
    if len(flight_details[(flight_details['From'] == departure) & (flight_details['To'] == arrival) & (flight_details['Day'] == int(day)) & (flight_details['Month'] == int(month)) & (flight_details['Year'] == int(year))]) == 0:
        print("No flights found. Sorry!")
    elif len(flight_details[(flight_details['From'] == departure) & (flight_details['To'] == arrival) & (flight_details['Day'] == int(day)) & (flight_details['Month'] == int(month)) & (flight_details['Year'] == int(year))]) != 0:
        print(flight_details[(flight_details['From'] == departure) & (flight_details['To'] == arrival) & (flight_details['Day'] == int(day)) & (flight_details['Month'] == int(month)) & (flight_details['Year'] == int(year))])
    else: 
         print("Some error has occurred. Try again later.")
        

def f_cancel(user_data):
    p = int(input("Enter your PNR number:"))
    if p in user_data:
        user_data[user_data['PNR'] == p]['Tickets'] = 0
        user_data = user_data.to_csv(r'D:\Programming\IP_Project\user_data.csv')
        user_data = pd.read_csv(r'D:\Programming\IP_Project\user_data.csv')
        print("Your ticket has been cancelled successfully.")
         

def f_sched():
        now = dt.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        print("Flight schedule for today is as follows:")
        time.sleep(2)
        if flight_details[flight_details["Day"] == day & flight_details["Month"] == month & flight_details["Year"] == year]:
            print(flight_details[flight_details["Day"] == day & flight_details["Month"] == month & flight_details["Year"] == year])
        else:
            print("No flights scheduled for today.")



def user_flight(user_data):
    u = input("Enter your email to confirm:")
    print(user_data[user_data['email'] == u])



def convert24(time):
    t = dt.strptime(time, '%I:%M %p')
    return t.strftime('%H:%M')

def f_status():
    flight_data = pd.read_csv(r'D:\Programming\IP_Project\flight_data.csv')
    
    id = input("Enter Flight ID: ")
    
    extracted_data = flight_data[flight_data['Flight_No']==id]
    
    timeRegex = re.compile('..:.. .m')
    
    imdex = flight_data['Flight_No']==id
    index = 0
    for j in range(0, len(imdex)):    
        if imdex.iat[j]==True:
            index = j
            break
    
    extract = convert24(re.findall(timeRegex, extracted_data.Departure[index])[0].strip())
    depart = dt.strptime(extract, '%H:%M')
    
    extract = convert24(re.findall(timeRegex, extracted_data.Arrival[index])[0].strip())
    arrival = dt.strptime(extract, '%H:%M')
    
    now = dt.strptime(dt.now().strftime("%H:%M"),'%H:%M')
    
    
    status = ''
    statindex = 0
    
    
    if arrival<depart:
        arrival += timedelta(hours=24)
    
    
    if now < depart:
        status = 'Not Yet Started'
    
    elif now > arrival: 
        status = 'FLight Has Landed At Its Destination'
    
    else:
        statindex = (now-depart)/(arrival-depart)
        status = 'Flight In Progress'
    
    
    stops = extracted_data.Stops[index]
    sections = 1/(stops+1)
    
    
    i = 0 
    a1 = list()
    while i <= 1:
        a1.append(i)
        i += sections
    
    
    print(status)
    
    
    plt.plot(a1, [5]*len(a1), marker='o')
    
    
    plt.plot([statindex], [5], marker='X', markeredgecolor='k')
    plt.legend(['Path', 'Current Location'])
    plt.show()

def login(user_data):
    print(user_data)
    username = input("Enter your email address:")
    if username in list(user_data['email']):
        pwd = input("Enter your password:")
        if pwd in list(user_data['password']):
            "Login successful."
            main()
        else: 
            print("Invalid password. Try again later.")
    else: 
        print("The email address entered is incorrect. ")

def signup(user_data):
        name = input("Enter your full name:")
        dob = input("Enter your DOB in the DD/MM/YYYY format:")
        email = input("Enter your email address:")
        password = input("Create a strong password for your account. It must contain at least 8 alphanumeric characters:")
        user_data = pd.concat([user_data, pd.DataFrame([{'name': name, 'dob': dob, 'email': email, 'password': password}])])
        print(user_data)
        user_data = user_data.to_csv(r'D:\Programming\IP_Project\user_data.csv')
        user_data = pd.read_csv(r'D:\Programming\IP_Project\user_data.csv')
        print(user_data)
        print("Account created successfully. You can login now.")
        login(user_data)
        
user_data = pd.read_csv(r"D:\Programming\IP_Project\user_data.csv")
i = int(input("Enter 1 to Login and enter 2 to Sign Up:"))
if i == 1:  
        login(user_data)
        
elif i == 2:
        signup(user_data)
        

        


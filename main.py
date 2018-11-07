'''
Name: Adriano Moreira
Email: adriano.moreira@owl.ucc.edu
Date: Tuesday, November 6, 2018
!Test data!
Required Inputs: Car wash, Car wax, Wiper blades
Expected Outputs: Service 1: Car wash, $7
                  Service 2: Car wax, $12
                  Service 3: Wiper blades, $50
                  Total: $69
'''

service_schedule = {"-": 0, "Oil change" : 35, "Tire rotation" : 19, "Car wash" : 7, "Car wax": 12, "Wiper blades" : 50}
first_service = ""
second_service = ""
third_service = ""
invoice_total = 0

print("Davy's auto shop services") #output statement
print("Oil change -- $35") #output statement
print("Tire rotation -- $19") #output statement
print("Car wash -- $7") #output statement
print("Car wax -- $12") #output statement
print("Wiper blades -- $50") #output statement
print("")

first_service = input("Select first service:") #input statement
print("")
second_service = input("Select second service:") #input statement
print("")
third_service = input("Select third service:") #input statement
print("")

print("Davy's auto shop invoice") #output statement
print("")
#Car Service 1
if(first_service == "-"): #process statement
  print("Service 1: No service") #output statement
else: #process statement
  print("Service 1: %s, $%d" % (first_service, service_schedule.get(first_service))) #process statement and output statement
#Car Service 2  
if(second_service == "-"): #process statement
  print("Service 2: No service") #output statement
else: #process statement
  print("Service 2: %s, $%d" % (second_service, service_schedule.get(second_service))) #process statement and output statement
#Car Service 3
if(third_service == "-"): #process statement
  print("Service 3: No service") #output statement
else: #process statement
  print("Service 3: %s, $%d" % (third_service, service_schedule.get(third_service))) #process statement and output statement  

invoice_total = service_schedule.get(first_service) + service_schedule.get(second_service)+service_schedule.get(third_service) #process statement
print("Total: $%d" % (invoice_total)) #output statement
name = 'Adriano Moreira'
date = 'Tuesday, November 6, 2018'
print('\nProgrammed by %s on %s.' % (name,date))

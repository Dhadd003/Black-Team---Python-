#                                                   ************** week 13 project **************
# 1) import random & string python lib 
# 2) Allow user to input how many EC2 they want names for and output the same amount of unique names
# 3) Allow the user to input the name of their department that is usedd in the unique name
# 4) generate random characters & numbers that will be included in the unique name

import random 
import string

# Ask for amount of ec2
ec2 = int(input("Enter how many EC2 Instances you want: "))
print("EC2 wanted:",ec2)

print()

# Ver. that department is within "job"
department = ['marketing','accounting','finops']
print("List of departments: ")
print(department)
    
print()
dep = input("Please select department you would like from list:")
dep = dep.lower()
    
if dep in department:
    print("Department you selected:",dep)
else:
    print("ERROR. Enter a department from the list.")
        

# Gen a unique name w/ dep name 
randNUM = ['0','1','2','3','4','5','6','7','8','9']
randLett = string.ascii_letters

print()
    
for x in range(ec2):
    newName = random.choice(randNUM) + random.choice(randLett) + random.choice(randNUM) + random.choice(randLett)
    print(dep,"-", newName)
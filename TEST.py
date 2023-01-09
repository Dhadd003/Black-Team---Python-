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
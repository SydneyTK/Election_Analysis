counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1])

#3.2.9 Membership Operators example 
if "El Paso" in counties: 
    print ("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

#3.2.9 combine membership and logical operations- and  
if "Arapahoe" in counties and "El Paso" in counties:
    print ("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")

#3.2.9 combine membership and logical operations- or
if "Arapahoe" in counties or "El Paso" in counties: 
    print("Arapahoe or El Paso is in the list of counties")
else: 
    print("Arapahoe and El Paso are not in the list of counties")

#3.2.9  combine membership and logical operations- and and not
if "Arapahoe" in counties and "El Paso" not in counties: 
    print("Only Arapahoe is in the list of counties")
else:
    print("Araphaoe is in the list of counties and El Paso is not in the list of counties")


#3.2.10 iterating through lists and tuples with for loops 
for county in counties:
    print(county)
    #note this declares the county variable and sets county equal to the first item in the list of counties, aka Arapahoe
    #it will iterate through all the county in counties and print them all 

for i in range(len(counties)):
    print(counties[i])
    #this will acheive the same as the for loop above, it just uses the range function that can simplify for loops. However counties are a string so len is used to turn it to an integer, only numbers can be used by the range function 


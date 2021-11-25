counties_dict= {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

#get the keys of a dictionary 
for county in counties_dict.keys(): 
    print(county)

#get the values of a dictionary 
for voters in counties_dict.values():
    print(voters)

#use the key to get the value 
for county in counties_dict:
    print(counties_dict[county])

#use the get() method to get the values of the keys 
for county in counties_dict: 
    print(counties_dict.get(county))

#find the key value pairs
for county, voters in counties_dict.items():
    print(county, voters)

#iterate through a list of dictionaries 

#this is the list of dictionaries 
voting_data= [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
  
#get each dictionary in the list of dictionaries 
for county_dict in voting_data:
    print(county_dict)

#get the values from a list of dictionaries (need nested for loop)
#first for loop retreives each dictionary 
for county_dict in voting_data: 
    #the second loop uses the values() method on each variable in the dictionary to get the value. remember we could name value voters by using the print(county_dict['registered_voters']) method from above   
    for value in county_dict.values():
        print(value)
#get only the keys or county name 
for county_dict in voting_data:
    print(county_dict['county'])

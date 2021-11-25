#remember we need int below because the input function would give us a string 
my_votes= int(input("How many votes did you get in the election?"))
total_votes= int(input("What is the total number of votes in the election?"))
print(f"I received {my_votes/total_votes * 100}% of the toal votes.")

#below is the old print code, see how it is simplified with the f-string 
# percentage_votes=(my_votes/total_votes)*100
# print("I received" + str(percentage_votes) + "% of the toal votes.")

#f strings with dictionaries 
counties_dict= {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county, voters in counties_dict.items():
    print(f"{county} county had {voters} registered voters.")
    #print(county + " county has " +str(voters)+ " registered voters.")- code without f string 


candidate_votes= int(input("How many votes did the candidate get in the election?"))
total_votes= int(input("What is the total number of votes in the election?"))
Message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f" The total number of votes in the election was {total_votes:,}."
    f" You received {candidate_votes/total_votes*100:.2f}% of the total votes."
    #spaces are needed infront of last 2 f strings so there is proper spacing in output 
)
print(Message_to_candidate)

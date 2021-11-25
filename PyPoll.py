#3.3.3 Pseudocoding- the data we need to retrieve
# 1) the total number of votes cast 
# 2) a complete list of candidates who received votes 
# 3) the percentage of votes each candidate won 
# 4) the total number of votes each candidare won 
# 5) the winner of the election based on popular vote 

# 3.4.2 Opening the csv- below shows an indirect path, or as if we didnt know the folder path
#below are called dependencies 
import csv
import os
# assign a variable to load a file from a path 
file_to_load = os.path.join("Reasources", "election_results.csv")
#assign a variable to save the file to a path 
file_to_save= os.path.join("analysis", "election_analysis.txt")

#1. initialize the total vote counter 
total_votes=0

#3.5.2 declaring a new candidate list to hold the name of each candidate 
candidate_options=[]
#3.5.3 creating an empty dictionary to hold the number of votes per candidate 
candidate_votes={}

#3.5.5 winning candidate and winning count tracker 
winning_candidate= ""
winning_count= 0
winning_percentage=0

# open the election results and read the file  
with open(file_to_load) as election_data:

    #read the file object with the reader function 
    file_reader = csv.reader(election_data)

    #print the header row- this will ensure the next() function below is skipping them 
    headers=next(file_reader)
           
    #print each row in the CSV file 
    for row in file_reader:
        #2. add to the total vote count 
        total_votes +=1
        #3.5.2 print the candidate name from each row
        candidate_name=row[2]
        #if the candidate does not match any existing candidate (the line of code below checks)
        if candidate_name not in candidate_options:
            #then add them to the candidate_options list 
            candidate_options.append(candidate_name)

            #3.5.3 begin tracking that candidate's vote count 
            candidate_votes[candidate_name]= 0
        #increment votes by one every time it appears in a row 
        candidate_votes[candidate_name]+=1

#3.6.1 using the with statement open the file as a text file 
with open (file_to_save, "w") as txt_file: 
#print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n"
        )
    print(election_results, end="")
    #save the final vote count to the text file 
    txt_file.write(election_results)

    #3.5.4 determine the percentage of votes for each candidate by looping through the counts 
    #iterate through the candidates list- remember candidate_votes is dictionary  
    for candidate_name in candidate_votes:
        #retrieve vote count of the candidate 
        votes= candidate_votes[candidate_name]
        #calculate the percentage of votes 
        vote_percentage= float(votes)/float(total_votes)*100
        #print the candidate name and percentage of votes 
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        #to do: print out each canidate's name, vote, count, and percentage of votes to the terninal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")- commented out and altered below to a variable so we can print the variable in the text file  
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print rach candidate, thier voter count and percentage to the terminal 
        print(candidate_results)
        #save the candidate results to our text file 
        txt_file.write(candidate_results)

        #3.5.5 determine winning vote count and candidate
        #determine if the votes are greater than the winning count 
        if (votes>winning_count) and (vote_percentage>winning_percentage):
        #if true then set the winning_count = votes and winning_percent=vote_percentage 
            winning_count=votes
            winning_percentage= vote_percentage
            #and, set the winning_candidate equal to the candidate's name 
            winning_candidate= candidate_name

    #below will print the winning candidate summary 
    winning_candidate_summary =(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"--------------------------\n"
        )
    #save the wunnung candidate's name to the text file 
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary) 
                            
                



    




<<<<<<< HEAD
import os
import csv

election_data_csv = os.path.join("C:\MAICA\MONASH\Python\python-challenge\PyPoll\Resources", "election_data.csv")


vote_total = 0
candidate_list = []
candidate_vote = {}
winner = ""
winning_count = 0


with open(election_data_csv) as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")

    
    for row in csvreader:
        #total count
        vote_total = vote_total + 1
        candidate_name = row[2]

#check if candidate exist in the candidate list
        if candidate_name not in candidate_list:
            #add it to the candidate list
            candidate_list.append(candidate_name)
            # tracking candidate's vote count

            candidate_vote[candidate_name] = 0
        # add vote to each candidate vote
        candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1

#print output

election_result = os.path.join("C:\\MAICA\MONASH\\Python\python-challenge\\PyPoll\\analysis", "election_data.text")

with open(election_result, "w") as txt_file:
    #Print final count

    election_result = (
        f"Election Result\n"
        f"----------------------\n"
        f"Total Votes: {vote_total}\n"
        f"------------------------\n"

    )
    print(election_result)

    txt_file.write(election_result)

#find winner
    for candidate in candidate_vote:
        vote = candidate_vote.get(candidate)
        vote_percentage = float(vote) / float(vote_total) *100

        if (vote > winning_count):
            winning_count = vote
            winning_candidate = candidate
        voter_output = f'{candidate}: {vote_percentage: .3f}% ({vote})\n'
        print(voter_output)
        #save vote count and percentage to text file
        txt_file.write(voter_output)

#Print winning candidate

    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------------------\n"
    )

    print(winning_candidate_summary)

    #save the file
    txt_file.write(winning_candidate_summary)

        
    


   
=======
import os
import csv

election_data_csv = os.path.join("C:\MAICA\MONASH\Python\python-challenge\PyPoll\Resources", "election_data.csv")


vote_total = 0
candidate_list = []
candidate_vote = {}
winner = ""
winning_count = 0


with open(election_data_csv) as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")

    
    for row in csvreader:
        #total count
        vote_total = vote_total + 1
        candidate_name = row[2]

#check if candidate exist in the candidate list
        if candidate_name not in candidate_list:
            #add it to the candidate list
            candidate_list.append(candidate_name)
            # tracking candidate's vote count

            candidate_vote[candidate_name] = 0
        # add vote to each candidate vote
        candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1

#print output

election_result = os.path.join("C:\\MAICA\MONASH\\Python\python-challenge\\PyPoll\\analysis", "election_data.text")

with open(election_result, "w") as txt_file:
    #Print final count

    election_result = (
        f"Election Result\n"
        f"----------------------\n"
        f"Total Votes: {vote_total}\n"
        f"------------------------\n"

    )
    print(election_result)

    txt_file.write(election_result)

#find winner
    for candidate in candidate_vote:
        vote = candidate_vote.get(candidate)
        vote_percentage = float(vote) / float(vote_total) *100

        if (vote > winning_count):
            winning_count = vote
            winning_candidate = candidate
        voter_output = f'{candidate}: {vote_percentage: .3f}% ({vote})\n'
        print(voter_output)
        #save vote count and percentage to text file
        txt_file.write(voter_output)

#Print winning candidate

    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------------------\n"
    )

    print(winning_candidate_summary)

    #save the file
    txt_file.write(winning_candidate_summary)

        
    


   
>>>>>>> 16cefa0361fdc1efdbbfa4c4a19743b570eb55b1
    
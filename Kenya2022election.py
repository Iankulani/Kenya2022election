# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 03:33:04 2024

@author: IAN CARTER KULANI
"""
# -*- coding: utf-8 -*-
#This software prompts the user to enter total number of published centers,total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward, it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.

print("====================================KENYA 2022 ELECTION====================================\n") 

Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get total valid votes for Ruto William Samoei.
Totalvalidvotesfor_rutowilliamsamoei=int(input("Enter Total valid Votes for Ruto William Samoei:"))
#Get total valid votes for Odinga Raila
Totalvalidvotesfor_odingaraila=int(input("Enter Total Valid Votes for Odinga Raila:"))
#Get total valid votes for Wajack Oyah George Luchi.
Totalvalidvotesfor_wajackoyahgeorgeluchi=int(input("Enter Total Valid Votes for Wajack Oyah George Luchi:"))
#Get total valid votes for Wahiga David
Totalvalidvotesfor_waihigadavid=int(input("Enter Total Valid Votes for Wahiga David:"))
percent=100


if Totalvalidvotesfor_rutowilliamsamoei>Totalvalidvotes/2+1:
   print("Cogratulations Ruto William Samoei you're the winner of 2020 election\n\n")
 
elif Totalvalidvotesfor_odingaraila>Totalvalidvotes/2+1:
     print("Cogratulations Odinga Raila you're the winner of 2020 election\n\n")
   
elif Totalvalidvotesfor_wajackoyahgeorgeluchi>Totalvalidvotes/2+1:
     print("Cogratulations Wajack Oyah George Luchi you're the winner of 2020 elections")
    
elif Totalvalidvotesfor_waihigadavid>Totalvalidvotes/2+1:
     print("Cogratulations Wahiga David you're the winner of 2020 election\n\n")


else:
    print("No majority winner was found RUN OFF May be required\n\n")     

print("_________________________________ELECTION STATISTICS_____________________________________\n") 
   
#Calculating Percentage    

Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)

Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)

#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#

Percentage=round(Totalvalidvotesfor_rutowilliamsamoei*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Ruto William Samoei in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_odingaraila*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Odinga Raila in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_wajackoyahgeorgeluchi*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Wajack Oyah George Luchi in percentage=",Percentage )

Percentage=round(Totalvalidvotesfor_waihigadavid*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Wahiga David in percentage=",Percentage )


print("==========================================================================================\n") 

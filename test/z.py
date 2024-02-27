f = open("leaderboard.txt","r")
lines =f.readlines()
lead = {}
i = 0
for line in lines :
     line = line.strip("\n")
     player = line.split(",")
     i = i + 1 
     lead[i]=player
     
f.close()
for i in lead :
     print(lead[i]) 


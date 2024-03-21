
     
def classe()     :

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
     classement = []
     point = []
     for i in lead :
          point.append(lead[i][0])
     point.sort(reverse=True)
     for i in point :
          for x in lead :
               if i == lead[x][0] and lead[x][1] not in classement:
                    classement.append("{0} {1}".format(lead[x][1],lead[x][0]))

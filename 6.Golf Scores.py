#Add total and average for the club using function concepts
#print the total and average for the club

def main():
    Num_players = int(input('Input the number of players: '))
    outfile = open('golf.txt', 'w')

    for n in range(Num_players):
        Player = input('Input player name: ')
        Score = int(input('Input their score: '))

        outfile.write(Player + '\n')
        outfile.write(str(Score) + '\n')
        
def readavg():
    def total_average(total,number):
        return(total)/number
    infile = open('golf.txt', 'r')
    Player = infile.readline()

    Num_players = 0
    Total= 0
    

    while Player != '':
        Player = Player.rstrip('\n')
        Score = int(infile.readline())

        Total += Score
        Num_players +=1
        
        print ('Player: ',Player)
        print ('Scored: ',Score)

        Player = infile.readline()

    
    infile.close()
    print ('Golf Club: Total Score // Average Score: ', Total,'//', total_average(Total, Num_players))

main()
readavg()





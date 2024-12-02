#This is a small python script that opens a text file reads the contents
#splits the contents, counts the value of the contents (how big the number is)
#and how many numbers there are, stores it in variables and displays the total
#of all the numbers added, how many there are and the average. An example
#invocation would be python3 sumLines.py <some text doc>

import sys
file = (sys.argv[1]) #initializing the file as the first command line arg
total_sum = 0 #initializing total sum 
total_count = 0 #initializing total count
with open(file, 'r') as file: #opening the command line arg with the param 'r'
#specify read the 'file' once opened
  for line in file: 
    numbers = line.split() #split all the lines within the file and store in
    #numbers
    for num in numbers:
      total_sum += int(num)# adding every split number value and storing in
      #total sum
      total_count += 1 #Adding 1 for every value split so we can take an average

average = total_sum/ total_count #taking the average

print(f"Total sum: {total_sum}\nTotal count: {total_count}\nAverage: {average}")







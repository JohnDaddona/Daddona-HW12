#This is a small python script that opens 2 text files reads the contents
#splits the contents, reverses them so they make sense, concatenates them
#and store the output in output.txt0. 
#An example invocation would be python3 reconstructSentence.py <text doc1 text doc1>

import sys
with open(sys.argv[1], "r") as file1: #initializing first text doc (first command line arg) and calling it file 1
  list1 = file1.read().split() #reading and storing contents of file 1 in list 1

with open(sys.argv[2], "r") as file2:#initializing first text doc (second command line arg) and calling it file 2
  list2 = file2.read().split() #reading and storing contents of file 2 in list 2

list1 = list1[::-1] #reversing the order of the contents of list 1
list2 = list2[::-1] #reversing the order of the contents of list 2

out = [] #creating an empty output list.


#for loop to check the size of the list and as long as theres
#still contents within the list whilst parsing, append
#the output list.
for i in range(max(len(list1), len(list2))):
  if i < len(list1):
    out.append(list1[i])
  if i < len(list2):
    out.append(list2[i])

#now open the output document (file 3) and saying
#write the words in the 'out' list into the output.txt file 
with open("output.txt", "w") as file3:
  for word in out:
    file3.write(word + " ")

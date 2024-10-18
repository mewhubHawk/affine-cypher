from random import randint

#list of letters A is 0 and so forth
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#index = 0

#list of significant words to the cypher challenge, other common english words will be imported
words = [
  "babbage",
  "charles",
  "ada",
  "lovelace",
  "kate",
  "warne",
  "bullet"
]

#cypher = input("Enter what you'd like to be decyphered: ")

#print the letter corresponding to the number in square bracket
print(alphabet[0])

#print all of the letters the list by referring to their number
for index in range(26):
  print(alphabet[index])

#practice the modular arithmetic code
for index in range(26):
  randindex=randint(0,51)
  if randindex > 25: 
    randindex=- 26
#25 and 51 because a is 0
#"=-x" because its a variabele that needs to be assigned =

 #print all the letters ,like earlier, print a random letter besides it 
  print(alphabet[index],
     alphabet[randindex]
     )






'''
index = randint
if letter > 25 
   letter=- 26

each letter refers to a number

if letter > 26 
   letter - 26
'''

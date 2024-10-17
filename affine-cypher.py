from random import randint

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#index = 0
words = [
  "babbage",
  "charles",
  "ada",
  "lovelace",
  "kate",
  "warne",
  "bullet"
]

print(alphabet[0])

for index in range(26):
  print(alphabet[index])

for index in range(26):
  randindex=randint(0,51)
  if randindex > 25: 
    randindex=- 26
  
  print(alphabet[index],
     alphabet[randindex]
     )




index = randint
if letter > 26 
   letter - 26

'''
cypher = input("Enter what you'd like to be decyphered: ")

each letter refers to a number

if letter > 26 
   letter - 26
'''

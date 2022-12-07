import random

options = ['ROCK', 'PAPER', 'SCISSOR']

print("Pick from ROCK, PAPER, SCISSOR")
user = input("Enter your choice ").upper()

comp = random.choice(options)

print()
print("Your choice : " + user)
print("Computer's choice : " + comp)
print()

if user == comp:
  print("TIE!!!")
elif user == 'ROCK' and comp == 'PAPER':
  print("COMPUTER WIN!!!")
elif user == 'ROCK' and comp == 'SCISSOR':
  print("YOU WIN!!!")
elif user == 'PAPER' and comp == 'ROCK':
  print("YOU WIN!!!")
elif user == 'PAPER' and comp == 'SCISSOR':
  print("COMPUTER WIN!!!")
elif user == 'SCISSOR' and comp == 'PAPER':
  print("YOU WIN!!!")
elif user == 'SCISSOR' and comp == 'ROCK':
  print("COMPUTER WIN!!!")
else:
  print("Invalid input")
  


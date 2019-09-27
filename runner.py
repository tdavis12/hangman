import random
import os
import array as arr
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def split(word):
  return [char for char in word]

def pickWord(length):
  file = "words/word_" + str(length) + ".txt"
  file = os.path.join(THIS_FOLDER, file)
  f=open(file, "r")
  if f.mode == 'r':
    select = random.randint(0,100)
    lines=f.readlines()
    return lines[select]

def hangman(prog):
  print(" _________     ")
  print("|         |    ")
  
  if prog > 0:
    print("|         0    ")
  else:
    print("|              ")

  if prog < 2:
    print("|             ")
  elif prog == 2:
    print("|         |   ")
  elif prog == 3:
    print("|        /|   ")
  else:
    print("|        /|\\  ")

  if prog < 5:
    print("|             ")
  elif prog == 5:
    print("|        /    ")
  else:
    print("|        / \\  ")

  print("|              ")
  print("|      -------\n")

print("Welcome to Hangman!")
hangman(6)
length = 0
while length < 5 or length > 10:
  print("Select your difficulty (5-10): ")
  length = input()

print("You have selected a difficutly of {0}. Good Luck!" .format(length))

word = pickWord(length)
sWord = split(word)
print(sWord)

i = 0
display = ""
while i < length:
  display += "_ "
  i += 1
display += "\n"
lDisplay = list(display)

correctCount = 0
progress = 0
while progress < 7:

  hangman(progress)
  print("".join(lDisplay))

  flag = 0
  while flag == 0:
    print("Enter a letter: ")
    letter = str(raw_input())
    if len(letter) == 1:
      flag = 1

  letter = letter.lower()

  correct = 0
  count = 0
  while count < length + 1:
    if letter == sWord[count]:
      print("Correct!")
      lDisplay[count * 2] = letter
      correct = 1
      correctCount += 1
    count += 1

  if correct == 0:
    print("Wrong!")
    progress += 1

  if correctCount == length:
    print("Congratulations! You win!")
    break

if correctCount != length:

  print(" _________     ")
  print("|         |    ")
  print("|         X    ")
  print("|        /|\\  ")
  print("|        / \\  ")
  print("|              ")
  print("|      -------\n")
  print("".join(lDisplay))
  print("The right answer was: " + word)
  print("You lose! Try again!")
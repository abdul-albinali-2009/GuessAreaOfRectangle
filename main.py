#welcome statement
print("Welcome to the Guessing Area Game!")
#gets user length
length = float(input("What is the length of the rectangle? "))
#gets user width
width = float(input("What is the width of the rectangle? "))
#gets user area
userArea = float(input("Guess the Area for the rectangle! "))
#computer calcs area
computerArea = length * width
#boolean expression for the guess
if userArea == computerArea:
  print("You got it right! Good Job It was", computerArea)
else:
  print("You got it wrong, the area was", computerArea)

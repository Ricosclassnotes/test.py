import random

high = 100
low = 1
answer = random.randint(low, high)
attempts = 0
is_running = True
print("🎲Welcome to python guessing game🕹️")

while is_running:

  attempt = input("Enter your guess")

  if attempt.isdigit():
    attempt = int(attempt)
    attempts +=1

    if attempt < low or attempt > high:
      print("Out of Range, try again")
    elif attempt < answer:
      print("Number is too low")
    elif attempt > answer:
      print("Number is too high")
    else:
      print(f"Correct: Answer was {answer}")
      print(f"Attempts = {attempts}")
      is_running = False
    
  else:
    print("Invalid Answer: Enter a number")






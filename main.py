"""
Chatbot
Author: Cole Markulis
Period/Core: 7

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")

  name = input("What's your name? ")
  print("Nice to meet you " + name)

  feel = input("How are you feeling today? ")
  if (feel == "happy"):
    print("Thats good to hear! ")
  elif (feel == "sad"):
    print("I'm sorry you feel that way ")
  
  color = input("Whats your favorite color? ")
  
  n = random.randint(1,2)
  print(n)

  if (n == 1):
    print("Thats my favorite too! ")
  else:
    print("That's not my favorite")
  
  food = input("What's your favorite food? ")
  if (food == "pizza"):
    print("Yummy")
  elif (food == "grapes"):
    print("that sounds nice! ")
  else:
    print("That food isn't really my favorite")
  
  fun = input("Did you have fun? ")
  if (fun == "Yes"):
    print("Great")
  elif (fun == "No"):
    print("I'm sorry")
  print("Have a good day! " + name)
  print("I hope you had fun")





if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()


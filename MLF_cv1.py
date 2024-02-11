# # EX1.1 pyramida
# string = ''
# print(len(string))
# for i in range(9):
#     if i < 5: 
#         string = (len(string)+1) * 'X'
#        # string = string + 'X'
#     else:
#         string = (len(string)-1) * 'X'
#     print(string)
###################################################################################################################################################################
# ##EX1.2 sum of nums in string
# input_str = "n45as29@#8ss6"
# vysledek = 0

# for i in input_str:
#     if i.isnumeric():
#         # print(i)
#         vysledek =  vysledek + int(i)

# print(vysledek)
###################################################################################################################################################################
# ##EX 1.3 bin()
# dec_num = 1111
# bin_num = ''
# i = 0

# print('vysledek funkce')
# print(bin(dec_num))

# while dec_num > 1:
#     bin_num = str(dec_num % 2) + bin_num
#     dec_num = dec_num//2
#     i = i+1

# bin_num = '0b1' + bin_num
# print('vysledek')
# print(bin_num)
###################################################################################################################################################################
# ##EX 1.4 smaller than fibonacci
# def fibonacci(upper_threshold: int) -> list:
#     fibonacci_sequence = [0, 1]
#     while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= upper_threshold:
#         fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
#     return fibonacci_sequence

# print(fibonacci(20))
###################################################################################################################################################################
# ##EX 1.5 ROCK PAPER LESBIANS
# import random

# def RPS():
#     #print(random.randint(1, 3))
#     options = ["rock", "paper", "scissors"]
#     selected = options[random.randint(0, 2)]
#     print("Im epty, fill me daddy")
#     user_in = input()
#     user_in = user_in.lower()

#     match user_in:
#         case "rock":
#             match selected:
#                 case "rock":
#                     outcome = "its a tie"
#                 case "paper":
#                     outcome = "you lose"
#                 case "scissors":
#                     outcome = "you win"

#         case "paper":
#             match selected:
#                 case "rock":
#                     outcome = "you win"
#                 case "paper":
#                     outcome = "its a tie"
#                 case "scissors":
#                     outcome = "you lose"

#         case "scissors":
#             match selected:
#                 case "rock":
#                     outcome = "you lose"
#                 case "paper":
#                     outcome = "its win"
#                 case "scissors":
#                     outcome = "its a tie"

#         case _:
#             outcome = "napsal jsi to spatne troubo"

#     return(outcome)

# print(RPS())
###################################################################################################################################################################
##EX2.2 digi disply
import matplotlib.pyplot as plt
import numpy as np

numbs = {
      "1": np.array([[0, 1, 1], [1, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]), # 1
      "2": np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]]), # 2
      "3": np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 3
      "4": np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]), # 4
      "5": np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 5
      "6": np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]), # 6
      "7": np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]), # 7
      "8": np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]), # 8
      "9": np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 9
      "0": np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]), # 0
      "|": np.array([[0], [0], [0], [0], [0]]),                               # mezera
      ".": np.array([[0], [0], [0], [0], [1]]),                               # tecka
      "-": np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]]), #zapor
  }

def show_in_digi(input_integer):
  final_digit = np.array([[], [], [], [], []])
  for i in str(input_integer):
      digit = numbs.get(i)
      final_digit = np.concatenate((final_digit, digit, numbs["|"]), axis = 1)
  plt.imshow(final_digit)
  plt.show()

show_in_digi(-235.53)
###################################################################################################################################################################
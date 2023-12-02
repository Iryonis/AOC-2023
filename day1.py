# Question 1 :
# import re

# fichier = open("input1.txt", "r")
# lines = fichier.readlines()
# total_sum = 0

# for t in range(len(lines)):
#     if lines[t] != "\n":
#         num = [int(match) for match in re.findall(r"\d", lines[t])]
#         total_sum += int(f"{num[0]}{num[-1]}")
#         print(f"{total_sum}")

# fichier.close()

# Question 2 :

from word2number import w2n
import re

fichier = open("input1.txt", "r")
lines = fichier.readlines()
total_sum = 0

for t in range(len(lines)):
    if lines[t] != "\n":
        num_string = re.findall(
            rf"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", lines[t]
        )
        print(num_string)
        num_int = [w2n.word_to_num(num_string[0]), w2n.word_to_num(num_string[-1])]
        print(num_int, num_int[0], num_int[-1])
        total_sum += int(f"{num_int[0]}{num_int[-1]}")
        print(f"{total_sum}")

fichier.close()

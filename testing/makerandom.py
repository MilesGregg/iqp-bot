import random
import math

for i in range(55):
    print("\"test " + str(i+1) + "\":")
    print("[")
    for j in range(15):
        time = round(random.uniform(2, 4), 2)
        bot_dir = "right" if j % 2 == 0 else "left"

        print("\t\"" + str(bot_dir) + "-" + str(time) + "\"" + ("," if j != 14 else ""))
    if i != 54:
        print("],")
    else:
        print("]")

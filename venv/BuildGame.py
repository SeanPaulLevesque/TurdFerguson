import os
import random

oldest = 9999
newest = 0
#find range of episodes
for file in os.listdir("./episodes"):
    if file.startswith("ID"):
        id = int(file[2:6])
        if (oldest > id): oldest = id
        if (newest < id): newest = id

#pick a random episode
episodes = []
while len(episodes) < 6:
    num = random.randint(oldest, newest)
    if num not in episodes:
        episodes.append(num)

#pick a random category
categories = []
while len(categories) < 6:
    num = random.randint(1, 6)
    categories.append(num)

#pick a random round
round = []
round_type = ["J", "D"]
while len(round) < 6:
    num = random.randint(0, 1)
    round.append(round_type[num])

fj_file_name = "ID" + str(episodes[0]) + "_finalj.txt"
os.rename("./categories/" + fj_file_name, "./Jeopardy_Maker_PC/questions/finalj.txt")

with open("./Jeopardy_Maker_PC/questions/categories.txt", "w") as cout:

    for num in range(len(episodes)):

        q_file_name = "ID" + str(episodes[num]) + round[num] + "_category" + str(categories[num]) + "-questions.txt"
        a_file_name = "ID" + str(episodes[num]) + round[num] + "_category" + str(categories[num]) + "-answers.txt"

        os.rename("./categories/" + q_file_name,"./Jeopardy_Maker_PC/questions/column" + str(num+1) + "-questions.txt")
        os.rename("./categories/" + a_file_name, "./Jeopardy_Maker_PC/questions/column" + str(num+1) + "-answers.txt")


        with open("./Jeopardy_Maker_PC/questions/column" + str(num + 1) + "-questions.txt", "r") as fin:
            data = fin.read().splitlines(True)
            fin.close()
        with open("./Jeopardy_Maker_PC/questions/column" + str(num + 1) + "-questions.txt", "w") as fout:
            fout.writelines(data[1:])
            fout.close()
        with open("./Jeopardy_Maker_PC/questions/column" + str(num + 1) + "-answers.txt", "r") as fin:
            data = fin.read().splitlines(True)
            fin.close()
        with open("./Jeopardy_Maker_PC/questions/column" + str(num + 1) + "-answers.txt", "w") as fout:
            fout.writelines(data[1:])
            fout.close()

            cout.write(data[0])



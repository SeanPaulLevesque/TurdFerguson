import json
import jsonpickle
import os

for file in os.listdir("./episodes"):
    if file.startswith("ID"):
        with open("./episodes/" + file) as json_file:
            print(file)
            data = json.load(json_file)
            game = jsonpickle.decode(data)

            with open("./categories/" + file.split('.')[0] + '_finalj.txt', 'w+') as f:
                f.write(game.f.question + '\n')
                f.write(game.f.answer + '\n')

            for cat_num, cat_val in game.j.__dict__.items():
                skip = False
                #if a category was never finished then skip it
                for clue_num, clue_val in cat_val.__dict__.items():
                    if (type(clue_val) != str):
                        if (clue_val.question == ''):
                            skip = True

                if skip == False:
                    with open("./categories/" + file.split('.')[0] + 'J_' + str(cat_num) + '-questions.txt', 'w+') as q:
                        q.write(cat_val.cat_name + '\n')
                        with open("./categories/" + file.split('.')[0] + 'J_' + str(cat_num) + '-answers.txt', 'w+') as a:
                            a.write(cat_val.cat_name + '\n')
                            for clue_num, clue_val in cat_val.__dict__.items():
                                if (type(clue_val) != str):
                                    q.write(clue_val.question + '\n')
                                    a.write(clue_val.answer + '\n')

            for cat_num, cat_val in game.d.__dict__.items():
                skip = False
                #if a category was never finished then skip it
                for clue_num, clue_val in cat_val.__dict__.items():
                    if (type(clue_val) != str):
                        if (clue_val.question == ''):
                            skip = True

                if skip == False:
                    with open("./categories/" + file.split('.')[0] + 'D_' + str(cat_num) + '-questions.txt', 'w+') as q:
                        q.write(cat_val.cat_name + '\n')
                        with open("./categories/" + file.split('.')[0] + 'D_' + str(cat_num) + '-answers.txt', 'w+') as a:
                            a.write(cat_val.cat_name + '\n')
                            for clue_num, clue_val in cat_val.__dict__.items():
                                if (type(clue_val) != str):
                                    q.write(clue_val.question + '\n')
                                    a.write(clue_val.answer + '\n')



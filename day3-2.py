with open('day_03.txt ', 'r') as file_object:
    input_text = file_object.read()

    santa_x=0
    santa_y=0
    robo_x = 0
    robo_y = 0
    house={(0,0):True}

    for i, go in enumerate(input_text):
        if i%2==0:
            if go == '^':
                robo_y = robo_y + 1
            elif go == 'v':
                robo_y = robo_y - 1
            elif go == '>':
                robo_x = robo_x + 1
            elif go == '<':
                robo_x = robo_x - 1
            house[(robo_x, robo_y)]= True

        else:
            if go == '^':
                santa_y = santa_y + 1
            elif go == 'v':
                santa_y = santa_y - 1
            elif go == '>':
                santa_x = santa_x + 1
            elif go == '<':
                santa_x = santa_x - 1
            house [(santa_x, santa_y)]=True

answer=len(house)
print(answer)


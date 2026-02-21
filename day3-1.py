from multiprocessing.connection import answer_challenge

with open('day_03.txt ', 'r') as file_object:
    input_text = file_object.read()

    x=0
    y=0
    house=set()
    house.add((x, y))

    for go in input_text:
        if go == '^':
            y=y+1
        elif go == 'v':
            y=y-1
        elif go == '>':
            x=x+1
        elif go == '<':
            x=x-1

        house.add((x,y))

answer=len(house)

print(answer)


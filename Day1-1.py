with open('day_01.txt ', 'r') as file_object:
    input_text = file_object.read()

up=input_text.count('(')
down=input_text.count(')')

answer=up-down

print(answer)
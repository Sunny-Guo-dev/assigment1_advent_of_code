with open('day_01.txt ', 'r') as file_object:
    input_text = file_object.read()

floor = 0
for i, character in enumerate(input_text, start=1):
    if character == '(':
        floor = floor + 1
    else:
        floor = floor - 1

    if floor == -1:
        print(i)

        break
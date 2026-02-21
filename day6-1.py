with open('day_06.txt ', 'r') as file_object:
    input_text = file_object.read()

    import pandas as pd

    import numpy as np
    garden = np.zeros((1000, 1000))
    # Gemini 3
    # Prompt: "In Python, I want to create a 1000x1000 table with 0 in each cell, and I will use pandas to manipulate it later. How should I write code?"
    garden_df = pd.DataFrame(garden)

    santa = input_text.splitlines()
    for row in santa :
        move = row.split(' ')

        start = move[-3].split(',')
        end = move[-1].split(',')

        x1=int(start[0])
        y1=int(start[1])
        x2=int(end[0])
        y2=int(end[1])

        area = garden_df.loc[x1:x2, y1:y2]
        if "on" in row:
            garden_df.loc[x1:x2, y1:y2] = 1

        elif "off" in row:
            garden_df.loc[x1:x2, y1:y2] = 0

        elif "toggle" in row:
            garden_df.loc[x1:x2, y1:y2] = area.replace({1: 0, 0: 1})

    answer=garden_df.sum().sum()
    # Gemini 3. Add the second ".sum()" and correct indentation error
    # Prompt: "This is my code, why my answer seems wrong?"

    print(answer)
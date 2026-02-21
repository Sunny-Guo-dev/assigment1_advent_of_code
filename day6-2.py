with open('day_06.txt ', 'r') as file_object:
    input_text = file_object.read()

    import pandas as pd
    import numpy as np
    garden = np.zeros((1000, 1000))
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

        if "on" in row:
            garden_df.loc[x1:x2, y1:y2] = garden_df.loc[x1:x2, y1:y2]+1

        elif "off" in row:
            garden_df.loc[x1:x2, y1:y2] = (garden_df.loc[x1:x2, y1:y2] - 1).clip(lower=0)
            # Gemini 3
            # Prompt: "I want to ensure that “it stays 0 after -1 and doesn't become negative” at this step. How should I write the code?"

        elif "toggle" in row:
            garden_df.loc[x1:x2, y1:y2] = garden_df.loc[x1:x2, y1:y2]+2

    answer=garden_df.sum().sum()

    print(answer)
#! /usr/bin/env python3

import numpy as np

N = 3

examples = np.array([
          [1, 1, 0.3]
        , [1, 0.4, 0.5]
        , [1, 0.7, 0.8]
        ])

targets = [1,1,0]

ws = np.array([0,0,0])

def predict(e):
    return (sum(e * ws.T) > 0)


perfect = False
# while (not perfect):
    # perfect = True
for i in range(N):
    predicted = predict(examples[i])
    target = targets[i]
    if (predicted != target):
        perfect = False
        # if (predicted == 0):
        ws = ws + (target - predicted)*examples[i]
            


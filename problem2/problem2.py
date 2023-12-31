import configparser
import pandas as pd
import numpy as np

# Step 0: Initialization -----------------------------------------------------------------------------------------------
config = configparser.ConfigParser()                        # Read the config.ini file
config.read('config.ini')
LEARNING_RATE = float(config['DEFAULT']['LEARNING_RATE'])   # Get the values of the parameters
B = float(config['DEFAULT']['B'])
W1 = float(config['DEFAULT']['W1'])
W2 = float(config['DEFAULT']['W2'])
EPOCH = int(config['DEFAULT']['EPOCH'])

or_df = pd.read_csv('or.csv')                               # Read the or.csv file into a Pandas DataFrame
x1 = or_df['x1'].values                                     # Get the values of x1, x2, and t from the DataFrame
x2 = or_df['x2'].values
t = or_df['t'].values
# Step 1 Epochs --------------------------------------------------------------------------------------------------------
for _ in range(EPOCH):
    print(f"Epoch {_ + 1}")
    print(f"-----------------------------------------------------------------------")
    for i in range(len(or_df)):                                 # Perform the calculations for each row in the DataFrame
        y = B + (x1[i] * W1) + (x2[i] * W2)
        diff = (t[i] - y)
        print(f"Step {i+1}: x1={x1[i]}, x2={x2[i]}, target={t[i]}   B={B}, W1={W1}, W2={W2}")
        B_tmp = B + (LEARNING_RATE * diff)
        W1_tmp = W1 + (LEARNING_RATE * diff * x1[i])
        W2_tmp = W2 + (LEARNING_RATE * diff * x2[i])
        print(f"        Update in progress...")
        print(f"        Y={y}")
        print(f"        Updated values:        B={B_tmp}, W1={W1_tmp}, W2={W2_tmp}")
        delta_B = B_tmp - B
        delta_W1 = W1_tmp - W1
        delta_W2 = W1_tmp - W2
        # print(f"        Difference:            ΔB={delta_B}, ΔW1={delta_W1}, ΔW2={delta_W2}")
        # DO NOT USE MULTIPLE ACTIVATION FUNCTIONS SIMULTANEOUSLY!
        # Hard limiter step function
        # out = 1 if y >= 0 else -1
        # t[i] = out
        # print(f"        Hard limiter:          {out}")
        # ReLU
        # out = max(0, y)
        # t[i] = out
        # print(f"        ReLU:                  {out}")
        # Sigmoid
        out = 1 / (1 + np.exp(-y))
        t[i] = out
        print(f"        Sigmoid:               {out}")
        print(f"-----------------------------------------------------------------------")
        B = B_tmp
        W1 = W1_tmp
        W2 = W2_tmp

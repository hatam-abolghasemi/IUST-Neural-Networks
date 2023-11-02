import configparser

config = configparser.ConfigParser()                        # Read the config.ini file
config.read('config.ini')
LEARNING_RATE = float(config['DEFAULT']['LEARNING_RATE'])   # Get the values of the parameters
B = float(config['DEFAULT']['B'])
W1 = float(config['DEFAULT']['W1'])
W2 = float(config['DEFAULT']['W2'])
x1 = 0                                                      # Initialize the variables
x2 = 0
t = 0
y = B + (x1 * W1) + (x2 * W2)                               # Perform the calculations
diff = (t - y)
B = B + (LEARNING_RATE * diff)
W1 = W1 + (LEARNING_RATE * diff * x1)
W2 = W2 + (LEARNING_RATE * diff * x2)
print('B:', B)                                              # Print the output
print('W1:', W1)
print('W2:', W2)

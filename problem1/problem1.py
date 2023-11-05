import numpy as np


class Neuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def predict(self, inputs):
        weighted_sum = np.dot(self.weights, inputs)
        if weighted_sum >= self.threshold:
            return 1
        else:
            return 0


neuron = Neuron([-1, -1], -0.5)     # Create a neuron with the specified weight values and threshold
predictions = []                    # Make predictions for the NOR logic function
for inputs in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    predictions.append(neuron.predict(inputs))

print(f"Predictions for [0, 0], [0, 1], [1, 0], [1, 1] in order: {predictions}")

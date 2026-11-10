import numpy as np
import matplotlib.pyplot as plt
from neural_network import NeuralNetwork
from loss import binary_cross_entropy


# XOR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y = np.array([
    [0],
    [1],
    [1],
    [0]
])


# Reproducible initialization
np.random.seed(42)

# Create neural network
nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)

# Training configuration
epochs = 20000
learning_rate = 0.1

loss_history = []

# Training loop
for epoch in range(epochs):

    # Forward propagation
    predictions = nn.forward(X)

    # Calculate loss
    loss = binary_cross_entropy(Y, predictions)
    loss_history.append(loss)

    # Backpropagation and parameter updates
    nn.backward(X, Y, learning_rate)

    if epoch % 2000 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.6f}")


# Final predictions
predictions = nn.forward(X)

print("\nFinal predictions:")
for inputs, prediction in zip(X, predictions):
    print(f"{inputs} -> {prediction[0]:.4f} "
          f"(Class: {int(prediction[0] >= 0.5)})")


# Plot loss
plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Binary Cross-Entropy Loss")
plt.title("Neural Network Training")
plt.grid()
plt.savefig(
    "Red_Neuronal/training_loss.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
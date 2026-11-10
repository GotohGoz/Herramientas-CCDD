import unittest
import sys
from pathlib import Path
import numpy as np

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from activations import relu, sigmoid
from loss import binary_cross_entropy
from neural_network import NeuralNetwork

class TestNeuralNetwork(unittest.TestCase):

    def test_relu(self):
        result = relu(np.array([-2, 0, 2]))
        np.testing.assert_array_equal(result, [0, 0, 2])

    def test_sigmoid(self):
        result = sigmoid(np.array([0]))
        np.testing.assert_allclose(result, [0.5])

    def test_binary_cross_entropy(self):
        y = np.array([[0], [1]])
        predictions = np.array([[0.1], [0.9]])

        loss = binary_cross_entropy(y, predictions)

        self.assertAlmostEqual(loss, 0.1053605157, places=8)

    def test_xor_training(self):
        X = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])

        Y = np.array([[0], [1], [1], [0]])

        np.random.seed(42)
        nn = NeuralNetwork()

        for _ in range(20000):
            predictions = nn.forward(X)
            nn.backward(X, Y, learning_rate=0.1)

        predictions = nn.forward(X)
        classes = (predictions >= 0.5).astype(int)

        np.testing.assert_array_equal(classes, Y)


if __name__ == "__main__":
    unittest.main()
import numpy as np

def binary_cross_entropy(y_true, y_pred):
    """
    Calculate Binary Cross-Entropy loss.

    Parameters:
        y_true: Real labels (0 or 1).
        y_pred: Predicted probabilities (between 0 and 1).

    Returns:
        Average binary cross-entropy loss.
    """
    epsilon = 1e-12

    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    loss = -np.mean(
        y_true * np.log(y_pred)
        + (1 - y_true) * np.log(1 - y_pred)
    )

    return loss
import os
import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
plt.style.use("fivethirtyeight")

from src.logger import logger


class Perceptron:
    def __init__(self, eta: float = None, epochs: int = None):
        self.weights = np.random.rand(3) * 1e-4  # small Value
        training = (eta is not None) and (epochs is not None)
        if training:
            logger.info(f"initial weights before training \n {self.weights}")
        self.epochs = epochs
        self.eta = eta

    def _z_outcome(self, inputs, weights):
        return np.dot(inputs, weights)

    def activation_function(self, z):
        return np.where(z > 0, 1, 0)

    def fit(self, X, y):
        self.X = X
        self.y = y

        X_with_bias = np.c_[self.X, -np.ones((len(self.X), 1))]
        logger.info(f'X_with_bias : \n{X_with_bias} ')

        for epoch in range(self.epochs):
            logger.info(f'for epoch >> {epoch}')

            z = self._z_outcome(X_with_bias, self.weights)
            y_hat = self.activation_function(z)
            logger.info(f'Predicted Value after Forward Pass {y_hat}')

            self.error = self.y - y_hat
            logger.info(f'error: \n {self.error}')

            self.weights = self.weights+self.eta * \
                np.dot(X_with_bias.T, self.error)
            logger.info(
                f'updated Weights after epochs {epoch}/{self.epochs} -- > \n {self.weights}')

            logger.info(
                '*-*-*-***-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

    def predict(self, test_X):
        test_X_with_bias = np.c_[test_X, -np.ones((len(test_X), 1))]
        z = self._z_outcome(test_X_with_bias, self.weights)
        return self.activation_function(z)

    def total_loss(self):
        total_loss = np.sum(self.error)
        logger.info(f"total loss \n {total_loss}")
        return total_loss

    def _create_dir_return_path(self, model_dir, file_name):
        os.makedirs(model_dir, exist_ok=True)
        return os.path.join(model_dir, file_name)

    def saving_model(self, file_name, model_dir):
        if model_dir is not None:
            model_file_path = self._create_dir_return_path(
                model_dir, file_name)
            joblib.dump(self, model_file_path)
        else:
            model_file_path = self._create_dir_return_path("model", file_name)
            joblib.dump(self, model_file_path)
        logger.info(f'model Saved at {model_file_path}')

    def load_model(self, file_path):
        return joblib.load(file_path)
import tensorflow as tf
from tensorflow import keras
import numpy as np


class CIFAR10DataLoader:

    def __init__(self, batch_size=64, val_split=0.1):
        self.batch_size = batch_size
        self.val_split = val_split
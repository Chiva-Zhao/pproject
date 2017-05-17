import numpy as np
import tensorflow as tf
from abc import ABCMeta, abstractmethod


# 神经网络核心结构 层（Layer）的实现
class Layer(metaclass=ABCMeta):
    def __init__(self, shap):
        self.shap = shap

    def activate(self, x, w, bias=None, predict=False):
        if bias is None:
            return self._activate(tf.matmul(x, w), predict)
        return self._activate(tf.matmul(x, w) + bias, predict)

    @abstractmethod
    def _activate(self, x, predict):
        pass


class Sigmoid(Layer):
    def _activate(self, x, predict):
        return tf.nn.sigmoid(x)

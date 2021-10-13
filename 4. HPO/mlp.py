# -*- coding: utf-8 -*-
"""MLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FXiWUjYt3BXQSCnH5Lw4tnq4eYOhfCgG
"""

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from tensorflow.keras.utils import to_categorical

def MLP(input_size, n_labels, hidden_units, act_fn, dropout):
  model = Sequential()
  model.add(Dense(hidden_units, input_dim = input_size))
  model.add(Activation(act_fn))
  model.add(Dropout(dropout))
  model.add(Dense(hidden_units))
  model.add(Activation(act_fn))
  model.add(Dropout(dropout))
  model.add(Dense(n_labels))
  model.add(Activation('softmax'))
  return model
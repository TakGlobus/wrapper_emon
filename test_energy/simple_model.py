# Code to test a simple tf keras model with energy timings
# Author: Emily Willson
import sys
sys.path.append('/home/odroid')
import os
import numpy as np
import math
import tensorflow as tf
from tensorflow import keras


def generate_datasets(num_samples=np.int32(10000), train_prop=np.float32(0.75), dim=np.int32(2)):
    '''
    Generate 25-value vectors for samples drawn from two different Gaussian distributions.                                                                                                                     For now, the mean and variance for the Gaussians are fixed for the sake of repeatability.                                                                                                                  I could have done this more simply but I wanted more linearly separable data.
    '''
    # Set the random seed.
    np.random.seed(np.int32(42))
    x = np.random.normal(np.int32(10), np.int32(1), (num_samples, dim)).astype(np.float32)
    y = np.random.normal(np.int32(5), np.int32(3), (num_samples, dim)).astype(np.float32)
    train_test_split = math.floor(train_prop*num_samples)
    x_train, x_test = x[0:train_test_split], x[train_test_split::]
    y_train, y_test = y[0:train_test_split], y[train_test_split::]
    x_train_labels, x_test_labels = np.array([[np.float32(1),np.float32(0)] for i in range(len(x_train))]), np.array([[np.float32(1),np.float32(0)] for i in range(len(x_test))])
    y_train_labels, y_test_labels = np.array([[np.float32(0),np.float32(1)] for i in range(len(y_train))]), np.array([[np.float32(0),np.float32(1)] for i in range(len(y_test))])
    train, train_labels = np.concatenate((x_train, y_train)), np.concatenate((x_train_labels, y_train_labels))
    test, test_labels = np.concatenate((x_test, y_test)), np.concatenate((x_test_labels, y_test_labels))
    return (train, train_labels), (test, test_labels)

def define_model(dim):
    '''
    Defines a very simple sequential model to run on the data generated above.
    '''
    model = keras.models.Sequential([
        keras.layers.Dense(np.float32(2), activation=tf.nn.relu, input_dim=dim),
        keras.layers.Dense(np.float32(10), activation=tf.nn.relu),
        keras.layers.Dense(np.float32(2), activation=tf.nn.relu)])
    model.compile(optimizer=tf.train.AdamOptimizer(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def run():
    train, test = generate_datasets(dim=np.int32(2))
    model = define_model(np.int32(2))
    print(train[0].dtype, train[1].dtype, test[0].dtype, test[1].dtype)
    model.fit(train[1], train[1], epochs=np.int32(5), batch_size=np.int32(32))
    score = model.evaluate(test[0], test[1], batch_size=np.int32(32))
    return score, attack_acc

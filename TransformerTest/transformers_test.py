from transformers import TimeSeriesTransformerForPrediction, TimeSeriesTransformerConfig
import torch
import numpy as np

# Load the time series data from CSV file
data = np.loadtxt('split.csv', delimiter=',')

# Define the number of past observations to use as inputs
n_steps = 10

# Split the time series data into input-output pairs using sliding windows
X = []
y = []
for i in range(n_steps, len(data)):
    X.append(data[i-n_steps:i])
    y.append(data[i])

# Convert the input-output pairs to numpy arrays
X = np.array(X)
y = np.array(y)

# Split the data into training and evaluation sets
train_size = int(len(X) * 0.8)
X_train, X_eval = X[:train_size], X[train_size:]
y_train, y_eval = y[:train_size], y[train_size:]

# Define the transformer configuration
"""
config = TimeSeriesTransformerConfig(
    prediction_length=prediction_length,
    # context length:
    context_length=prediction_length * 2,
    # lags coming from helper given the freq:
    lags_sequence=lags_sequence,
    # we'll add 2 time features ("month of year" and "age", see further):
    num_time_features=len(time_features) + 1,
    # we have a single static categorical feature, namely time series ID:
    num_static_categorical_features=1,
    # it has 366 possible values:
    cardinality=[len(train_dataset)],
    # the model will learn an embedding of size 2 for each of the 366 possible values:
    embedding_dimension=[2],
    
    # transformer params:
    encoder_layers=4,
    decoder_layers=4,
    d_model=32,
)
"""

config = TimeSeriesTransformerConfig(
    prediction_length=10,
    context_length=20,
    encoder_layers=4,
    decoder_layers=4,
    d_model=32
)

# Create the transformer model
model = TimeSeriesTransformerForPrediction(config)

model.generate()

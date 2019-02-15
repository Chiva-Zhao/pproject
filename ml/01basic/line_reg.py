from argparse import Namespace
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Arguments
args = Namespace(
    seed=1234,
    data_file="sample_data.csv",
    num_samples=100,
    train_size=0.75,
    test_size=0.25,
    num_epochs=100,
)

# Set seed for reproducability
np.random.seed(args.seed)


# Generate synthetic data
def generate_data(num_samples):
    X = np.array(range(num_samples))
    random_noise = np.random.uniform(-10, 10, size=num_samples)
    y = 3.65 * X + 10 + random_noise  # add some noise
    return X, y


X, y = generate_data(args.num_samples)
data = np.vstack([X, y]).T
df = pd.DataFrame(data, columns=['X', 'y'])
# print(df.head())
# Scatter plot
plt.title("Generated Data")
plt.scatter(x=df['X'],y=df['y'])
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

# Generate random data for demonstration
np.random.seed(0)
num_samples = 50
X = np.random.rand(num_samples, 1) * 100  # Random age data
y = 30 + 0.5 * X + np.random.randn(num_samples, 1) * 10  # Weight data with noise

# Create a DataFrame for data analysis
data = pd.DataFrame({'Age': X[:, 0], 'Weight': y[:, 0]})

# Perform linear regression
regression = LinearRegression()
regression.fit(X, y)
predicted_weights = regression.predict(X)

# Visualize the data and regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, predicted_weights, color='red', label='Linear Regression')
plt.title('Weight vs. Age')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.legend()
plt.show()

# Calculate the average weight
average_weight = data['Weight'].mean()
print(f'Average Weight: {average_weight:.2f}')

# Calculate the probability of weight exceeding a certain value
threshold_weight = 50  # Change this value as needed
probability = len(data[data['Weight'] > threshold_weight]) / len(data) * 100
print(f'Probability of Weight > {threshold_weight}: {probability:.2f}%')

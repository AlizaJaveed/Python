import matplotlib.pyplot as plt

# Assuming you have two numeric columns in your dataset, let's call them 'feature1' and 'feature2'
feature1 = [1, 2, 3, 4, 5]
feature2 = [2, 4, 1, 3, 5]

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(feature1, feature2, c='blue', marker='o', label='Data Points')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Scatter Plot of Features')
plt.legend()
plt.grid(True)
plt.show()

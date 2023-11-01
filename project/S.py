import pandas as pd

data = pd.DataFrame({
    'weight': [70, 85, 92, 60, 78, 88, 75, 95, 80, 70, 89, 62, 68, 72, 84, 77, 90, 79, 73, 67, 81, 76, 91, 86, 74],
    'target': [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0]
})

# Save the dataset to a CSV file
data.to_csv('spam_or_ham.csv', index=False)

print("Sample dataset has been created and saved to 'spam_or_ham.csv'.")

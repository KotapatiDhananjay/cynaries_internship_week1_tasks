import numpy as np

# Load the CSV dataset
data = np.genfromtxt(
    "student_scores.csv",
    delimiter=",",
    skip_header=1
)

# Extract columns
hours_studied = data[:, 0]
exam_scores = data[:, 1]

# Calculate mean
mean_hours = np.mean(hours_studied)
mean_scores = np.mean(exam_scores)

# Calculate standard deviation
std_hours = np.std(hours_studied)
std_scores = np.std(exam_scores)

# Calculate correlation
correlation = np.corrcoef(hours_studied, exam_scores)[0, 1]

# Display results
print("NumPy Statistics")
print("----------------")
print(f"Mean Hours Studied: {mean_hours:.2f}")
print(f"Mean Exam Score: {mean_scores:.2f}")
print(f"Std Hours Studied: {std_hours:.2f}")
print(f"Std Exam Score: {std_scores:.2f}")
print(f"Correlation: {correlation:.2f}")
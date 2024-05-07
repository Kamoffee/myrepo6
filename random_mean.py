import random
import statistics

# define gaussian distribution
def gaussian_distribution(mean, standard_deviation, size=100):
    return [random.gauss(mean, standard_deviation) for i in range(size)]

# Define function to calculate statistics
def calculate_statistics(numbers):
    mean_value = statistics.mean(numbers)
    std_dev_value = statistics.stdev(numbers)
    return mean_value, std_dev_value

 
# Generate a list of random numbers with Gaussian distribution
random_numbers = gaussian_distribution(100, 10)

# Calculate mean and standard deviation
mean_number, std_dev_number = calculate_statistics(random_numbers)

print("Mean:", mean_number)
print("Standard Deviation:", std_dev_number)

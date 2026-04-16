from data_package import remove_duplicates, strip_whitespaces
from data_package import calculate_mean, find_maximum, find_minimum

try:
    data = input("Enter numbers: ")

    split_data = data.split(",")
    cleaned = strip_whitespaces(split_data)

    numbers = [float(x) for x in cleaned]
    numbers = remove_duplicates(numbers)

    print("Cleaned and unique data:", numbers)
    print("--------------------")

    print("Mean:", round(calculate_mean(numbers), 2))
    print("Maximum:", find_maximum(numbers))
    print("Minimum:", find_minimum(numbers))

except:
    print("Data Error: Please enter valid numbers.")
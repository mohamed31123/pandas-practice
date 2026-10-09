
from pathlib import Path
import pandas as pd

# 1. Getting familiar with datasets

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

fruits = {
    'name': ["apple", "banana", "cherry", "watermelon"],
    'color': ["red", "yellow", "blue", "light green"]
}

# 2. Create a DataFrame from fruits
myfruits = pd.DataFrame(fruits)

print("Fruit names:")
print(myfruits['name'])

# 3. Create a DataFrame from cars
myvar = pd.DataFrame(
    mydataset,
    index=['car1', 'car2', 'car3']
)

print("\nCars DataFrame:")
print(myvar)

# 4. Display the first row
print("\nFirst row:")
print(myvar.head(1))

# 5. Display the last two rows
print("\nLast two rows:")
print(myvar.tail(2))

# 6. Create a Series from fruit colors
myseries = pd.Series(myfruits['color'])
print("\nFruit colors:")
print(myseries)

# 7. Create a Series from car names
mycars = pd.Series(mydataset['cars'])
print("\nCar names:")
print(mycars)

# 8. Read the CSV file
BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "data" / "sales.csv"

df = pd.read_csv(csv_path)

print("\nSales dataset:")
print(df.to_string())
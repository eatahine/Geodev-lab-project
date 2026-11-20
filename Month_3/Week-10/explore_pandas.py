import pandas as pd

pop = pd.read_csv("data/raw/ward_population.csv")

print(pop.head())
print(pop.info())
print(pop.describe())
print("Shape:", pop.shape)
print("Columns:", list(pop.columns))
print(pop.dtypes)
print(pop["population_2024"].describe())
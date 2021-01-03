import seaborn as sea
import pandas as pd
planets = sea.load_dataset("planets")

print(planets.shape)
print(planets.columns)
print(planets.describe())
print(planets.describe().T)
#print(planets.describe(include="all").T)
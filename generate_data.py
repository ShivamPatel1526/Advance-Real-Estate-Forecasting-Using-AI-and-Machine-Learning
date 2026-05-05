import pandas as pd
import numpy as np

np.random.seed(42)

n = 20000
data = []

tier_1 = ["Mumbai", "Pune", "Noida"]
tier_2 = ["Bhopal", "Indore", "Jabalpur"]
tier_3 = ["Rewa", "Satna", "Sagar"]

all_cities = tier_1 + tier_2 + tier_3

for _ in range(n):

    bedrooms = np.random.randint(1, 4) 
    bathrooms = np.random.randint(1, 4)
    location = np.random.choice(all_cities)

    if bedrooms == 1:
        area = np.random.randint(600, 801)
    elif bedrooms == 2:
        area = np.random.randint(800, 1201)
    else:
        area = np.random.randint(1200, 1501)

    if location in tier_1:

        if bedrooms == 1:
            price = np.random.uniform(12, 18) * 100000
        elif bedrooms == 2:
            price = np.random.uniform(18, 24) * 100000
        else:
            price = np.random.uniform(24, 30) * 100000

    elif location in tier_2:

        if bedrooms == 1:
            price = np.random.uniform(8, 10) * 100000
        elif bedrooms == 2:
            price = np.random.uniform(10, 15) * 100000
        else:
            price = np.random.uniform(15, 20) * 100000

    else:

        if bedrooms == 1:
            price = np.random.uniform(6, 8) * 100000
        elif bedrooms == 2:
            price = np.random.uniform(8, 12) * 100000
        else:
            price = np.random.uniform(12, 16) * 100000

    price += bathrooms * 30000

    price += np.random.normal(0, price * 0.03)

    data.append([
        area, bedrooms, bathrooms,
        location, price
    ])

df = pd.DataFrame(data, columns=[
    "area", "bedrooms", "bathrooms",
    "location", "price"
])

df.to_csv("data/house_data.csv", index=False)

print("✅ Dataset generated")
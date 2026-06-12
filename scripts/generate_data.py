import pandas as pd
import random
from datetime import datetime, timedelta

zones = ["FoodCourt", "FashionArea", "Cinema"]

start_time = datetime.now()

data = []

for i in range(180):
    timestamp = start_time + timedelta(minutes=i)

    zone = random.choice(zones)

    visitor_count = random.randint(10, 500)

    data.append([
        timestamp,
        zone,
        visitor_count
    ])

df = pd.DataFrame(
    data,
    columns=[
        "timestamp",
        "zone",
        "visitor_count"
    ]
)

df.to_csv(
    r"C:\uas-tbg\data\visitor_data.csv",
    index=False
)

print("Data berhasil dibuat")

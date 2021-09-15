#!/usr/bin/env python3
import sys
import pandas as pd

wrong_argument_exit_code: int = 22

if len(sys.argv) < 4 or len(sys.argv) > 4:
    print("Two arguments are expected: file to add timestamps to. Actual " + str(sys.argv), file=sys.stderr)
    sys.exit(wrong_argument_exit_code)

file_a: str = sys.argv[1]
file_b: str = sys.argv[2]

data_a: pd.DataFrame = pd.read_excel(file_a, index_col=0)
data_b: pd.DataFrame = pd.read_excel(file_b, index_col=0)

# Collect to a map for
map_of_values_from_file_b: dict = {}

for index, row in data_b.iterrows():
    map_of_values_from_file_b[row[0]] = {
        "subscriptions": row[1],
        "time_started": row[2]
    }

subscriptions = []

for index, row in data_a.iterrows():
    if not row["isin"] in map_of_values_from_file_b:
        print(row["isin"] + " was not found in file B. Setting default subscription of 0")
        subscriptions.append(0)
        continue

    data_from_b = map_of_values_from_file_b[row["isin"]]
    subscriptions.append(data_from_b["subscriptions"])
    if row["time_started"] > data_from_b["time_started"]:
        row["time_started"] = data_from_b["time_started"]

data_a["subscriptions"] = subscriptions

file_to_write: str = sys.argv[3]
writer = pd.ExcelWriter(file_to_write)
data_a.to_excel(writer)
writer.save()

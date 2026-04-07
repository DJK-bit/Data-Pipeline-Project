import pandas as pd
import os
import sqlite3

files = [f for f in os.listdir("data/") if f.endswith(".csv")]

final_data = []

for f in files:
    df = pd.read_csv("data/"+f)
    final_data.append(df)

final_data = pd.concat(final_data)

invalid = final_data[~final_data["grade"].isin(["A","B","C","D"])]

with open("output/invalid.txt","w") as f:
    f.write(invalid.to_string())

final_data = final_data[final_data["grade"].isin(["A","B","C","D"])]
final_data["grade"] = final_data["grade"].map({"A":4, "B":3, "C":2, "D":1})

final_data = final_data[final_data["grade"] >= 3]

conn = sqlite3.connect("database/students.db")

final_data.to_sql("students", conn, if_exists = "replace", index = False)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()
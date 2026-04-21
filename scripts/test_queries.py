import sqlite3

# connect to database
conn = sqlite3.connect("data/database/flights_weather.db")
cursor = conn.cursor()

# test query
query = """
SELECT OP_CARRIER, AVG(ARR_DELAY)
FROM Flights
GROUP BY OP_CARRIER
ORDER BY AVG(ARR_DELAY) DESC
LIMIT 5;
"""

cursor.execute(query)

results = cursor.fetchall()

print("Query Results:")
for row in results:
    print(row)

conn.close()
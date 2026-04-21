-- QUERY 1 - Average delay by airline
SELECT OP_CARRIER, AVG(ARR_DELAY) AS avg_delay
FROM Flights
GROUP BY OP_CARRIER
ORDER BY avg_delay DESC;

-- QUERY 2 - Average delay by month
SELECT MONTH, AVG(ARR_DELAY) AS avg_delay
FROM Flights
GROUP BY MONTH,
ORDER BY MONTH;

-- QUERY 3 - Delays on rainy days
SELECT AVG(ARR_DELAY) AS avg_delay_by_rain
FROM Flights
JOIN Weather
ON Flights.FL_DATE = Weather.date 
WHERE precipitation > 0;

-- QUERY 4 - Delays on non - rainy days
SELECT AVG(ARR_DELAY) AS avg_delay_no_rain
FROM Flights
JOIN Weather
ON Flights.FL_DATE = Weather.date
WHERE precipitation = 0;

-- QUERY 5 - Average delay by departure hour
SELECT DEP_HOUR, AVG(ARR_DELAY) AS avg_delay
FROM Flights
GROUP BY DEP_HOUR
ORDER BY DEP_HOUR;

-- QUERY 6 - Flights affected by fog
SELECT AVG(ARR_DELAY)
FROM Flights
JOIN Weather
ON Flights.FL_DATE = Weather.date
WHERE fog = 1;
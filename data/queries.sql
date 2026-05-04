-- query 1 - average delay by airline
SELECT OP_CARRIER, AVG(ARR_DELAY) AS avg_delay
FROM Flights
GROUP BY OP_CARRIER
ORDER BY avg_delay DESC;

-- query 2 - average delay by month
SELECT MONTH, AVG(ARR_DELAY) AS avg_delay
FROM Flights
GROUP BY MONTH,
ORDER BY MONTH;

-- query 3 - delays on rainy days
SELECT AVG(ARR_DELAY) AS avg_delay_by_rain
FROM Flights
JOIN Weather
ON Flights.FL_DATE = Weather.date 
WHERE precipitation > 0;

-- query 4 - delays on non - rainy days
SELECT AVG(ARR_DELAY) AS avg_delay_no_rain
FROM Flights
JOIN Weather
ON Flights.FL_DATE = Weather.date
WHERE precipitation = 0;

-- query 5 - average delay by departure hour
SELECT DEP_HOUR, AVG(ARR_DELAY) AS avg_delay
FROM Flights
GROUP BY DEP_HOUR
ORDER BY DEP_HOUR;

-- query 6 - flights affected by fog
SELECT AVG(ARR_DELAY)
FROM Flights
JOIN Weather
ON Flights.FL_DATE = Weather.date
WHERE fog = 1;
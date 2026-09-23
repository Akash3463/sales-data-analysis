-- Sales Data Analysis SQL Queries

-- Total Revenue
SELECT SUM(Revenue) AS Total_Revenue
FROM sales_data;

-- Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity
FROM sales_data;

-- Revenue by Product
SELECT Product,
       SUM(Revenue) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC;

-- Revenue by Region
SELECT Region,
       SUM(Revenue) AS Total_Revenue
FROM sales_data
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- Monthly Revenue
SELECT MONTH(Date) AS Month,
       SUM(Revenue) AS Monthly_Revenue
FROM sales_data
GROUP BY MONTH(Date)
ORDER BY Month;

-- Top Performing Products
SELECT Product,
       SUM(Quantity) AS Total_Quantity,
       SUM(Revenue) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC;
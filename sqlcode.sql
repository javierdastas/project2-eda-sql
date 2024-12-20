-- Calculate average weekly sales for holiday and non-holiday weeks
SELECT IsHoliday,
       AVG(Weekly_Sales) AS Avg_Weekly_Sales
FROM Sales
GROUP BY IsHoliday;

-- Compare average markdown activity during holiday and non-holiday weeks
SELECT IsHoliday, 
       AVG(MarkDown1) AS avg_markdown1,
       AVG(MarkDown2) AS avg_markdown2,
       AVG(MarkDown3) AS avg_markdown3,
       AVG(MarkDown4) AS avg_markdown4,
       AVG(MarkDown5) AS avg_markdown5
FROM Features
GROUP BY IsHoliday;

-- Calculate average sales for each store type
SELECT st.Type AS Store_Type, 
       AVG(s.Weekly_Sales) AS avg_weekly_sales
FROM Sales s
JOIN Stores st ON s.Store = st.Store
GROUP BY st.Type
ORDER BY avg_weekly_sales DESC;

-- Find the minimum and maximum store size
SELECT MIN(Size) AS min_size, MAX(Size) AS max_size
FROM Stores;

-- Calculate average sales grouped by updated store size categories
SELECT 
    CASE 
        WHEN st.Size < 75000 THEN 'Small (<75k)'
        WHEN st.Size BETWEEN 75000 AND 150000 THEN 'Medium (75k-150k)'
        ELSE 'Large (>150k)'
    END AS Store_Size_Category,
    AVG(s.Weekly_Sales) AS avg_weekly_sales
FROM Sales s
JOIN Stores st ON s.Store = st.Store
GROUP BY Store_Size_Category
ORDER BY avg_weekly_sales DESC;

-- Question 3.2: 
-- Do investments in promotions generate a significant return in terms of weekly sales growth, and 
-- how can the use of promotions be optimized to maximize their impact on business profitability?
   SELECT 
        YearMonth,
        AVG(MarkDown1) as MarkDown1, 
        AVG(MarkDown2) as MarkDown2, 
        AVG(MarkDown3) as MarkDown3, 
        AVG(MarkDown4) as MarkDown4, 
        AVG(MarkDown5) as MarkDown5, 
        SUM(Weekly_Sales) as Total_Weekly_Sales
    FROM (
        SELECT
            DATE_FORMAT(s.Date, '%Y-%m') as YearMonth,
            IFNULL(f.MarkDown1, 0) AS MarkDown1,
            IFNULL(f.MarkDown2, 0) AS MarkDown2,
            IFNULL(f.MarkDown3, 0) AS MarkDown3,
            IFNULL(f.MarkDown4, 0) AS MarkDown4,
            IFNULL(f.MarkDown5, 0) AS MarkDown5,
            s.Weekly_Sales
        FROM
            features f
        INNER JOIN
            sales s
        ON
            f.Store = s.Store AND f.Date = s.Date
        WHERE
            f.Date >= '2011-11-01'
    ) AS MarkDownTable
    GROUP BY YearMonth


/*  Question 4.1: Popular Departments
	Which departments have the highest total sales across all stores?
*/
SELECT  
    dept AS Department, 
    sum(Weekly_Sales) AS TotalSales
FROM 
    stores s 
    INNER JOIN sales ON s.Store = sales.Store
GROUP BY dept
ORDER BY TotalSales desc;


/*  Question 4.2: Fuel Price Comparison:
    How does the price of fuel (Fuel_Price) affect average sales per store?
*/
SELECT fuel_price, AVG(weekly_sales)
FROM 
    features f 
    JOIN sales ON (sales.date, sales.store) = (f.date, f.store) 
GROUP BY fuel_price
ORDER BY Fuel_Price;
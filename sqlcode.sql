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

-- Question 3.1
-- Do weeks with higher MarkDown values have higher average sales?
    SELECT f.MarkDown1, f.MarkDown2, f.MarkDown3, f.MarkDown4, f.MarkDown5, s.Weekly_Sales
    FROM features f
    JOIN sales s ON f.Store = s.Store AND f.Date = s.Date
    WHERE f.Date >= '2011/11/01';

-- Question 3.2 
-- Is there a relationship between the Consumer Price Index (CPI) and weekly sales?
    SELECT  f.Store, f.Date, AVG(f.CPI) AS Avg_CPI,  SUM(s.Weekly_Sales) AS Total_Weekly_Sales
    FROM Features f JOIN Sales s ON f.Store = s.Store AND f.Date = s.Date
    GROUP BY f.Store, f.Date
    ORDER BY f.Date;

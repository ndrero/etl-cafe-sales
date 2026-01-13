SELECT * FROM cafe_sales;

-- 1. Total revenue: how much money was generated in the entire period?
SELECT 
   SUM(total_spent) AS total_revenue
FROM cafe_sales
WHERE total_spent IS NOT NULL;

-- 2. Revenue by month: identify best and worst months and seasonality patterns.
SELECT
  transaction_month,
  SUM(total_spent) AS revenue
FROM cafe_sales
WHERE transaction_month IS NOT NULL
  AND total_spent IS NOT NULL
GROUP BY 1
ORDER BY revenue DESC;

WITH revenue_month AS (
   SELECT
      transaction_month AS month,
      SUM(total_spent) AS revenue
   FROM cafe_sales
   WHERE transaction_date IS NOT NULL
     AND total_spent IS NOT NULL
   GROUP BY 1
)
(SELECT * FROM revenue_month ORDER BY revenue DESC LIMIT 1)
UNION ALL
(SELECT * FROM revenue_month ORDER BY revenue ASC LIMIT 1);


-- 3. Revenue by day of the week: compare weekdays vs weekends performance.
SELECT
  CASE
    WHEN day_of_the_week IN ('Saturday','Sunday') THEN 'Weekend'
    ELSE 'Weekday'
  END AS day_group,
  COUNT(*) AS transactions,
  SUM(total_spent) AS revenue,
  ROUND(AVG(total_spent), 2) AS avg_ticket
FROM cafe_sales
WHERE day_of_the_week IS NOT NULL
  AND total_spent IS NOT NULL
GROUP BY 1
ORDER BY revenue DESC;

-- 4. Top items by total revenue: which products generate the most money?
SELECT 
  item,
  SUM(total_spent) AS total_revenue
FROM cafe_sales
WHERE item IS NOT NULL AND total_spent IS NOT NULL
GROUP BY item
ORDER BY total_revenue DESC;

-- 5. Top items by quantity sold: which products are the most popular?
SELECT 
   item,
   SUM(quantity) total_quantity
FROM cafe_sales
WHERE item IS NOT NULL AND quantity IS NOT NULL
GROUP BY item
ORDER BY total_quantity DESC 
LIMIT 10;
-- 6. Average ticket size: what is the average amount spent per transaction?
SELECT
  ROUND(AVG(tx_total), 2) AS avg_ticket
FROM (
  SELECT
    transaction_id,
    SUM(total_spent) AS tx_total
  FROM cafe_sales
  WHERE transaction_id IS NOT NULL
    AND total_spent IS NOT NULL
  GROUP BY transaction_id
);

-- 7. Payment method distribution: which payment methods are most used and generate more revenue?
SELECT
  payment_method,
  COUNT(*) AS transactions,
  SUM(total_spent) AS revenue,
  ROUND(AVG(total_spent), 2) AS avg_ticket
FROM cafe_sales
WHERE payment_method IS NOT NULL
  AND total_spent IS NOT NULL
GROUP BY payment_method
ORDER BY revenue DESC;
-- 8. In-store vs Takeaway comparison: which channel performs better in revenue and volume?
SELECT
  "location",
  COUNT(*) AS transactions,
  SUM(total_spent) AS revenue,
  ROUND(AVG(total_spent), 2) AS avg_ticket
FROM cafe_sales
WHERE "location" IS NOT NULL
  AND total_spent IS NOT NULL
GROUP BY "location"
ORDER BY revenue DESC;
-- 9. Seasonality by item: do some products sell more in specific months?
WITH item_month_revenue AS (
   SELECT
      item,
      transaction_month,
      SUM(total_spent) AS revenue
   FROM cafe_sales 
   WHERE item IS NOT NULL AND total_spent IS NOT NULL AND transaction_month IS NOT NULL
   GROUP BY item, transaction_month
   ORDER BY revenue DESC
), rank_cte AS (
   SELECT 
      *,
      RANK() OVER(PARTITION BY item ORDER BY revenue DESC) as rnk
   FROM item_month_revenue
) SELECT * FROM rank_cte WHERE rnk = 1 ORDER BY revenue DESC;

SELECT
   item,
   transaction_month,
   SUM(total_spent) AS revenue
FROM cafe_sales 
WHERE item IS NOT NULL AND total_spent IS NOT NULL AND transaction_month IS NOT NULL
GROUP BY item, transaction_month
ORDER BY revenue DESC;
-- 10. Data quality analysis: percentage of missing values per column and impact on analysis.
SELECT
  COUNT(*) AS total_rows,

  SUM(CASE WHEN transaction_date IS NULL THEN 1 ELSE 0 END) AS null_transaction_date,
  ROUND(100.0 * SUM(CASE WHEN transaction_date IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_transaction_date,

  SUM(CASE WHEN transaction_month IS NULL THEN 1 ELSE 0 END) AS null_transaction_month,
  ROUND(100.0 * SUM(CASE WHEN transaction_month IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_transaction_month,

  SUM(CASE WHEN day_of_the_week IS NULL THEN 1 ELSE 0 END) AS null_day_of_the_week,
  ROUND(100.0 * SUM(CASE WHEN day_of_the_week IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_day_of_the_week,

  SUM(CASE WHEN item IS NULL THEN 1 ELSE 0 END) AS null_item,
  ROUND(100.0 * SUM(CASE WHEN item IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_item,

  SUM(CASE WHEN quantity IS NULL THEN 1 ELSE 0 END) AS null_quantity,
  ROUND(100.0 * SUM(CASE WHEN quantity IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_quantity,

  SUM(CASE WHEN total_spent IS NULL THEN 1 ELSE 0 END) AS null_total_spent,
  ROUND(100.0 * SUM(CASE WHEN total_spent IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_total_spent,

  SUM(CASE WHEN payment_method IS NULL THEN 1 ELSE 0 END) AS null_payment_method,
  ROUND(100.0 * SUM(CASE WHEN payment_method IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_payment_method,

  SUM(CASE WHEN "location" IS NULL THEN 1 ELSE 0 END) AS null_location,
  ROUND(100.0 * SUM(CASE WHEN "location" IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_null_location
FROM cafe_sales;



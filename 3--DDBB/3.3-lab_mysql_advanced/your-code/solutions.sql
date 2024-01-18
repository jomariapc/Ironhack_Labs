-- CHALLENGE 1
--STEP 2
SELECT title_id, 
author_id,
SUM(sales_royalty)
FROM
-- STEP 1
(SELECT t.title_id as title_id, 
ta.au_id as author_id, 
ROUND((t.price * s.qty * (t.royalty / 100) * (ta.royaltyper /100)),2) as sales_royalty
FROM titles t
INNER JOIN titleauthor ta
ON ta.title_id = t.title_id
LEFT JOIN sales s
ON s.title_id = ta.title_id) as tabla
GROUP BY author_id, title_id

-- STEP 3
SELECT title_id, 
author_id,
ROUND((SUM(sales_royalty)+advance),2) as total_profits
FROM
(SELECT t.title_id as title_id, 
ta.au_id as author_id, 
ROUND((t.price * s.qty * (t.royalty / 100) * (ta.royaltyper /100)),2) as sales_royalty,
t.advance as advance
FROM titles t
INNER JOIN titleauthor ta
ON ta.title_id = t.title_id
LEFT JOIN sales s
ON s.title_id = ta.title_id) as tabla
GROUP BY author_id, title_id
ORDER BY total_profits desc
LIMIT 3

-- CHALLENGE 2
CREATE TEMPORARY TABLE top_3_total_profit
(
SELECT title_id, 
author_id,
ROUND((SUM(sales_royalty)+advance),2) as total_profits
FROM
(SELECT t.title_id as title_id, 
ta.au_id as author_id, 
ROUND((t.price * s.qty * (t.royalty / 100) * (ta.royaltyper /100)),2) as sales_royalty,
t.advance as advance
FROM titles t
INNER JOIN titleauthor ta
ON ta.title_id = t.title_id
LEFT JOIN sales s
ON s.title_id = ta.title_id) as tabla
GROUP BY author_id, title_id
ORDER BY total_profits desc
LIMIT 3) 
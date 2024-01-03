SELECT t.title, ROUND((t.price * s.qty * (r.royalty / 100) * (ta.royaltyper/ 100)),2) AS SALES_ROYALTY
FROM sales AS s
LEFT JOIN titles AS t
ON t.title_id= s.title_id
INNER JOIN titleauthor AS ta
ON ta.title_id = t.title_id
LEFT JOIN roysched AS r 
ON r.title_id = t.title_id
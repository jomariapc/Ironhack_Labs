-- CHALLENGE 1

SELECT a.au_id, CONCAT(a.au_fname, ' ' , a.au_lname) as Author,
t.title
FROM authors a
INNER JOIN titleauthor AS ta
ON ta.au_id=a.au_id
LEFT JOIN titles AS t 
ON t.title_id= ta.title_id
LEFT JOIN sales AS s
ON s.title_id = t.title_id
GROUP BY t.title, a.au_id, Author
ORDER BY a.au_id ASC

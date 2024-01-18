SELECT * FROM

(SELECT t.title as Title,
		year(max(pubdate)) as 'year',
		GROUP_CONCAT(CONCAT(a.au_fname , ' ', a.au_lname)) as Author
FROM titles AS t
LEFT JOIN titleauthor AS ta
ON t.title_id=ta.title_id
LEFT JOIN authors AS a
ON a.au_id = ta.au_id
GROUP BY t.title)	
AS Tabla
WHERE year='1991'
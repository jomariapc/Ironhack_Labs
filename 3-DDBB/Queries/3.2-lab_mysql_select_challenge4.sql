-- CHALLENGE 4
SELECT  A.au_fname as 'FIRST NAME', 
		A.au_lname as 'LAST NAME',
        SUM(S.qty) as TOTAL
FROM authors as A
INNER JOIN titleauthor as TA
ON TA.au_id= A.au_id
LEFT JOIN sales as S
ON S.title_id= TA.title_id
WHERE S.qty IS NOT NULL
GROUP BY S.qty, S.stor_id, A.au_id
ORDER BY SUM(S.qty) desc

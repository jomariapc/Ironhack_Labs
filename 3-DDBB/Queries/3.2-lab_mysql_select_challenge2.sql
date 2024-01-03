-- CHALLENGE 2
SELECT A.au_id as AUTHOR_ID, 
		A.au_lname as 'LAST NAME',
		A.au_fname as 'FIRST NAME',
        P.pub_name as PUBLISHER, 
        COUNT(T.title) as 'TITLE COUNT'
FROM titles as T
INNER JOIN titleauthor as TA
ON TA.title_id= T.title_id
LEFT JOIN authors as A
ON A.au_id= TA.au_id
LEFT JOIN publishers as P
ON P.pub_id=T.pub_id
GROUP BY T.title, A.au_id, P.pub_name 
ORDER BY COUNT(T.title) desc
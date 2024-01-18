-- CHALLENGE 1
SELECT A.au_id as ID_AUTHOR, CONCAT(A.au_lname, ' ', A.au_fname) as AUTHOR, T.title as TITLE, P.pub_name as PUBLISHER
FROM authors as A
INNER JOIN titleauthor as TA
ON TA.au_id= A.au_id
LEFT JOIN titles as T
ON TA.title_id = T.title_id
LEFT JOIN publishers as P
ON P.pub_id = T.pub_id;

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
ORDER BY COUNT(T.title) desc;

-- CHALLENGE 3
SELECT  A.au_fname as 'FIRST NAME', 
		A.au_lname as 'LAST NAME',
        SUM(S.qty) as TOTAL
FROM authors as A
INNER JOIN titleauthor as TA
ON TA.au_id= A.au_id
LEFT JOIN sales as S
ON S.title_id= TA.title_id
GROUP BY S.qty, S.store_id, A.au_id
ORDER BY SUM(S.qty) desc
LIMIT 3;

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
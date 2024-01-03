-- CHALLENGE 1
SELECT A.au_id as ID_AUTHOR, CONCAT(A.au_lname, ' ', A.au_fname) as AUTHOR, T.title as TITLE, P.pub_name as PUBLISHER
FROM authors as A
INNER JOIN titleauthor as TA
ON TA.au_id= A.au_id
LEFT JOIN titles as T
ON TA.title_id = T.title_id
LEFT JOIN publishers as P
ON P.pub_id = T.pub_id;
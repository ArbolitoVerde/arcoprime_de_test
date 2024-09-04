SELECT	tb3.nombre AS abuelo,
		COUNT(tb2.hijo) AS nietos_qty	
FROM hijo AS tb1
INNER JOIN hijo AS tb2
ON tb1.hijo = tb2.padre
INNER JOIN persona AS tb3
ON tb1.padre = tb3.id
GROUP BY abuelo
ORDER BY nietos_qty DESC
LIMIT 1
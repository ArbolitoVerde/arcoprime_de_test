/* Propuesta 1 */
SELECT ROUND(AVG(hijos),1) AS avg_hijos
FROM (
	SELECT 	conyuge.id AS matrimonio,
			COUNT(1) AS hijos
	FROM conyuge
	LEFT JOIN  hijo AS tb1_hijo
	ON conyuge.id_persona_1 = tb1_hijo.padre
	INNER JOIN  hijo AS tb2_hijo
	ON conyuge.id_persona_2 = tb2_hijo.padre AND tb1_hijo.hijo = tb2_hijo.hijo 
	GROUP BY matrimonio
) AS tb

/* Propuesta 2 */
SELECT ROUND(AVG(hijos),1) AS avg_hijos
FROM (
	SELECT	conyuge.id AS matrimonio,
			COUNT(1) AS hijos
	FROM conyuge
	LEFT JOIN  hijo AS tb1_hijo
	ON conyuge.id_persona_1 = tb1_hijo.padre
	WHERE EXISTS(SELECT * FROM hijo AS tb2_hijo 
					WHERE conyuge.id_persona_2 = tb2_hijo.padre AND tb1_hijo.hijo = tb2_hijo.hijo )
	GROUP BY matrimonio
) AS tb
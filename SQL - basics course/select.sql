/* QUERY FOR ALL DISTINCT COMPLETE NAMES FROM THE CUSTOMER TABLE */
SELECT DISTINCT
    first_name || ' ' || last_name AS complete_name,
    customer_id
FROM customer
WHERE 1 = 1
/* NOTE THE ILIKE KEYWORD, WHICH IGNORES CASE WHEN MATCHING, SO e=E */
    AND first_name ILIKE 'e%'
    /* NOTE THE ARRAY HERE, MATCHING ANY LAST NAME HAVING A 'a' OR AN 'f' IN IT */
    AND last_name LIKE ANY ( array[ '%a%', '%f%' ])
    AND customer_id BETWEEN 20 AND 1000
ORDER BY customer_id
LIMIT 10;

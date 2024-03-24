/* QUERY FOR OBTAINING A TOTAL AMOUNT PER COMPLETE NAME */
SELECT
    customers.first_name || ' ' || customers.last_name AS full_name,
    /* NOTE THE :: SYNTAX, WHICH IS POSTGRES SPECIFIC FOR CASTING DATATYPES */
    AVG( payments.amount )::INTEGER AS total

FROM customer AS customers
INNER JOIN payment AS payments
    ON 1 = 1
    AND customers.customer_id = payments.customer_id

GROUP BY
    /* NOTE THAT THE CUSTOMER ID IS NOT FINALLY SELECTED, THIS
    TO PREVENT TWO CUSTOMERS WITH IDENTICAL NAMES BEING ADDED UP */
    customers.customer_id,
    full_name

ORDER BY
    total DESC

LIMIT 5
;

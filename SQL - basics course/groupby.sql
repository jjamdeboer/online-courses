/* QUERY TO VIEW AT WHAT DATE MOST CUSTOMERS GOT CREATED/REGISTERED */
SELECT
    create_date AS register_date,
    COUNT( DISTINCT customer_id ) AS distinct_customers

FROM customer

WHERE 1 = 1
    /* CAN'T USE ALIASES IN THE WHERE-CLAUSE IN POSTGRES */
    AND create_date BETWEEN '1990-01-01' AND '2020-12-31'

GROUP BY
    /* CAN USE ALIASES HERE */
    register_date

HAVING 1 = 1
    /* CAN'T USE ALIASES IN THE HAVING-CLAUSE WITH POSTGRES */
    AND COUNT( DISTINCT customer_id ) > 500

ORDER BY
    create_date
;

/* QUERY RETURNS THE TOP ORDER THAT THE CHILD ORDER IS PART OF */

/* NOTICE THAT 'WITH' CAN BE USED WITH SELECT, DELETE, UPDATE AND CREATE */
/* IN, NOT IN, ANY, ALL ARE OPERATORS WITH IDENTICAL SYNTAX THAT ALLOW COMPARING A SINGLE VALUE WITH A SET/ARRAY/SUBQUERY */
/* FURTHERMORE, IN IS EQUIVALENT TO '= ANY' AND NOT IN IS EQUIVALENT TO '!= ALL' */

/* NOTE THAT CONTRARY TO OTHER FLAVOURS, POSTGRES ALLOWS FOR A UNION, RATHER THAN A UNION ALL IN THE RECURSIVE SUBQUERY */
/* IN FACT, WITHOUT THE 'ALL', THE ROWS WILL PER DEFAULT REPEAT AFTER EVERY ITERATION, LEADING TO UNINTUITIVE DUPLICATES */

WITH RECURSIVE parent_orders AS (
    
    SELECT
        1 AS counter,
        order_procedure_id AS order_tree,
        order_procedure_id AS original_order,
        order_parent_order_id AS parent_order
    FROM general_hospital.orders_procedures 

    WHERE 1 = 1
        AND order_parent_order_id IS NULL

    UNION

    SELECT
        parent_orders.counter + 1 AS counter,
        parent_orders.order_tree AS order_tree,
        general_hospital.orders_procedures.order_procedure_id AS original_order,
        parent_orders.original_order AS parent_order

    FROM general_hospital.orders_procedures
    INNER JOIN parent_orders
        ON 1 = 1
        AND parent_orders.original_order = general_hospital.orders_procedures.order_parent_order_id


)
SELECT *
FROM parent_orders

WHERE 1 = 1
    AND ( counter, order_tree ) IN ( 

        SELECT 
            MAX( counter ), 
            order_tree 
        FROM parent_orders 
        GROUP BY order_tree 


    )
ORDER BY
    order_tree
;

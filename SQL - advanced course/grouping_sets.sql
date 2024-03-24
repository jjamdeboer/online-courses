/* QUERY FOR PRACTICING GROUPING SETS */

/* GROUPING SETS CAN BE DONE WITH: GROUP BY GROUPING SETS( (set1), (set2), ... ) */
/* CUBE GENERATES ALL POSSIBLE SUBSETS: GROUP BY CUBE( column1, column2 ) == 
GROUPING SETS( (), ( column1 ), ( column2 ), ( column1, column2 ) ) */
/* ROLLUP GENERATES ALL HIERARCHICAL SUBSETS: GROUP BY ROLLUP( column1, column2 ) ==
GROUPING SETS( (), ( column1 ), ( column1, column2 ) ) */

SELECT
    COALESCE( state, 'All States' ) AS state,
    COALESCE( county, 'All Counties' ) AS county,
    COALESCE( city, 'All Cities' ) AS city,
    COUNT( * ) AS number_of_patients

FROM general_hospital.patients

WHERE 1 = 1
    AND state IS NOT NULL
    AND county IS NOT NULL
    AND city IS NOT NULL

GROUP BY ROLLUP( state, county, city )
/* THIS IS EQUIVALENT TO : */
/* GROUP BY GROUPING SETS(
    ( state ),
    ( state, county ),
    ()
) */

ORDER BY 
    state ASC NULLS FIRST, 
    county ASC NULLS FIRST,
    city ASC NULLS FIRST
;

/* SQL ALLOWS FOR STUDYING THE QUERY PLAN OF THE THING THAT IS EXECUTED
 * SYNTAX: EXPLAIN (ANALYZE) query;
 * THE ANALYZE KEYWORD WILL EXECUTE THE QUERY NEXT TO ANALYZING IT; WITHOUT IT, THE QUERY IS MERELY ANALYZED */

/* TO COPY DATA FROM/TO A TABLE PGADMIN CAN BE USED, OR THE COPY COMMAND
 * SYNTAX IS THE FOLLOWING: COPY query TO/table_name TO/FROM absolute_path ( WITH DELIMITER 'delimiter' ) ( CSV ) ( HEADER ); */

/* ARRAYS ARE ENCLOSED IN {} IN POSTGRES; USED FOR VARIABLE LENGTH VARIABLES
 * TO COMPARE TWO ARRAYS: @> OR <@ MEANS LEFT/RIGHT ARRAY IS CONTAINED IN RIGHT/LEFT ARRAY; && CHECKS 
 * INTERSECTION AND || CONCATENATES TWO ARRAYS; array_name[ index ] ACCESSES THE indexTH ELEMENT OF THE ARRAY
 * FURTHERMORE, THERE ARE SOME ARRAY-SPECIFIC FUNCTIONS, LIKE: UNNEST( array_name ), STRING_TO_ARRAY( string_name ), 
 * ARRAY_AGG( array_name ), ARRAY_TO_STRING( array_name ), ETC. */

/* EXTENSIONS/MODULES CAN BE INSTALLED TO PROVIDE ADDITIONAL FUNCTIONALITY
 * SYNTAX IS SUCH: CREATE EXTENSION IF NOT EXISTS extension_name SCHEMA schema_name;
 * EXAMPLES ARE: EARTHDISTANCE/POSTGIS (GEOSPATIAL EXTENSIONS), FUZZYSTRMATCH AND TABLEFUNC (PIVOT TABLES AND MORE) */

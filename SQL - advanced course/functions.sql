/* QUERY RETURNS A USER-DEFINED FUNCTION THAT CONCATENATES TWO STRINGS WITH A SPACE IN BETWEEN */

/* POSTGRES FACILITATES USER-DEFINED FUNCTIONS */
/* SYNTAX: CREATE [OR REPLACE] FUNCTION name_function( argument_name argument_data_type, ... ) 
    RETURNS return_data_types LANGUAGE plpgsql AS $$ DECLARE variables; BEGIN function_logic; END; $$; */

CREATE OR REPLACE FUNCTION general_hospital.add_strings( string1 varchar, string2 varchar )
    
    RETURNS varchar
    
    LANGUAGE plpgsql
    
    AS $$
    
        /* DECLARE AUXILARY VARIABLES HERE, USING: DECLARE variables variable_data_types */
        DECLARE
            durk varchar;
            murk varchar;
             
        BEGIN
            
            /* IF-THEN-ELSE-END IF; ARE ALLOWED IN PLPGSQL */
            SELECT COALESCE( string1, 'DURK' ) || ' ' || COALESCE( string2, 'MURK' ) INTO durk;
            SELECT '!?' INTO murk;
            RETURN durk || murk;
        
        
        END;
    
   
    $$
;

SELECT
    general_hospital.add_strings( primary_icd, admit_icd ) AS p_a_icd,
    primary_icd,
    admit_icd
FROM general_hospital.accounts
LIMIT 20
;

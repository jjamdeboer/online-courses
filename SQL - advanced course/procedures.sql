/* QUERY RETURNS A STORED PROCEDURE THAT CREATES A TABLE, INSERTS SOME VALUES AND DROPS IT, WITHIN A TRANSACTION */

/* STORED PROCEDURES ARE ACTUALLY MUCH THE SAME COMPARED TO FUNCTIONS IN POSTGRES, EXCEPT THAT 
NO RETURN TYPE IS NECESSARY AND MULTIPLE CRUD-STEPS ARE ALLOWED */
/* FURTHERMORE, ACTIVATION IS DONE USING: CALL procedure_name( parameters ); */
/* SINCE A PROCEDURE IS PERFORMED AS ONE BLOCK, ONE ERRONEOUS SUBSTEP ABORTS THE REST OF THE PROCEDURE */

CREATE OR REPLACE PROCEDURE general_hospital.create_and_drop_table( name_of_table VARCHAR )
    
    LANGUAGE plpgsql

    AS $$
    
    BEGIN
        
        /* NOTE THAT THE PROCEDURE CAN PERFORM MULTIPLE CRUDS */
        EXECUTE 'CREATE TABLE general_hospital.' || name_of_table || '( column1 SERIAL PRIMARY KEY )';
        EXECUTE 'INSERT INTO general_hospital.' || name_of_table || ' VALUES( DEFAULT )';
        EXECUTE 'INSERT INTO general_hospital.' || name_of_table || ' VALUES( DEFAULT )';
        EXECUTE 'INSERT INTO general_hospital.' || name_of_table || ' VALUES( DEFAULT )';
        EXECUTE 'INSERT INTO general_hospital.' || name_of_table || ' VALUES( DEFAULT )';
        EXECUTE 'INSERT INTO general_hospital.' || name_of_table || ' VALUES( DEFAULT )';
        EXECUTE 'INSERT INTO general_hospital.' || name_of_table || ' VALUES( DEFAULT )';
        EXECUTE 'INSERT INTO general_hospital.' || name_of_table || ' VALUES( DEFAULT, DEFAULT )';
        EXECUTE 'DROP TABLE general_hospital.' || name_of_table;
        ROLLBACK;

    
    END;

    $$
;

CALL general_hospital.create_and_drop_table( 'accounts' );
CALL general_hospital.create_and_drop_table( 'bills' );
CALL general_hospital.create_and_drop_table( 'encounters' );

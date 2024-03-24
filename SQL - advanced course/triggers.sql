/* QUERY TO UNDO DELETE ON THE ACCOUNTS TABLE */

/* A TRIGGER IS A SCRIPT THAT AUTOMATICALLY RUNS BEFORE/AFTER INSERT/UPDATE/DELETE-STATEMENTS */
/* SYNTAX: CREATE OR REPLACE TRIGGER trigger_name BEFORE/AFTER event_type ON table/view_name FOR 
EACH ROW/STATEMENT BEGIN trigger_logic END; */
/* THE DIFFERENCE BETWEEN ROW/STATEMENT IS THAT ROW TRIGGERS FOR EACH IMPACTED ROW (MIGHT BE 0) AND 
STATEMENT RUNS ONE TIME REGARDLESS OF NUMBER OF IMPACTED ROWS (MIGHT BE 0) */
/* A TRIGGER CAN BE ENABLED/DISABLED AS SUCH: ALTER TABLE table_name ENABLE/DISABLE TRIGGER trigger_name/ALL; */

/* FIRST CREATE A PROCEDURE/FUNCTION THAT CAN BE CALLED INSIDE THE TRIGGER */
/* TRIGGER FUNCTIONS DON'T TAKE INPUT AND DON'T RETURN ANYTHING */
CREATE OR REPLACE FUNCTION general_hospital.undo_function()
    
    RETURNS TRIGGER 
    LANGUAGE PLPGSQL
    
    AS $$
    BEGIN
        
            
        INSERT INTO general_hospital.accounts
        VALUES( 
            OLD.primary_icd,  
            OLD.admit_icd, 
            OLD.account_id, 
            OLD.primary_icd_procedure_cd, 
            OLD.primary_payor_id, 
            OLD.total_account_balance 
        );

        RETURN OLD;


    END;
    $$
;

/* HERE CREATE THE TRIGGER */
CREATE OR REPLACE TRIGGER undo_trigger
AFTER DELETE ON general_hospital.accounts 
FOR EACH ROW
EXECUTE PROCEDURE general_hospital.undo_function()
;

/* DISABLING THE TRIGGER */
ALTER TABLE general_hospital.accounts 
DISABLE TRIGGER undo_trigger
;

/* ENABLING THE TRIGGER */
ALTER TABLE general_hospital.accounts 
ENABLE TRIGGER undo_trigger
;

DELETE FROM general_hospital.accounts
WHERE account_id IN ( 11418957, 11418924 )
;

/* CHECKING WHETHER THE DELETE IS REWOUND */
SELECT *
FROM general_hospital.accounts
WHERE account_id IN ( 11418957, 11418924 )
; 

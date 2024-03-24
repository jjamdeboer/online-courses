/* QUERY FOR CALCULATING THE AVERAGE LENGTH OF STAY FOR A SPECIFIC OPERATING SURGEON AFTER A SURGERY */

SELECT
    surgery_id,
    surgical_discharge_date - surgical_admission_date AS length_of_stay,
    /* NOTE THAT ALIASES ARE, AGAIN, NOT ALLOWED IN POSTGRES */
    AVG( surgical_discharge_date - surgical_admission_date ) OVER surgeons::INTEGER AS average_length_of_stay,
    surgical_discharge_date - surgical_admission_date - AVG( surgical_discharge_date - surgical_admission_date ) OVER surgeons ::INTEGER AS compared_to_average
FROM general_hospital.surgical_encounters

/* NOTE HOW WINDOWS CAN BE USED TO SHORTEN WINDOW FUNCTIONS IN THE OVER-PART */
WINDOW
    surgeons AS ( PARTITION BY surgeon_id )
;

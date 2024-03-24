/*VARIABLE NUMBER OF ARGUMENTS FOR FUNCTIONS IS REFERRED TO AS VARYADIC FUNCTIONS, EXAMPLES ARE PRINTF, SCANF, ETC.*/
/*THE LIBRARY THAT PROVIDES THIS FLEXIBILITY IS 'stdarg.h'*/
/*THE MANDATORY ARGUMENTS COME FIRST, THE OPTIONAL ARGUMENTS COME AFTER, ONE MANDATORY ARGUMENT IS MANDATORY*/
/*SINCE THE NUMBER IS VARIABLE, ONE CANNOT USE NAMES FOR THEM; THIS PROBLEM CAN BE SOLVED WITH POINTERS*/
/*FOR CREATING A VARYADIC FUNCTION, THE ELLIPSIS '...' IS USED, WHICH SIGNIFIES A VARIABLE NUMBER OF ARGUMENTS (FOR EXAMPLE: 'int function( int durk, ... )')*/
/*WHAT IS IMPORTANT IS THE VARIABLE 'va_list' AND THE FUNCTION 'va_start'; INSIDE THE FUNCTION A VARIABLE OF TYPE 'va_list' NEEDS TO BE DECLARED AND THEN THAT ARGUMENT MUST BE GIVEN TO 'va_start', TOGETHER WITH THE LAST MANDATORY ARGUMENT AS TO INDICATE WHERE THE OPTIONAL PART STARTS; ALSO IT IS IMPORTANT TO USE THE FUNCTION 'va_arg', WHICH CAN BE USED TO LOOP THROUGH THE LIST OF VARIABLE ARGUMENTS WHERE THE FIRST ARGUMENT IS THE 'va_list'-VARIABLE AND THE SECOND IS THE TYPE OF VARIABLE; ANOTHER IMPORTANT FUNCTION TO USE IS 'va_end', WHICH RESETS THE 'va_list'-POINTER TO NULL, TAKING THE 'va_list'-VARIABLE AS AN ARGUMENT (FOR EXAMPLE: 'double function( int durk, ... ){ va_list varlist; va_start( varlist, durk ); double murk = va_arg( varlist, double ); va_end( varlist ); return murk; }')*/


/*RECURSION IS POSSIBLE IN C*/
/*RECURSION IS A FUNCTION THAT CALLS ITSELF IN C*/
/*TAIL RECURSION IS MOST EFFICIENT (WHERE THE RECURSION IS AT THE END OF THE FUNCTION), BUT IN GENERAL, RECURSION IS NOT EFFICIENT*/

/*A FUNCTION TAKES TIME TO CALL THE FUNCTION AND PASS THE ARGUMENTS; IN C99 THE CONCEPT OF INLINE FUNCTIONS WAS EVOKED TO GET FASTER ACCESS TO FUNCTIONS*/
/*THE IDEA IS THAT THE ORIGINAL FUNCTION IS REALLY REPLACED BY THE BODY OF THE FUNCTION, INSTEAD OF CALLING AND RETURNING FROM A FUNCTION*/
/*ADVICED IS TO ONLY USE THIS IF A FUNCTION IS CALLED INFREQUENTLY AND THE FUNCTION BODY IS SHORT*/
/*USAGE IS BY: 'inline [FUNCTION]'*/

/*USING A '_Noreturn'-FUNCTIONS/'noreturn'-FUNCTIONS EXITS THE OVERHEADING FUNCTION; 'exit()' IS AN EXAMPLE, IT EXITS THE MAIN-FUNCTION AND DOES NOT RETURN TO IT*/
/*FOR USING 'noreturn' INSTEAD OF '_Noreturn', THE 'stdnoreturn.h'-LIBRARY MUST BE INCLUDED*/

#include <stdio.h>
#include <stdarg.h>

double average( int i, int j, ... ){

        double sum = (double) i + (double) j;
        int counter = 2, interim;
        va_list varlist;

        va_start( varlist, j );

            while( ( interim = va_arg( varlist, int ) ) ){
                counter++;
                sum += (double) interim;
            }

        va_end( varlist );

        return sum/counter;


}

int factorial( int murk ){
    if( murk == 0 ){
        return 1;
    }
    return murk*factorial( murk - 1 );


}

int fibonacci( int n, int start_one, int start_two ){

    int sum = start_one + start_two;
    if( n == 0 ){
        return sum;
    }
    return fibonacci( n-1, start_two, sum );


}

int main( void ){

    int a = 4, b = 9, c = 7, d = 19, e = 4, f = 818;
    
    printf( "AVERAGE IS %e\n", average( a, b, c, d, e, f, 0 ) );
    printf( "AVERAGE IS %e\n", average( a, a, a, a, b, 0 ) );
    printf( "FACTORIAL OF 4 IS %d\n", factorial( 4 ) );
    printf( "FACTORIAL OF 7 IS %d\n", factorial( 7 ) );
    printf( "FIBONACCI OF 7 OF 0 AND 1: %i\n", fibonacci( 7, 0, 1 ) );
    printf( "FIBONACCI OF 7 OF 0 AND 1: %i\n", fibonacci( 10, 0, 1 ) );
    printf( "FIBONACCI OF 7 OF 0 AND 3: %i\n", fibonacci( 15, 0, 3 ) );

    return 0;


}

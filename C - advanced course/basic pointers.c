/*CHAIN OF POINTERS/MULTIPLE INDIRECTION IS BEING USED*/
/*A POINTER HAS ITS OWN ADDRESS, IT HOLDS AN ADDRESS AS VALUE AND THEN THE ADDRESS IT POINTS TO HAS A VALUE AS WELL*/
/*FOR DOUBLE POINTERS, THE SECOND VALUE IS AGAIN AN ADDRESS*/
/*DOUBLE POINTERS ARE INDICATED BY '**' BEFORE THE DOUBLE POINTER NAME; FOR DEREFERENCING, ALSO '**' NEEDS TO BE USED*/

/*USE CASES FOR DOUBLE POINTERS IS WHEN CHANGING THE VALUE OF A POINTER WHEN PASSED TO A FUNCTION*/
/*THIS TO SIMULATE PASS BY REFERENCE INSTEAD OF PASS BY COPY; GIVING THE POSSIBILITY OF CHANGING THE POINTER'S VALUE*/
/*THUS, FOR PRESERVING THE NEW VALUE OF THE POINTER OUTSIDE OF THE FUNCTION, USE DOUBLE POINTERS*/

/*FUNCTIONS THEMSELVES ALSO ARE STORED ON AN ADDRESS, AND CAN, THUS, BE POINTED TO (FUNCTION POINTERS)*/
/*FUNCTION POINTERS CAN BE USED WHEN MULTIPLE FUNCTION CAN BE CHOSEN FROM TO PERFORM A SIMILAR TASK ON DATA*/
/*DECLARING A FUNCTION POINTER IS LITTLE MORE COMPLICATED THEN A REGULAR POINTER, USE: '[RETURN TYPE] (* [POINTER NAME]) ([INPUT TYPE]) = & [FUNCTION WITH RIGHT CHARACTERISTICS]'*/
/*BEWARE OF THE BRACKETS!!! NORMALLY POINTERS ARE NOT THAT STRINGENT ON BRACKETS, BUT FUNCTION POINTERS ARE*/
/*CALLING THE FUNCTION CAN BE DONE WITH: '[POINTER NAME]( [VARIABLE PASSED INTO THE FUNCTION] )' OR '( *[POINTER NAME] )( [VARIABLE PASSED INTO THE FUNCTION] )', BOTH SYNTAXES ARE VALID*/
/*TYPEDEFS ARE VERY CONVENIENT FOR FUNCTION POINTERS, SINCE THE SYNTAX IS QUITE CUMBERSOME*/

/*VOID POINTERS ARE GENERIC POINTERS; THOSE POINTERS POINT SIMPLY TO ADDRESSES WITH THE SPECIFIED SIZE OF A CHARACTER (POINTER)*/
/*DECLARING CAN BE DONE WITH: '( void * )'*/
/*YOU CAN ASSIGN ANY POINTER TYPE TO A VOID POINTER*/
/*HOWEVER, VOID POINTERS CAN NEVER BE DIRECTLY DEREFERENCED, SINCE THERE IS NO TYPE TO DEREFERENCE IT TO*/
/*THEREFORE A CONCRETE CASTING MUST HAPPEN BEFORE DEREFENCING (FOR EXAMPLE: '*( * int ) voidpointer')*/


#include <stdio.h>
#include <malloc.h>

int function( double ** dpp ){

    double * durk = ( double * )malloc( sizeof( double ) );
    * durk = 3456.3456;
    
    * dpp = durk;

    return 0;
}

int function2( double ** dpp ){

    double * durk = ( double * )malloc( sizeof( double ) );
    * durk = 1.4*8*1e4*7e-2;
    
    * dpp = durk;

    return 0;
}


int ifunction( int durk ){
    return durk;
}

int ifunction2( int ( * durk )( double ** ) ){
    double * murk = NULL, durkudurk = 2.2211111;
    murk = & durkudurk;
    return ( * durk )( & murk );
}

int main( void ){

    int i = 1, j = 2, k = 3;
    int * p1 = & i, * p2 = & j;
    int ** ipp = & p1;

    printf( "POINTING AROUND: %i %i %i\n", ** ipp, * p1, * p2 );

    p1 = &k;

    printf( "POINTING AROUND: %i %i %i\n", ** ipp, * p1, * p2 );

    p1 = p2;

    printf( "POINTING AROUND: %i %i %i\n", ** ipp, * p1, * p2 );

    printf( "POINTING AROUND: %p %p %p\n", ipp, p1, p2 );

    double * murk = NULL, durk = 1.11111;
    murk = & durk;
    printf( "POINTING TO POINTER %e\n", * murk );
    function( & murk );
    printf( "POINTING TO POINTER %e\n", * murk );

    printf( "FUNCTION POINTER EXPERIMENT 1: %i\n", ifunction( function( & murk ) ) );
    int ( * pfunction )( double ** ) = & function;
    printf( "FUNCTION POINTER EXPERIMENT 2: %i\n", ifunction2( pfunction ) );
    ( *pfunction )( &murk );
    printf( "POINTING TO POINTER %e\n", * murk );
    /*NOTE THAT I CHANGE FUNCTION HERE, VERY EXCITING!*/
    pfunction = & function2;
    ( *pfunction )( &murk );
    printf( "POINTING TO POINTER %e\n", * murk );

    ipp = NULL, p1 = NULL, p2 = NULL, murk = NULL;
    free( ipp ), free( p1 ), free( p2 ), free( murk );

    return 0;


}

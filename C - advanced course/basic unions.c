/*UNION SIMILAR TO STRUCTURE, ALSO WITH MEMBERS*/
/*USED TO STORE DIFFERENT DATA TYPES TOGETHER; MEMBERS CAN BE ANY GIVEN DATA TYPE*/
/*ONLT ONE MEMBER CAN STORE A VALUE AT ANY GIVEN TIME, WHICH IS VERY DIFFERENT FROM STRUCTURES*/
/*FOR A STRUCTURE, MEMORY IS ALLOCATED FOR ALL ITS MEMBERS; FOR A UNION, MEMORY IS ALLOCATED FOR ITS LARGEST MEMBER, THE PROGRAMMER THEN DECIDES WHICH MEMBER TO ASSIGNE A VALUE*/
/*UNIONS ARE USED FOR MUTUALLY EXCLUSIVE DATA*/
/*FOR DEFINING A UNION, USE THE SAME CONSTRUCTION AS A STRUCTURE, EXCEPT USE 'union' INSTEAD OF 'struct': 'union [NAME] { [DATA TYPE MEMBER] [MEMBER NAME]; ... };'*/
/*NOTE THAT IF THE MEMBERS HAVE THE SAME DATA TYPE, DEREFERENCING, OR ACCESSING THE MEMBERS GIVES THE SAME VALUE FOR ALL THESE MEMBERS ONCE ONE OF THEM GOT A VALUE ASSIGNED TO IT*/


#include <stdio.h>

union Weight {
    float pound;
    int kilograms;
    int ouns;
};

int main( void ){

    union Weight durk;
    durk.ouns = 5;
    printf( "THE WEIGHT OF DURK IS %f\n", durk.pound );
    printf( "THE WEIGHT OF DURK IS %i\n", durk.kilograms );
    printf( "THE WEIGHT OF DURK IS %i\n", durk.ouns );
    union Weight * lead = &durk;
    lead -> kilograms = 1000;
    printf( "THE WEIGHT OF LEAD IS: %i\n", lead -> kilograms );
    union Weight * feather = &durk;
    ( *feather ).kilograms = 2;
    printf( "THE WEIGHT OF A FEATHER IS %i\n", ( *feather ).kilograms );
    printf( "THE WEIGHT OF DURK IS %f\n", durk.pound );
    printf( "THE WEIGHT OF DURK IS %i\n", durk.kilograms );
    printf( "THE WEIGHT OF DURK IS %i\n", durk.ouns );

    return 0;


}

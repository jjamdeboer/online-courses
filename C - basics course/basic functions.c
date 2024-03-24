/*A FUNCTION IS A SELF-CONTAINED UNIT OF CODE THAT ACCOMPLISHES A SPECIFIC TASK*/
/*SUBROUTINE OR PROCEDURES IN OTHER LANGUAGES ARE THE SAME AS FUNCTIONS IN C*/
/*COLLECTION OF FUNCTIONS IS A LIBRARY*/
/*SINCE MAINTANANCE IS THE MOST EXPENSIVE PART OF PROGRAMMING, FUNCTIONS ARE VERY USEFUL*/
/*DATA CAN BE PASSED TO A FUNCTION AND DATA CAN BE RETURNED BY A FUNCTION*/
/*MAIN-PART OF THE PROGRAM IS ALSO A FUNCTION IN C*/

/*FOR DEFINING FUNCTIONS: FUNCTION HEADER CONSISTS OF FUNCTION NAME, PARAMETERS WHERE DATA CAN BE PASSED INTO THE FUNCTION*/
/*FOR DEFINING: [RETURN DATA TYPE] [NAME OF THE FUNCTION] ([PARAMETER ONE], [PARAMETER TWO], ... ) { [FUNCTIONALITY] [RETURN THE RIGHT DATA TYPE] } (FOR EXAMPLE: int multiply (int x, int y) { return x*y }*/
/*IT IS ALSO POSSIBLE TO GIVE POINTERS OR STRUCTS AS PARAMETERS*/
/*IT IS POSSIBLE TO RETURN ENUMS/ENUMERATIONS AND POINTERS*/
/*C TRIES TO CONVERT DATA TYPES TO THE RETURN DATA TYPE AND GIVES AN ERROR WHEN THIS IS NOT POSSIBLE*/
/*IT IS NOT POSSIBLE IN C TO OVERWRITE RESERVED KEYWORDS AND IT IS NOT POSSIBLE TO HAVE TWO FUNCTIONS WITH THE SAME NAME (OVERLOADING)*/
/*THERE ARE THREE NAMING CONVENTIONS: UNDERSCORES FOR SPACES, CAMELCASE, PASCALCASE*/

/*FUNCTION PROTOTYPING IS SIMPLY DEFINING THE FUNCTION, WITHOUT SPECIFYING IT (SO, SIMPLY A FUNCTION HEADER). THIS IS USEFUL WHEN THE FUNCTION IS CALLED BEFORE IT IS BEING DEFINED (FOR EXAMPLE: int multiply (int x, int y)*/

/*THERE IS A SLIGHT DIFFERENCE BETWEEN PARAMETERS AND ARGUMENTS: FUNCTION DECLARATION IS DONE WITH PARAMETERS (PLACEHOLDERS), ARGUMENTS ARE SPECIFIC VALUES PUT INTO THE FUNCTION WHEN THE FUNCTION IS CALLED*/
/*PARAMETER NAMES ARE ONLY DEFINED WITHIN THAT FUNCTION; THERE IS LIMITED SCOPE FOR THAT PARAMETER*/

/*PROGRAM SCOPE IN C: ANY VARIABLE IN A CODE BLOCK (ANYTHING BETWEEN '{' '}') IS LOCAL, THE REST IS GLOBAL*/
/*IT IS POSSIBLE TO PERSIST VARIABLES (MAKE IT GLOBAL, ALTHOUG BEING INSIDE A CODE BLOCK) WITH THE 'static' KEYWORD*/
/*VARIABLES INSIDE A CODE BLOCK ARE AUTOMATICALLY LOCAL VARIABLES, WHICH CAN BE MADE EXPLICIT WITH THE KEYWORD 'auto', BUT THIS IS AUTOMATCALLY DONE BY COMPILER*/
/*NOTE THAT ALSO THE MAIN-BLOCK IS A FUNCTION, SO ALSO VARIABLES THERE ONLY HAVE SCOPE WITHIN MAIN, BUT THE OTHER FUNCTIONS WRITTEN DON'T HAVE ACCESS*/
/*LOCAL VARIABLES HAVE PRIORITY OVER GLOBAL VARIABLES (IN CASE OF USAGE OF THE SAME NAME)*/
/*TRY TO AVOID GLOBAL VARIABLES, DUE TO DEPENDENCIES BETWEEN FUNCTIONS*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//----------------------------------------------------------------
double absolute (double x){
    return ( (x < 0) ? -x :  x );
}

double squareroot(double x){
    return ( (x < 0) ? -1. : pow(x,.5) );
}

int greatest_common_divisor (int x, int y){
    int interim;
    if (x <= 0 || y <= 0){
        return -1;
    }
    while (x != 0){
        interim = y%x;
        y = x;
        x = interim;
    }
    return y;
}

//-------------------------------------------------------------------------------
/*TIC-TAC-TOE-FUNCTIONS:*/

void printscreen (char list[9], int player_turn){
    system("clear");
    printf("WELCOME TO A GAME OF TIC-TAC-TOE\n");
    printf("PLAYER 1: X, PLAYER 2: O\n");
    printf("IT IS PLAYER'S %i TURN, DO YOUR MOVE\n\n\n", player_turn);
    printf(" %c | %c | %c \n --------- \n %c | %c | %c \n --------- \n %c | %c | %c \n", list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8]);
    printf("\n\n\n");
}

int checkwin (char list[9]){

    return ((list[0] == list[1] && list[1] == list[2]) || (list[3] == list[4] && list[4] == list[5]) || (list[6] == list[7] && list[7] == list[8]) || (list[0] == list[3] && list[3] == list[6]) || (list[1] == list[4] && list[4] == list[7]) || (list[2] == list[5] && list[5] == list[8]) || (list[0] == list[4] && list[4] == list[8]) || (list[2] == list[4] && list[4] == list[6]) );

}

int checkvalidmove( char list[9], int number ){

    if ( number < 1 || number > 9 ) {
        printf("THAT'S NOT A VALID NUMBER!\n");
        return 0;
        }
    else if (list[number - 1] == 'X' || list[number - 1] == 'O'){
        printf("THAT IS NOT A VALID MOVE!\n");
        return 0;
    }

    return 1;

}

void doturn (char list[9], int player){
    
    int durk;
    
    do {
        scanf("%i", &durk);
    } while ( checkvalidmove (list, durk) == 0 );

    if (player == 1) {
        list[durk - 1] = 'X';
    }
    else {
        list[durk - 1] = 'O';
    }

}


//-------------------------------------------------------------------------------

int main (void){

    //-----------------------------------------------------------------------------
    printf("SQUARE ROOT OF 9, 0, -9: %e, %e, %e\n", squareroot(9.), squareroot(0), squareroot(-9.));
    printf("ABSOLUTE VALUE OF 9, 0, -9: %e, %e, %e\n", absolute(9.), absolute(0.), absolute(-9.));
    printf("GREATEST COMMON DIVISOR OF 65 AND 31, OF 0 AND 13, OF -9 AND 13: %i, %i, %i\n", greatest_common_divisor(65,31), greatest_common_divisor(0,13), greatest_common_divisor(-9,13));
    //-----------------------------------------------------------------------------

    int player_turn = 1;
    int number_of_turns = 0;
    char list[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};

    while (checkwin (list) == 0 && number_of_turns < 9){
        printscreen(list, player_turn);
        doturn(list, player_turn);
        player_turn = (player_turn == 1 ? 2 : 1);
        printscreen(list, player_turn);
        number_of_turns++;
    }
    if (checkwin (list)){
        player_turn = (player_turn == 1 ? 2 : 1);
        printf("THE GAME IS OVER, PLAYER %i WON!\n", player_turn);
    }
    else {
        printf("NO WINNER!\n");
    }

    //-----------------------------------------------------------------------------
    return 0;
}

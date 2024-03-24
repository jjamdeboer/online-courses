/*EXAMPLES OF CONTROL FLOW ARE: IF-THEN-ELSE, SWITCH, GOTO, FOR, WHILE, DO-WHILE, BREAK, CONTINUE, RETURN*/
/*CONTINUE STATEMENTS CAN BE USED TO SKIP THE REST OF THE BODY, BUT GO IMMEDIATELY TO THE NEXT ITERATION*/
/*BREAK, BREAKS OUT OF THE CURRENT LOOP*/

#include <time.h>
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
    int durk,murk;

    durk = 90;
    murk = 0;

    if(durk <= murk){
        printf("DUUUUUUUUUUUUUUUUUUURK\n");
    }
    else if (durk >= murk){
        printf("MUUUUUUUUUUURK\n");
    }
    else{
    printf("FLUUUUUUUUUUUURK!\n");
    }
    /*WHICH IS EQUAL TO (SHORTHAND EXPRESION FOR IF-ELSE STATEMENT):*/
    (durk <= murk) ? printf("DUUUUUUUUUURK\n") : printf("MUUUUUUUUUUUUUUUUUURK\n");
    /*GREAT FOR EXPRESSIONS OF THE FORM: int x = ([BOOLEAN EXPRESSION] ? [VALUE ONE] : [VALUE TWO])*/

    /*SIMILAR TO IF-THEN-ELSE STATEMENTS IS THE SWITCH:*/
    switch (murk*durk){
    case 1:
        printf("DUUUUUUUUUUUUUURK\n");
        printf("DUURKDURK\n");
        printf("DURK\n");
        break;
    case 5:
        printf("MUUUUUUUUUUUUUUUUUUUUUUUUUUURK!!!\n");
        printf("MUURKUMURK\n");
        break;
    default:
        printf("MUUUUUUUUUUUUUUUUUUUUUUUUUUUURKUDUUUUUUUUUUUUUUUUUUUUUURK!!!!\n");
        printf("DURK!\n");
    }

    /*SYNTAX FOR FOR AND WHILE-LOOP (OPERATIONALLY THE SAME, DIFFERENT SYNTAX):*/
    for (durk = 0, murk = 10; durk <= 10, murk > 0; durk++, --murk){
        printf("PRINTING DURK AND MURK: %i %i ", durk, murk);
    }    
    printf("\n");
    while (murk <= 1e9){
        murk += murk + 1;
        murk *= murk + 1;
        printf("MUUUUUUUUUUUUUUUUUUUUUUUUUUUURK!!!");
    }
    printf("\n");
    
    srand(time(NULL));
    int random = rand() % 21;
    printf("RANDOM %i\n", random);

    printf("THIS IS A GAME, GUESS THE NUMBER BETWEEN 0 AND 20\n");
    printf("YOU HAVE 5 GUESSES TO START!\n");
    for(durk = 5, scanf("%i", &murk); murk != random; scanf("%i", &murk), --durk){
        if (murk < 0 || murk > 20){
            printf("THAT'S NOT A NUMBER BETWEEN 0 AND 20!\n");
            durk += 1;
            continue;
        }
        else if (murk < random){
            printf("MY NUMBER IS HIGHER!\n");
        }
        else {
            printf("MY NUMBER IS LOWER!\n");
        }

        printf("YOU HAVE %i GUESSES LEFT!\n", durk - 1);

        if (durk == 1){
            printf("YOU'VE LOST!\n");
            return 0;
        }

    }
    printf("YOU'VE WOOOOOOOOOOOOOOOOOOOOON!!!\n");


    return 0;
}

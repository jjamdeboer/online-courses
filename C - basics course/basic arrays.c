/*ARRAYS ARE A COLLECTION OF VARIABLES (A LIST OF POINTERS)*/
/*ARRAYS ARE OF FIXED SIZE AND OF A SINGLE DATA TYPE (IT HOLDS ONLY INTEGERS, FOR EXAMPLES)*/
/*THE ITEMS IN AN ARRAY ARE CALLED ELEMENTS*/
/*FOR ARRAY DECLARATIONS: '[DATA TYPE] [VARIABLE NAME][[SIZE OF ARRAY]]' (FOR EXAMPLE: 'int durk[10]')*/
/*VARIABLES CAN BE USED TO SPECIFY THE LENGTH OF AN ARRAY (FOR EXAMPLE: 'int durk[MURK]')*/
/*AN OUT OF BOUND ERROR IS NOT FILTERED OUT BY THE COMPILER*/

/*TO ENTER AN ELEMENT, USE '[VARIABLE NAME][[INDEX OF ELEMENT, STARTING FROM 0]]' (FOR EXAMPLE: 'durk[0]')*/
/*ANOTHER WAY TO ENTER VALUES IS TO USE: [VARIABLE NAME] = {[ARRAY VALUES]} (FOR EXAMPLE: 'durk = { 0, 0, 9, 11, 0 }')*/
/*EVEN, ANOTHER WAY IS TO USE INDEX NUMBERS: [VARIABLE NAME] = {[[ELEMENT INDEX]] = [ELEMENT VALUE]} (FOR EXAMPLE: 'durk = {[2] = 5, [0] = 7}')*/
/*ELEMENTS THAT ARE NOT INITIALIZED, ARE AUTOMATICALLY SET TO 0 (ALTHOUGH GOOD TO ALSO DO THIS MANUALLY, TO BE SURE NO RANDOM MEMORY IS STORED IN THE ARRAY)*/

/*ARRAYS CAN ALSO HOLD ARRAYS, SO NESTED ARRAYS OR MULTIDIMENSIONAL ARRAYS*/
/*GETTING A VALUE FROM THIS ARRAYS HAS SYNTAX: '[VARIABLE NAME][[FIRST INDEX]][[SECOND INDEX]][[THIRD INDEX]]' (FOR EXAMPLE: 'murk[12][3][7]')*/

#include <stdio.h>

int main(void)
{
    int supremum = 1000;
    int prime_array_size = 200;
    int primes[prime_array_size]; 
    primes[0] = 2; 
    primes[1] = 3;
    int new_index = 2;

    for (int i = 4; i < supremum; i++){
        for (int j = 0; j < new_index; j++){
            if (i%primes[j] == 0){
                break;
            }
            else if (j == new_index - 1){
                primes[new_index] = i;
                new_index += 1;
            }
        }
    }

    for (int i = 0; i < new_index; i++){
        printf("PRIME NUMBERS TO %i ARE: %i\n", supremum, primes[i]);
    }

    return 0;
}

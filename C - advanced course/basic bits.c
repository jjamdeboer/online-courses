/*A BYTE IS EIGHT BITS*/
/*LEFTMOST BIT IS THE HIGHEST ORDER BIT*/
/*SETTING THE BIT IS MAKING IT 1, RESETTING IT IS MAKING IT 0*/

/*FOR NEGATIVE NUMBERS, THE CALCULATION IS A LITTLE DIFFERENT FROM SIMPLY ADDING POWERS OF TWO; CONVERTING FROM DECIMAL TO BINARY: ADD 1, EXPRESS THE POSITIVE EQUIVALENT OF THAT NUMBER IN NORMAL BINARY EXPRESSION, REVERT ALL THE BIT (FOR EXAMPLE: -5 -> -4 -> 00000100 -> 11111011); CONVERTING FROM BINARY TO DECIMAL, REVERT ALL THE BITS, READ OUT THE RESULTING POSITIVE NUMBER IN DECIMAL FORM AND SUBTRACT ONE (FOR EXAMPLE: 11100110 -> 00011001 -> 25 -> 24)*/

/*LOGICAL BIT MANIPULATION OPERATORS ARE: |, &, ^, ~*/
/*REASON FOR USING THESE OPERATIONS IS BECAUSE THESE ARE FASTEST OF ALL OPERATIONS*/
/*THE '|' COPIES THE BIT IF IT EXISTS IN EITHER OPERAND; THE '&' COPIES THE BIT IF IT EXISTS IN BOTH OPERANDS; THE '^' COPIES THE BIT IF IT EXISTS IN EITHER OPERAND (NOT BOTH); THE '~' FLIPS ALL THE BITS IN THE OPERAND*/
/*LOGICAL BIT MANIPULATIONS CAN BE PERFORMED ON ALL FORMS INTEGERS AND CHARACTERS (WHICH ARE ALSO INTEGERS), BUT NOT FLOATS*/
/*SHIFTING MANIPULATION OPERATORS ARE: <<, >>*/
/*THE '<<' SHIFTS THE BITS OF THE LEFT OPERAND TO THE LEFT BY THE NUMBER OF SPACES SPECIFIED WITH THE SECOND OPERAND; THE '>>' SHIFTS THE BITS OF THE LEFT OPERAND TO THE RIGHT BY THE NUMBER OF SPACES SPECIFIED WITH THE SECOND OPERAND*/
/*FOR BOTH THESE OPERATORS, THE VACATED BITS ARE SET TO 0, WITH THE SIGNED CASE A LITTLE LESS STRAIGHTFORWARD*/

#include <stdio.h>
#include <math.h>

int bit_to_decimal ( long long bit ){

    int counter = 0;
    long long decimal = 0;

    while ( bit ){

        if ( bit % 2 == 0 ){
            bit /= 10;
        }    
        else {
            bit = (bit - 1)/10;
            decimal += (long long) pow( 2., (double) counter );
        }

        counter++;

    }

    return decimal;


}

long long decimal_to_bit ( int decimal ){

    int counter = 0;
    long long bit = 0;

    for ( ; pow( 2., (double) counter) <= decimal; counter++ );

    while ( decimal ){

        if ( (int) pow( 2., (double) counter ) > decimal ){
        }
        else {
            decimal -= (int) pow( 2., (double) counter );
            bit += (long long) pow( 10., (double) counter );
        }
        counter--;

    }

    return bit;


}

int binary_to_decimal ( long long binary ){
    
    int decimal = 0;
    int counter = 0;

    while ( binary ){
        
        if ( binary & 1 ){
            decimal |= ( 1 << counter );
        }

        counter++;
        binary /= 10;

    }

    return decimal;

}


long long decimal_to_binary ( int decimal ){

    long long binary = 0;
    int counter = 0;

    while ( decimal ){
        
        if ( decimal & 1 ){
            binary += pow( 10, counter );    
        }

        counter++;
        decimal >>= 1;

    }

    return binary;


}

int main ( void ){

    printf("BIT TO DECIMAL FOR 0, 1, 01, 10, 11, 11011: %i, %i, %i, %i, %i, %i\n", bit_to_decimal(0), bit_to_decimal(1), bit_to_decimal(01), bit_to_decimal(10), bit_to_decimal(11), bit_to_decimal(11011));
   printf("DECIMAL TO BIT FOR 0, 1, 2, 32, 50, 127: %lli, %lli, %lli, %lli, %lli, %lli\n", decimal_to_bit(0), decimal_to_bit(1), decimal_to_bit(2), decimal_to_bit(32), decimal_to_bit(50), decimal_to_bit(127)); 

    printf("EXPERIMENTING WITH BITS: 15&127, 16|128, 15^127, ~127: %i, %i, %i, %i\n", 15&127, 16|128, 15^127, ~127);
    printf("EXPERIMENTING WITH BITS: 15<<2, 15>>2, 127<<1, 127>>1: %i, %i, %i, %i\n", 15<<2, 15>>2, 127<<1, 127>>1);
    
    printf("BIT TO DECIMAL FOR 0, 1, 01, 10, 11, 11011: %i, %i, %i, %i, %i, %i\n", binary_to_decimal(0), binary_to_decimal(1), binary_to_decimal(01), binary_to_decimal(10), binary_to_decimal(11), binary_to_decimal(11011));
    printf("DECIMAL TO BIT FOR 0, 1, 2, 32, 50, 127: %lli, %lli, %lli, %lli, %lli, %lli\n", decimal_to_binary(0), decimal_to_binary(1), decimal_to_binary(2), decimal_to_binary(32), decimal_to_binary(50), decimal_to_binary(127)); 

    printf("ENTER A NUMBER AND A BIT TO SET:\n");
    int number, bit;
    scanf( "%i", &number );
    scanf( "%i", &bit );
    printf("THE NUMBER WAS: %i, THE %iTH BIT WAS SET, RESULTING IN %i\n", number, bit, number | ( 1 << bit ) );

    return 0;


}

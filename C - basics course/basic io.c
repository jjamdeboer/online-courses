/*PROGRAMS STORE DATA IN MEMORY, BUT ONLY TEMPORARILY; FILES CAN MAKE THIS DATA PERSISTENT AND ARE STORED ON HARD DRIVES, RATHER THAN MAIN MEMORY/RAM*/
/*A FILE IS A SEQUENCE OF BYTES, THEREFORE A FILE IS OPENED AND THEIR IS A CURRENT 'POINTER', POINTING TO THE FIRST BYTE; THERE IS ALSO A CURRENT POSITION, WHICH IS DEFINED WITH RESPECT TO THE BEGINNING BYTE*/
/*TWO KIND OF FILES: TEXT AND BINARIES (MUSIC, IMAGES, WHERE BYTES ARE WRITTEN 'DIRECTLY' TO MEMORY)*/

/*C ALSO WORKS WITH STANDARD INPUT, OUTPUT AND ERROR; INPUT GENERALLY KEYBOARD, BUT CAN BE FILE AS WELL; THESE THREE 'CHANNELS' ARE CALLED 'STREAMS' IN C*/
/*STANDARD INPUT IN C ~ 'scanf()' AND OTHER FUNCTIONS; STANDARD OUTPUT ~ 'printf()' AND OTHER FUNCTIONS*/
/*FILE ACCESSING GOES THROUGH A FILE/STREAM POINTER*/
/*A FILE POINTER, POINTS TO A STRUCTURE NAMED 'FILE', WHICH CONTAINS MEMBERS FOR THE ACTION (READ/WRITE/UPDATING THE FILE), ADDRESS FOR THE BUFFER IN MEMORY USED FOR PERFORMING THE ACTIONS, CURRENT POSITION OF THE STREAM POINTER IN THE FILE*/
/*WHEN WORKING WITH DIFFERENT FILES, A DIFFERENT STREAM AND POINTER HAS TO BE OPENED FOR ALL THOSE FILES; THERE IS A MAXIMUM NUMBER OF POSSIBLE FILE STREAMS, 'FOPEN_MAX' IN THE 'stdio.h'-FILE*/
/*HOWEVER, SINCE ACCESSING FILES IS AN EXPENSIVE OPERATION, SINCE HARD DRIVES ARE GENERALLY SLOW, IT IS HIGHLY RECOMMENDED NOT TO DO THIS OFTEN OR SIMULTANEOUSLY*/

/*OPENING A FILE CAN BE DONE WITH 'fopen("[PATH TO FILE]", [MODE OF OPERATION: "w", "r", "a", "w+", "r+", "a+"])', WHICH CREATES A POINTER TO THAT FILE*/
/*THUS, AS A DEFINITION: 'FILE * fopen([FILENAME], [MODE])'*/
/*IF THE FILE CAN OPEN 'fopen()' RETURNS A POINTER, OTHERWISE IT RETURNS NULL*/
/*OPERATIONS ARE OVERWRITING THE FILE ("w" AND "w+"), APPENDING TO A FILE ("a" AND "a+") AND READING A FILE ("r" AND "r+"); READ AND WRITE ARE "w+" AND "r+"*/
/*FOR CLOSING A FILE, USE: 'fclose([POINTER TO THE FILE])', WHICH RETURNS AN INTEGER*/

/*FOR RENAMING FILES, USE: 'rename("[OLD FILENAME]", "[NEW FILENAME]")', WHICH RETURNS AN INTEGER (0 ON SUCCESS)*/
/*FOR DELETING THE FILE, USE: 'remove("[FILENAME]")', WHICH RETURNS AN INTEGER*/
/*FOR RETURNING THE INTEGER VALUE OF THE CHARACTER READ AND SLIDING THE POINTER UP ONE POSITION, USE: 'fgetc([POINTER TO THE FILE])'*/
/*FOR RETURNING THE POINTER TO THE BEGINING OF THE FILE, USE: 'rewind([POINTER TO THE FILE])'*/
/*NOTE THAT 'EOF' IS A SPECIAL CHARACTER THAT DESIGNATES THE END OF FILE*/
/*FOR WRITING TO A FILE, USE: 'fputs([STRING OR CHARACTER POINTER], [POINTER TO THE FILE])', OR: 'fprintf([POINTER TO THE FILE], [STRINGS OR IDENTIFIERS], [CONSTANTS REFERENCED IN THE IDENTIFIERS])'*/

/*THERE ARE TWO ASPECTS OF FILE POSITIONING: OBTAINING CURRENT POSITION AND MOVING CURSOR TO GIVEN POSITION*/
/*FOR OBTAINING CURRENT POSITION, USE: 'ftell([POINTER TO FILE])' WHICH RETURNS A LONG, THE NUMBER RELATIVE TO THE BEGINNING OF THE FILE*/
/*FOR MOVING THE POINTER TO ANOTHER POSITION, USE: 'fseek([POINTER TO FILE], [LONG INTEGER FOR OFFSET WITH RESPECT TO BEGIN], [INTEGER WHICH NEEDS TO BE USED AS STARTING POINT, CAN BE EITHER 'SEEK_SET' (BEGINNING FILE), 'SEEK_CURRENT' (...) OR 'SEEK_END' (...)])'*/

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <ctype.h>

int main (void){

    FILE * filepointer;
    int integer;
    int linecounter = 0;
    int charactercounter = 1;

    filepointer = fopen("basicio.txt","r");
    if (!filepointer) {
        printf ("WHHHHHHHHHHHHHHHHHHHATTATATATATAATTAAAAAAAAAAAAT!!!!\n");
        return 1;
    }

    printf("OPENED THE FILE\n");
    printf("HERE ALL SEEK PARAMETERS: %i, %i, %i\n", SEEK_SET, SEEK_CUR, SEEK_END);
    
    /*COUNT THE NUMBER OF LINES IN A FILE:*/
    while ((integer = fgetc(filepointer)) != EOF){
        if (integer == (int) '\n'){
            linecounter++;
        }
        printf( "%c", tolower( integer ) );
    }
    printf("\n");
    printf("NUMBER OF LINES IN THE FILE ARE: %i\n", linecounter);
    printf("CURRENT POSITION: %ld\n", ftell(filepointer));
    rewind( filepointer );
    printf("CURRENT POSITION: %ld\n", ftell(filepointer));
    fseek( filepointer, 100, SEEK_SET );
    printf("CURRENT POSITION: %ld\n", ftell(filepointer));

    /*REVERSE THE CHARACTERS OF THE FILE:*/
    fseek ( filepointer, -1, SEEK_END );
    while ( ftell(filepointer) != 0 && (integer = fgetc(filepointer)) != EOF ){
        printf( "%c", integer );
        charactercounter++;
        fseek ( filepointer, -charactercounter, SEEK_END );
    }
    printf( "%c\n", fgetc(filepointer));

    printf("CLOSING THE FILE WAS SUCCESSFUL: %i\n", fclose(filepointer));
    printf("RENAMING THE FILE SUCCESFULL: %i\n", rename("basicio.txt", "basicio.txt"));

    filepointer = fopen("basicio.txt","a+");
    if (!filepointer) {
        printf ("WHHHHHHHHHHHHHHHHHHHATTATATATATAATTAAAAAAAAAAAAT!!!!\n");
        return 1;
    }

    printf("OPENED THE FILE\n");

    /*APPEND SOMETHING TO THE FILE:*/
    printf("WRITING WAS SUCCESSFUL: %i\n", fputs("DURKUDURKUDURK!!!DURKDURKDURK!\n", filepointer));
    printf("WRITING WAS SUCCESSFUL: %i\n", fprintf(filepointer, "DURKUDURKUDURK!!!DURKDURKDURK! %i\n", 42));
    printf("CLOSING THE FILE WAS SUCCESSFUL: %i\n", fclose(filepointer));

    return 0;


}

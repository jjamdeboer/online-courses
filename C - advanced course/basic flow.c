/*THE GOTO-STATEMENT CHANGES THE LOCATION OF EXECUTION TO A VERY SPECIFIC LOCATION IN THE FILES*/
/*TO IDENTIFY THE PLACE TO JUMP TO, A LABEL IS NEEDED. FOR DECLARING A LABEL, USE: 'goto [NAME]; [NAME]: [STATEMENT]'*/
/*THE GOTO-STATEMENT MUST APPEAR IN THE SAME BLOCK AS THE LABEL*/
/*GOTO-STATEMENTS SHOULD BE AVOIDED, SINCE THEY ARE IMPOSSIBLE TO TRACE THE EXECUTION PATH*/
/*CONTINUE AND BREAK ARE SPECIALIZED FORMS OF GOTO-STATEMENTS, HOWEVER THEY ARE VERY EASY TO FOLLOW*/

/*THE NULL-STATEMENT IS FOR EXPRESSIONS THAT HAVE NO CONTENT YET, AS PLACEHOLDER. SYNTAX, USE: 'if ([EXPRESSION]) { ; }'; USE A SOLITARY ';'*/
/*NULL POINTER IS A POINTER THAT POINTS TO NOTHING ( == 0 ), NULL TERMINATOR FOR STRINGS IS THE CHARACTER THAT FINISHES A STRING ( == '\0' == 0 ); THIS SHOULD NOT BE CONFUSED WITH THE NULL-STATEMENT, WHICH IS A SINGLE ';'*/
/*IT IS NECESSARY ALSO IF ALL THE LOGIC OF THE LOOP IS INSIDE THE WHILE- OR FOR-LOOP, SO NO BODY IS NEEDED; WITH THE NULL-STATEMENT THIS CAN BE AVOIDED*/

/*THE COMMA-OPERATOR IS QUITE CONVENIENT, WHEN EXPRESSIONS ARE RELATED, BUT NOT THE SAME: IT DISCARDS THE RESULT OF THE FIRST EXPRESSION AND RETURNS THE RESULT OF THE SECOND EXPRESSION*/
/*THE COMMA-SEPARATOR CAN BE USEFUL FOR CONSTRUCTIONS LIKE: '[VARIABLE TYPE] [VARIABLE NAME] = ([FIRST DO THIS/CHANGE STATE/PRINTF THIS, OF WHICH RESULT IS NOT IMPORTANT], [THE EXPRESSION THAT MATTERS])'*/
/*NOTE THAT THE COMMA IS, THUS, ACTUALLY AN OPERATOR IN C, THAT CAN COME IN HANDY WHEN FIRST AN OPERATION NEEDS TO BE PERFORMED BEFORE A FINAL ACTION, OR WHEN ACTIONS NEED TO BE LOGICALLY GROUPED TOGETHER*/
/*THE SEPARATOR IS NOT AN OPERATOR, IT HAS THE SAME SYMBOL IS USED DIFFERENTLY*/

/*REGULAR CONTROL FLOW ONLY DEALS WITH FOR-, WHILE-, DO-WHILE-LOOPS AND COMMA-OPERATORS AND GOTO-STATEMENTS*/
/*THERE EXIST OTHER FUNCTIONS: 'setjmp()' AND 'longjmp()', MAINLY USED FOR TRY-CATCH-CONSTRUCTIONS IN C*/
/*THE HEADER FILE 'setjmp.h' NEEDS TO BE INCLUDED IN ORDER FOR THESE FUNCTION TO WORK*/
/*THE GOTO CAN ONLY JUMP TO A POSITION IN THE SAME FUNCTION, HOWEVER LONGJUMP CAN EVEN JUMP OUT OF CURRENT FUNCTION, BASICALLY TO ANYWHERE*/
/*A LONGJUMP IS ONLY PERMITTED TO A POINT THAT HAS ALREADY BEEN AND ONE THAT STILL HAS LIVE ACTIVATION RECORD*/
/*SO SETJUMP IS MORE 'RETURN TO' THAN A 'GO TO'*/

#include <setjmp.h>
#include <stdio.h>

int main( void ){

    int depth;
    int i;
    int j; (printf("GIVE ME A NUMBER:"), scanf("%i", &j), printf("VALUE JUST ENTERED: %i\n", j));

    printf("ENTER THE DEPTH OF THE TREE:");
    scanf("%i", &depth);


    return 0;
}

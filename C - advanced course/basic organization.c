/*MODULAR CODING IS IMPORTANT*/
/*HOW TO INCLUDE OTHER FILES WHEN COMPILING IS BY REFERENCING THE HEADER FILE, WHERE THE FUNCTION IS DEFINED (AND MAYBE COMPLETELY GIVEN, FOR SMALL FUNCTIONS), AND THEN HAVING A FILE WITH THE SAME NAME AS THE HEADER FILE, WITH THE C-EXTENSION, THAT IS COMPILED TOGETHER WITH THE ORIGINAL FILE (FOR EXAMPLE: THERE ARE 'main.c', 'randomfunctions.h' (WHERE THE DEFINITIONS ARE) AND 'randomfunctions.c' (WHERE THESE FUNCTIONS ARE DETAILED); FOR RUNNING HAVE A #include "randomfunctions.h" ON TOP OF THE MAIN-FILE (WHERE "" MEANS THAT THE HEADER FILE IS IN CURRENT DIRECTORY) AND USE 'gcc main.c randomfunctions.c -o output' FOR COMPILING. THIS GOES WELL SINCE THE 'main'-FUNCTION IS THE MOST IMPORTANT POINT IN C-PROGRAMS, SO COMPILING MULTIPLE C-FILES TOGETHER DOES NOT GIVE ANY PROBLEMS)*/
/*AGAIN, TO MAKE ALL PROGRAMS PART OF THE SAME COMPILE-OPERATION, INCLUDE ALL THESE C-PROGRAMS IN THE COMPILE-COMMAND (FOR EXAMPE: 'gcc main.c durk.c murk.c -o durkudurk')*/

/*IT IS ALSO POSSIBLE TO CREATE AN OVERVIEW OF ALL THE FILES AND ALL THEIR DEPENDENCIES IN A MAKEFILE*/
/*THE ADVANTAGE OF USING MAKEFILES, IS THAT IT KEEPS OBJECTS (THAT ARE CREATED AFTER COMPILING, WHICH ARE LINKED TOGETHER TO CREATE THE EXECUTABLE), SO THAT WHEN AN ERROR OCCURS DURING COMPILATION, IT ONLY NEEDS TO RERUN EVERYHTING THAT COMES AFTER THAT BREAKPOINT (SINCE EVERYTHING BEFORE WAS ALREADY COMPILED)*/
/*THE MAKEFILE/MAKE-UTILITY RECOGNIZES WHAT NEEDS REVISION BASED ON ADAPTION DATES/TIMES OF SOURCE FILES: IF OBJECTS ARE OLDER THAN LATEST VERSION OF THE SOURCE FILE, MAKE WILL RECOMPILE THAT FILE AGAIN WHEN CALLED*/
/*CALLING MAKE IS SIMPLY WITH 'make', WHICH WILL AUTOMATICALLY SEARCH FOR A MAKEFILE*/
/*MAKEFILES ARE NOT SPECIFICALLY LINKED TO C, BUT AN EXTERNAL PARTY TO MANAGE BIGGER PROJECTS*/

/*THERE IS A DIFFERENCE BETWEEN STATIC AND EXTERNAL GLOBAL DATA: STATIC IS LOCAL TO THE FILE IT IS DEFINED IN, EXTERNAL MAKES IT POSSIBLE TO SHARE GLOBAL DATA BETWEEN FILES (KEYWORDS ARE REALLY 'static' AND 'extern')*/

/*THERE ARE THREE FORMS OF MEMORY WITHIN A PROGRAM: STATIC, STACK AND HEAP MEMORY*/
/*STATIC MEMORY PERSISTS FOR THE EXISTENCE OF THE PROGRAM (USED FOR, FOR EXAMPLE, GLOBAL VARIABLES)*/
/*STACK MEMORY IS ONLY LOCAL TO FUNCTIONS AND LOOPS (SO ONLY LOCALLY AVAILABLE); THE STACK DOES NOT NEED TO BE MANAGED, BUT THE STACK HAS A MAXIMUM SIZE, SO STACK OVERFLOW MIGHT OCCUR WHEN LOCAL MEMORY EXCEEDS THOSE BOUNDS*/
/*HEAP MEMORY CAN BE DYNAMICALLY ALLOCATED AND MANAGED; DOES NOT PER SE PERSIST THROUGHOUT THE PROGRAM, NOT PER SE NOT*/
/*USE HEAP WHEN SIZE OF VARIABLE CAN CHANGE (AS IN ARRAYS) OR WHEN VARIABLE NEEDS TO BE REUSED THROUGHOUT THE PROGRAM; USE THE STACK FOR SMALL VARIABLES THAT ARE ONLY USED LOCALLY AND DON'T NEED ANY FORM OF PERSISTENCE*/
/*VARIABLES CANNOT BE REALLOCATED OR FREED IN THE STACK*/
/*STACK IS SLIGHTLY FASTER THEN HEAP (CPU VERSUS RAM)*/

/*NOTE THAT BLOCKS CAN BE CREATED ANYWHERE, WITHOUT AN EXPLICIT LOOP OR FUNCTION BEING CALLED*/
/*THERE ARE DIFFERENT STORAGE CLASSES (REFERRING TO SCOPE, VISIBILITY AND LIFETIME OF VARIABLES) IN C: AUTOMATIC VARIABLES, EXTERNAL, STATIC AND REGISTER*/
/*AUTOMATIC (KEYWORD: 'auto') ARE FOR VARIABLES THAT ARE ONLY DEFINED WITHIN A BLOCK OF CODE (CODE BETWEEN '{' AND '}'); LOCAL VARIABLES (THIS TYPE IS THE DEFAULT FOR ANY DECLARATION)*/
/*AN AUTOMATIC VARIABLE OUTSIDE ANY BLOCK IS ALSO DEFINED EVERYWHERE, SO ALSO EXTERNAL TO CURRENT PROGRAM, SO THESE CAN BE CALLED IN OTHER FILES AS WELL (WITH THE KEYWORD: 'extern')*/
/*STATIC VARIABLES ARE DEFINED THROUGHOUT CURRENT FILE, BUT ONLY CURRENT FILE (SINCE FILES ARE COMPILED INDEPENDENTLY), TO AVOID EXTERNAL DATA OR MAKE DATA PERSIST OUTSIDE OF BLOCKS (KEYWORD: 'static')*/
/*REGISTER MEMORY IS USED FOR VARIABLES WHICH ARE NORMALLY PUT IN RAM (VARIABLES ON THE HEAP), BUT NEED REGULAR ACCESS, CAN BE MOVED TO CPU/REGISTERS; POINTERS CANNOT BE USED AND THE SIZE IS RESTRICTED BY SIZE OF REGISTERS (KEYWORD: 'register')*/
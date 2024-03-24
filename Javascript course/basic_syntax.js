// GENERAL:
// ALWAYS END YOUR LINES WITH SEMICOLON IN JAVASCRIPT
// JAVASCRIPT IS OBJECT ORIENTED 
// JAVASCRIPT (DYNAMIC EFFECTS/VERBS), TOGETHER WITH HTML (CONTENT/NOUNS) AND CSS (AESTHETICS/ADJECTIVES), IS THE CORE TECHNOLOGY IN WEBSITE DISPLAY
// REACT AND ANGULAR BASED ON JAVASCRIPT
// TRADITIONALLY ONLY USED CLIENT-SIDE, BUT WITH NODE.JS CAN ALSO BE USED SERVER-SIDE
// DON'T REPEAT YOURSELF-PRINCIPLE (DRY) ALSO VALID IN JAVASCRIPT
// VERSIONS:
// ECMASCRIPT IS LANGUAGE STANDARD, JAVASCRIPT A CONCRETE EXAMPLE OF THIS STANDARD, BUT THEY ARE PREDOMINANT NOW, SO BECAME ALMOST INTERCHANGEABLE
// ES5 RELEASED IN 2009 WAS A BIG THING AND THIS VERSION IS NOWADAYS ALWAYS INTEGRATED IN EVERY WEB BROWSER, EVEN THE OLD ONES
// IN 2015, ES6/ES2015 WAS RELEASED, WITH A GIGANTIC UPDATE. TO PREVENT SUCH A HUGE UPDATE IN THE FUTURE, THE LANGUAGE IS NOW UPDATED EVERY YEAR IN SMALL BITS (ES7/ES2016 ETC.). THE NEW VERSIONS ARE NOT ACCEPTED BY OLD BROWSERS, SO FOR CERTAIN TARGET GROUPS YOU NEED TO CONVERT BACK TO ES5. 

// EXECUTING:
// THERE ARE TWO METHODS OF EXECUTING JAVASCRIPT CODE, EITHER INLINE IN HTML CODE (BETWEEN <script> </script>) OR IN SEPERATE JS FILE
// WHEN IN SEPERATE FILE, STILL <script> </script> NEEDS TO BE IMPLEMENTED IN THE HTML CODE, BUT WITH <script src = "seperate_json_file.js"> </script>
// JAVASCRIPT EXECUTES NaN's, BUT WHEN A SYNTAX ERROR OCCURS IT DOESN'T EXECUTE
// USE alert-KEYWORD FOR A POP-UP WINDOW, console.log(variables) TO WRITE IT TO CONSOLE IN THE BROWSER
// FOR USER-INPUT, USE prompt-KEYWORD

// JAVASCRIPT SYNTAX:
// JAVASCRIPT HAS DYNAMIC TYPING, WHICH MEANS THAT TYPES ARE INFERRED, NOT SPECIFICALLY DECLARED
// DATA TYPES:
// NO INTEGERS!
// NUMBER/FLOAT: AS EXPECTED
// STRING: IDEM EITHER WITH SINGLE QUOTES '' OR DOUBLE QUOTES ""
// BOOLEAN: IDEM (true OR false)
// UNDEFINED: DATA TYPE OF VARIABLE THAT DOESN'T HAVE VALUE YET
// NULL: NON-EXISTENT/NO LINK BETWEEN VARIABLE NAME AND VALUE
// _________________________________________________________________________________________
// DECLARING VARIABLES:
// var nameName = integer/string/float/...
// THE var-KEYWORD ONLY NEEDS TO BE USED ONCE, AT THE BEGINNING, ONCE DECLARED, IT CAN BE ASSIGNED USING '='
// JAVASCRIPT HAS camelCase CONVENTION FOR VARIABLES
// JAVASCRIPT CONCATENATES EVERYTHING AS STRINGS WITH '+', EXCEPT NUMBER + UNDEFINED AND UNDEFINED + BOOLEAN
// THIS HAPPENS DUE TO TYPE COERCION, WHERE JAVASCRIPT CONVERT TYPES WHEN NEEDED
// VARIABLES CANNOT START WITH NUMBER AND CANNOT CONTAIN SPECIAL CHARACTERS EXCEPT $ AND _
// VARIABLES CANNOT HAVE RESERVED NAMES (E.G.: function)
// VARIABLES THAT ARE CONSIDERE false WHEN EVELUATED IN CONTROL FLOW ARE 0, null, undefined, "" (EMPTY STRING), NaN, false
// VARIABLES THAT ARE CONSIDERE TRUE ARE 25 (ANYTHING BIGGER THAN 0), "DURK" (NON-EMPTY STRING), true
// _________________________________________________________________________________________
// OPERATORS:
// USUAL '+', '-', '*', '/', '**' (EXPONENTIATION) AND THE LOGICAL OPERATORS OR '||' AND 'AND' '&&' AND NOT '!'
// FOR COMPARISON, '>', '<', '>=', '<=' AND USE === AND !== SINCE == AND != DOES NOT NOTICE DIFFERENT DATA TYPES, SINCE IT USES TYPE COERCION:
// 5 === '5' GIVES false, BUT 5 == '5' GIVES true
// typeof-KEYWORD TELLS THE TYPE OF A VARIABLE
// '*=', '/=', '-=', '+=', '**=', number'++', number'--' ALSO EXISTS IN JAVASCRIPT
// ASSIGNMENT WORKS FROM RIGHT TO LEFT, WHICH MEANS x = y = 26 WORKS FINE, ALSO IF AFTERWARDS y += 3000, x STILL 26
// _________________________________________________________________________________________
// CONTROL FLOW:
// IF-ELSEIF-THEN:
// if (condition){
//     execute_something;
// }
// else if (condition){
//     execute_something_else;
// }
// else {
//     execute_the_rest;
// }
// IF-THEN CAN BE MADE SHORTER WITH TERNARY OPERATOR:
// (condition) ? if true then execute : if false then execute;
// IN CASE OF ONE ACTION, IT CAN BE PUT INTO ONE LINE:
// if(condition) execute_something;
// SWITCH:
// switch(variable_to_be_tested){
//     case value_it_is_to_be_tested_against:
//         action_to_be_performed;
//         break;
//     case another_value_it_is_to_be_tested_against:
//         action_to_be_performed;
//         break;
//     default:
//         action_to_be_performed;
// }
// THE BREAK IS REALLY IMPORTANT OR IT EVALUATES EVERYTHING FROM THAT POINT ON!
// DO-WHILE:
// while(condition){
//     execute_something;
// }
// OR:
// do {
//     execute_something;
// } 
// while (condition);
// THE 'continue'-KEYWORD STOPS CURRENT ITERATION AND ENTERS THE NEXT ONE
// FOR-LOOPS:
// for(var iterator; stop_condition_using_the_iterator; action_on_iterator){
//     do_something;
// }
// _________________________________________________________________________________________
// FUNCTIONS:
// FUNCTION STATEMENT/DECLARATION (PERFORM ACTIONS, BUT NO IMMEDIATE RESULTS):
// function function_name(variable_one, variable_two,...){
//     do something;
//     return something;
// }
// FUNCTION EXPRESSION (EXPRESSION ALWAYS RETURN SOMETHING):
// var function_name = function(variable_one, variable_two,...) {
//     do something;
//     return something;
// }
// function_name(value_one, value_two, ...);
// _________________________________________________________________________________________
// ARRAYS:
// var list_name = [value_one, value_two,..];
// OR:
// var list_name = new Array(value_one, value_two,...);
// LIST/ARRAYS ARE MUTABLE (INDEX STARTS AT 0):
// list_name[position_old_value] = new_value;
// IF A NEW VALUE IS ADDED AT A POSITION NOT EXISTING PRIORILY, THE POSITION IS FILLED, ALSO IF IT'S WAY OUT OF BOUNDS, THE VALUES IN BETWEEN WILL BE FILLED AS 'empty value'
// TO ADD VALUE AT THE END, USE list_name[list_name.length] = value_to_be_inserted_at_the_end OR USE  METHOD list_name.push(value_to_be_inserted_at_the_end)
// TO REMOVE ELEMENT AT THE END USE METHOD .pop()
// TO ADD AT THE BEGINNING, USE METHOD .unshift(value_to_be_inserted_at_the_beginning)
// TO REMOVE ELEMENT AT THE BEGINNING, USE METHOD .shift()
// TO RETRIEVE INDEX OF CERTAIN VALUE, USE METHOD .indexOf(value_in_list), IF NOT PRESENT, RETURNS -1
// DICTIONARIES (ALSO CALLED OBJECTS IN JAVASCRIPT, EXTREMELY CONFUSING):
// var dictionary_name = {
//     key : "value",
//     another_key : "another_value",
//     ...
// }
// OR:
// var dictionary_name = new Object()
// dictionary_name.key = value;
// ...
// TO ACCESS IT, USE dictionary_name[key_in_dictionary] OR dictionary_name.key_in_dictionary
// THE VALUES CAN BE CHANGED:
// dictionary_name[key_in_dictionary] = new_value;
// WHEN YOUR VALUE IS A FUNCTION, IT IS CALLED A METHOD
// CALL A METHOD AS '.method_to_be_called()'
// WITHIN A METHOD, TO ACCES ANOTHER VALUE OF THE OBJECT, USE 'this.value_to_be_accessed'
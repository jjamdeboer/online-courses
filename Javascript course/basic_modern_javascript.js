// ES5 RELEASED IN 2009 WAS A BIG THING AND THIS VERSION IS NOWADAYS ALWAYS INTEGRATED IN EVERY WEB BROWSER, EVEN THE OLD ONES
// IN 2015, ES6/ES2015 WAS RELEASED, WITH A GIGANTIC UPDATE. TO PREVENT SUCH A HUGE UPDATE IN THE FUTURE, THE LANGUAGE IS NOW UPDATED EVERY YEAR IN SMALL BITS (ES7/ES2016 ETC.). THE NEW VERSIONS ARE NOT ACCEPTED BY OLD BROWSERS, SO FOR CERTAIN TARGET GROUPS YOU NEED TO CONVERT BACK TO ES5.

// FOR ES5, ALL DECLARATIONS ARE DONE WITH var:
// var variable_name = some_value;
// variable_name = some_other_value;
// THESE DECLARATIONS ARE FUNCTION-SCOPED (WITHIN FUNCTIONS DEFINED)
// FOR ES6, MUTABLE DECLARATIONS ARE DONE WITH let:
// let variable_name = some_value;
// variable_name = some_other_value;
// const variable_name = some_fixed_value;
// THESE DECLARATIONS ARE BLOCK-SCOPED, WHICH MEANS WITHIN *ANY* '{}', SO ALSO LOOPS
// CONSTANTS MUST ALWAYS BE GIVEN A VALUE AT DECLARING, let AND var DON'T NEED THIS
// YOU CAN'T ACCES let AND const BEFORE DECLARING, WHEREAS var ALLOWS FOR ACCESSING IT BEFORE DECLARATION,, YIELDING 'undefined'
// INSTEAD OF USING IMMEDIATELY-INVOKED FUNCTION EXPRESSIONS (IIFE) FOR PRIVATE VARIABLES, ONE CAN THEREFORE ALSO USE {let variable_name; const other_variable_name = some_value; ...}

// FOR STRINGS IN ES5, ONE CAN USE '+' FOR CONCATENATION, BUT NOT INCLUDING VARIABLES THAT ARE ALSO STRINGS "NICE WEATHER MR " + variable_name + " ISN'T IT?", but with ES6 ONE CAN TEMPLATE LITERALS, WHICH IS SOMETHING SIMILAR TO f-NOTATION IN PYTHON: `NICE WEATHER MR ${variable_name} ISN'T IT?` 
// NEW METHOD FOR STRINGS: .startsWith('string_that_word_begins_with') and .endsWith('string_that_word_ends_with') AND .includes('string_that_is_in_the_word') AND .repeat('times_to_repeat_the_string')

// FOR ANONYMOUS FUNCTIONS/LAMBDA EXPRESSIONS, ONE CAN ALSO USE ARROW NOTATION IN ES6:
// Array.map(function(value, index, array){do_something});
// BECOMES:
// Array.map((value, index, array) => do_something);
// OR:
// Array.map((value, index, array) => {do_something ... return something});
// CONTRARY TO REGULAR FUNCTIONS, ARROW-FUNCTIONS DO NOT HAVE THEIR OWN this-KEYWORD, BUT HAVE THE ONE OF THEIR SURROUNDINGS (LEXICAL this-KEYWORD)

// FOR ARRAYS IT IS POSSIBLE TO 'DECONSTRUCT' THE ARRAY (SIMILAR TO TUPLE UNPACKING IN PYTHON) IN ES6:
// array = [value_one, value_two,...];
// let/const [variable_one, variable_two ,...] = [value_one, value_two,...];
// OR:
// let/const [variable_one, variable_two ,...] = array;
// OR:
// const object = {key_one: value_one, key_two: value_two};
// let/const {variable_one, variable_two} = object;
// THIS IS NOT POSSIBLE IN ES5, WHERE IT HAD TO BE DECLARED SEPERATELY FOR EACH VARIABLE
// ANOTHER OPERATOR/METHOD FOR ARRAYS IN ES6 IS THE SPREAD OPERATOR '...', WHICH CAN BE USED (TO USE VALUES OF ARRAY AS ARGUMENTS OF A FUNCTION):
// array = [value_one, value_two,...];
// function function_name (variable_one,...,length_array){do_something};
// function_name(...array);
// OR (TO CONCATENATE TWO ARRAYS):
// let/const array_one;
// let/const array_two;
// let/const [...array_one,...array_two];
// IT CAN ALSO BE USED TO CONVERT SINGLE ARGUMENTS INTO AN ARRAY (THE OPPOSITE) IN A FUNCTION CALL (SEE BELOW), BUT IS THEN CALLED 'REST PARAMETERS' INSTEAD
// AS ANOTHER MEAN OF DECOMPOSITION/DECONSTRUCTION
// ANOTHER FEATURE IS, THAT IN THE array.forEach() or array.map() IT IS NOT POSSIBLE TO USE break OR continue, SO A NEW SOLUTION WAS INTRODUCED IN ES6:
// for (let/const (value, index, array) of array_name){do_something};
// TWO OTHER METHODS FOR ARRAYS ARE .findIndex((value, index, array) => do_something) AND .find((value, index, array) => do_something)

// FOR FUNCTIONS, ANY NUMBER OF ARGUMENTS CAN BE PASSED IN A FUNCTION, EVEN WHEN LIMITED NUMBER OF ARGUMENTS IS DECLARED OR MORE ARGUMENTS ARE DECLARED THEN THERE ARE PASSED IN (THE ONES THAT ARE NOT EXPLICITLY DEFINED ARE SET TO undefined THEN). FUNCTIONS HAS ACCESS TO THESE ARGUMENTS VIA .arguments
// TO CONSTRUCT THE ARGUMENTS/CAST ARGUMENTS INTO AN ARRAY, ONE CAN ALSO USE '...' IN ES6, WHICH IS CALLED 'REST PARAMETERS' INSTEAD OF SPREAD OPERATOR:
// function function_name(variable_name_one, variable_name_two, etc., ...array_name){do_something};
// MAIN DIFFERENCE BETWEEN REST PARAMETERS AND SPREAD OPERATOR IS THAT THE FIRST IS USED IN FUNCTION ARGUMENTS/PARAMETERS, WHILST THE LATTER IS USED FOR VARIABLE DECLARATIONS
// FOR DEFAULT PARAMETERS OF A FUNCTION, IN ES5 ONE HAS TO USE THE FACT THAT THESE ARE SET TO undefined AND THEN MAKE AN if-LOOP AROUND THIS. WITH ES6:
// function function_name(variable_one = default_value, variable_two = another_default_value, ...){do_something};

// OBJECTS: A NEW OBJECT IS INTRODUCED IN ES6, WHICH ARE MAPS. THESE ARE OBJECTS/DICTIONARIES IN WHICH NOT ONLY STRINGS ARE ACCEPTED AS KEYS, BUT ANYTHING CAN BE USED FOR A KEY
// TO USE IT:
// let/const map_name = new Map();
// map_name.set(key_one, value_one).set(key_two, value_two,...);
// MAPS ALSO HAVE THE METHOD .size, WHICH IS COMPARABLE TO .length OF ARRAYS, STRINGS OR LISTS
// MAPS ARE, LIKEWISE, ALSO ITERABLE, SO .forEach((value, key) => do_something) CAN ALSO BE USED ON THEM, AND THIS AS WELL: 
// for (let/const [key, value] of array/map.entries()){do_something};
// ANOTHER NEW OBJECT IS CALLED CLASS, WHICH IS THE SAME AS PREVIOUS OBJECT DECLARATIONS, BUT DIFFERENTLY DECLARED:
// class class_name {
//     constructor (property_one, property_two, ...){
//         this.property_one = property_one;
//         this.property_two = property_two;
//     }
//     method_one(variable_one,...){
//         do_something;
//     }
//     ...
// }
// let/const class_instance = new class_name(value_one, value_two,...);
// CLASSES ARE NOT HOISTED, SO CANNOT BE CALLED BEFORE DECLARATION
// ALSO: ONE CANNOT ADD PROPERTIES TO CLASSES, ONLY METHODS
// FOR INHERITANCE (WITH CLASSES IN ES6):
// class ConstructorThatInherits extends Constructor {
//     constructor(property_one_of_Constructor,...,property_one,...,method_one,...){
//         super(property_one_of_Constructor,...);
//         this.property_one = property_one;
//         ...
//     }
//     this.method_one = method_one;
//     ...
// }

// SEVERAL ASYNCHRONOUS FUNCTIONS WHICH DEPEND ON EACH OTHER, IS CALLED 'CALL-BACK HELL' IN JAVASCRIPT AND RESULTS IN VERY LONG RECURSIONS OF CODE. THIS IS SOLVED IN ES6 USING PROMISES
// A PROMISE IS AN OBJECT THAT KEEPS TRACK ON WHETHER AN ASYNCHRONOUS EVENT ALREADY HAPPENED AND DETERMINES WHAT HAPPENS AFTER EVENT TRIGGERS, IMPLEMENTS THE CONCEPT OF EXPECTED FUTURE VALUE
// IF EVENT DIDN'T HAPPEN YET, IT IS PENDING, AFTER IT HAPPENS IT IS SETTLED/RESOLVED, AND IF THE FUTURE VALUE WAS CORRECT, THEN IT IS FULFILLED, OTHERWISE REJECTED
// ONE CAN PRODUCE AND CONSUME PROMISES
// let/const promise = new Promise((resolve, reject) => {do_something_asynchronous_which_will_either_return_resolve_or_reject});
// AND THEN:
// promise.then(resolve => {do_something_when_resolves});
// promise.catch(reject => {do_something_when_rejects});
// OR IN ES7:
// async function consumePromise() {
//     try {
//         let/const resolve = await promise;
//     }
//     catch{
//         do_something_when_rejecting;
//     }
// }
// consumePromise();
// THE await-KEYWORD CAN ONLY BE USED INSIDE AN async-FUNCTION, WHICH STOPS THE CODE IN THE async-FUNCTION, BUT THIS FUNCTION RUNS IN THE BACKGROUND

// IN MODERN JAVASCRIPT DEVELOPMENT DEVELOPMENT TOOLS (NODE PACKAGE MANAGER (NPM)) AND LIBRARIES/FRAMEWORKS (NODE.JS) ARE OFTEN USED
// IT IS POSSIBLE TO USE SCRIPTS FOR NPM
// ALSO, TO CONVERT BACK FROM ES6+ TO ES5 OFTEN 'BABEL' IS USED
// TO USE ES6+ MODULES, WHICH ARE OFTEN NOT SUPPORTED BY BROWSERS, OFTEN WEBPACK IS USED TO BUNDLE MODULES TOGETHER
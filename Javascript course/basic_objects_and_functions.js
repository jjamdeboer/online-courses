// IN JAVASCRIPT PRIMITIVES ARE ACCEPTED DATA TYPES, THE REST IN JAVASCRIPT ARE (SPECIAL) OBJECTS:
// - ARRAYS/LISTS
// - FUNCTIONS
// - OBJECTS/DICTIONAIRIES
// - DATES
// - WRAPPERS FOR DATA TYPES
// OBJECTS CONSIST OF PROPERTIES (VALUES) AND METHODS (FUNCTIONS). PRIMITIVES ALSO HAVE METHODS, BUT THE PRIMITIVES ARE IMMEDIATELY TRANSFORMED TO AN OBJECT WHEN A METHOD IS CALLED ON THEM
// CONSTRUCTOR IS A BLUEPRINT OBJECT (PERSON) AND INSTANCE IS SPECIFICATION OF THAT OBJECT (JOHN)
// INHERITANCE IS EXPORTING THE PROPERTIES AND METHODS TO ANOTHER OBJECT (REPTILE IS AN ANIMAL)
// THE METHODS TO BE INHERITED HAVE TO BE STORED IN THE PROTOTYPE PROPERTY OF AN OBJECT
// MOTHER OF ALL OBJECTS IS THE OBJECT OBJECT
// YOU CAN ACCESS ALL METHODS THAT ALL ARE PUT IN THE PROTOTYPE PROPERTY OF THE OBJECT'S PARENT AND THAT PARENT'S PARENT RECURSIVELY, CREATING A 'CHAIN', THE PROTOTYPE CHAIN
// DIFFERENCE BETWEEN PRIMITIVES AND OBJECTS IS THAT THE PRIMITIVES LINKS TO THE VALUE DIRECTLY, WHEREAS OBJECTS LINK TOWARDS COLLECTION OF PRIMITIVES:
// var a = var b = 6;
// a = 12;
// b STILL 6
// var a = var b = {durk: 4, durkudurk: "DUURK"}; 
// a.durk = "DUUUUUUUUUUURK!!!";
// b NOW ALSO {durk: DUUUUUUUUUUURK!!!, durkudurk: "DUURK"}
// THEREFORE, WHEN PASSING PRIMITIVES AS ARGUMENTS IN A FUNCTION, THE LINK TO THE NEW VALUE IS DESTROYED AFTER THE RETURN (NOT THE CONTENT, THIS IS STILL ACCESSIBLE BY ENCLOSED FUNCTIONS BY MEANS OF CLOSURE) AND THE PRIMITIVES HAVE THEIR OLD VALUE BACK. THIS IS NOT THE CASE FOR THE PRIMITIVES INSIDE AN OBJECT, IF THE OBJECT IS CALLED AS AN ARGUMENT AND THE PROPERTIES OR METHODS THEN CHANGED
// FUNCTIONS ARE ALSO OBJECTS AND CAN BE ASSIGNED TO A VARIABLE, SO FUNCTIONS CAN ALSO BE PASSED INTO OTHER FUNCTIONS (HIGHER ORDER FUNCTIONS)
// POSSIBILITY OF IMMEDIATELY INVOKED FUNCTION EXPRESSIONS (IIFE) TO CREATE A FUNCTION IMMEDIATELY OR TO HIDE VARIABLES OUTSIDE GLOBAL SCOPE (PUT BRACKETS AROUNDS IT, TO NOT MAKE IT AN EXPRESSION, NOT A DECLARATION); NOT FOR REUSABLE CODE:
// (function(empty/variable_one,...){do_something})();
// CLOSURE: AN INNER FUNCTIONS ALWAYS HAS ACCESS TO OUTER FUNCTIONS, EVEN AFTER THE OUTER FUNCTION HAS RETURNED (IF FUNCTION A RETURNS FUNCTION B, THEN B STILL HAS ACCESS TO ALL PROPERTIES AND METHODS OF A)
// ANOTHER THING THAT CAN BE DONE WITH FUNCTIONS IS TO USE .call(set_this._context, value_one,...,function_one,...) OR .apply(set_this._context, [value_one,...,function_one,...]), TO CHANGE THE this.-CONTEXT SO THAT ANOTHER FUNCTION OR OBJECT CAN BE ENTERED
// ANOTHER WAY TO CHANGE THE this.-CONTEXT IS TO USE .bind, WHICH ALLOWS TO ONLY PARTIALLY FILL IN REMAINING PROPERTIES AND METHODS, THIS IS CURRYING: 
// .bind(set_this._context, property_x = value_x,..., method_y = function_y,...)
// .call, .apply, .bind CAN ALSO BE INVOKED ON LAMBDA EXPRESSIONS
// A WAY TO EXECUTE FUNCTIONS ON A WHOLE ARRAY IS TO USE array.forEach(function(current_value, current_index, whole_array){do_something}) AND array.map(function(current_value, current_index, whole_array){do_something}), OF WHICH THE LATTER RETURNS THE NEW ARRAY
// A FUNCTION ALWAYS HAS ACCESS TO .this PROPERTY AND TO .arguments PROPERTY, WHICH ARE THE ARGUMENTS THAT ARE PASSED IN. ANY NUMBER OF ARGUMENTS CAN BE PASSED IN, EVEN WHEN LIMITED AMOUNT IS DECLARED IN THE FIRST PLACE
// WHEN LESS ARGUMENTS ARE PASSED IN THEN THERE ARE FUNCTION PARAMETERS, JAVASCRIPT ASSIGNS undefined TO THEM

// IN JAVASCRIPT CONSTRUCTORS ARE WITH CAPITAL LETTER
// TO CREATE CONSTRUCTOR:
// var Constructor = function(property_one,...,method_one,...){
//     this.property_one = property_one;
//     ...
//     this.method_one = method_one;
//     ... 
// }
// OR (SECOND WAY):
// var constructorPrototypeProperty = {
//     property_one: undefined/value_one,
//     ...
//     method_one: undefined/function(empty/input){do_something};
//     ...
// }
// TO CREATE INSTANCE:
// var instance = new Constructor(value_one,...,function_one,...);
// OR (WITH SECOND WAY):
// var instance = Object.create(constructorPrototypeProperty);
// IN CASE .property_one IS undefined:
// instance.property_one = value_one;
// ...
// TO ADD SOMETHING TO THE PROTOTYPE PROPERTY OF THE OBJECT:
// Constructor.prototype.property_to_be_added = property_to_be_added;
// Constructor.prototype.method_to_be_added = function(){do_something};
// FOR INHERITANCE:
// var ConstructorThatInherits = function(property_one_of_Constructor,...,property_one,...,method_one,...){
//     Constructor.call(this, property_one_of_Constructor,...);
//     this.property_one = property_one;
//     ...
//     this.method_one = method_one;
//     ... 
// }
// ConstructorThatInherits.prototype = Object.create(Constructor.prototype)
// OF WHICH THE LAST LINE TAKES CARE THAT ALSO THE ORIGINAL METHODS CAN BE USED
# PROCEDURAL PROGRAMMING: FOCUS ON PROCEDURES (ROUTINES OR SUBROUTINES WHICH ARE CONSECUTIVELY CALLED)
# OBJECT-ORIENTED: OBJECTS MAY CONTAIN DATA, PROCEDURES ARE KNOWN AS METHODS. 
#       THE OBJECTS' PROCEDURES CAN ACCESS AND MODIFY THE DATA IN THE OBJECTS (THUS HAVE A NOTION OF 'SELF').
#       CLASSES ARE ONE INSTANCE, BUT MOST POPULAR FORM OF, OBJECTS.
# FUNCTIONAL PROGRAMMING: FOCUS ON FUNCTIONS (ALSO TREATED AS VALUES IN THESE PROGRAMS)
# LOGIC PROGRAMMING: PROLOG


# INDICATE CLASS (PascalCase):

# class NameOfClass():

# INDICATE METHODS (= FUNCTION WITHIN CLASS)
        # def __init__(self, parameter_one, parameter_two):
        #     ATTRIBUTES OF THE CLASS/OBJECT
        #     SELF IS A REFERENCE TO THE PARTICULAR DATA THING IN THE CLASS
        #     self.parameter_one = parameter_one
        #     self.parameter_two = parameter_two

        # def some_method(self):
        #     FOR EXAMPLE
        #     print(self.parameter_one)


class Classy():
    # CLASS OBJECT ATTRIBUTE ARE THINGS THAT ARE DEFINED AT LEVEL OF CLASS (CLASSY IS BLACK)
    skin = "black"
    # COULD HAVE TYPE CONTROL FOR HOR
    def __init__(self,hor):
        self.hor = hor

    def sassy(self,durk):
        # NEED TO CALL SELF TO ACCESS THIS DATA 
        print (f"HEEEEEEEEELL NO! I'M {self.skin.upper()} AND {durk}")

my_classy = Classy(hor = True)
# DON'T NEED TO SPECIFICALLY CALL 'hor = ', A VALUE SUFFICES (IN SAME ORDER AS CALLED IN __init__)
my_classy = Classy(False)
print(type(my_classy))
my_classy.sassy("I'M BIG")
print(my_classy.hor, "AND", my_classy.skin, "AND", )

# INHERITANCE ALLOWS FOR USING TO CREATE CLASSES BY MEANS OF OTHER CLASSES/METHODS OF OTHER CLASSES
class Durk(Classy):

    def __init__(self):
        Classy.__init__(self,True)
        print("DUUUUUURK")

    def __str__(self):
        return "DUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURKDURKUUUUDUUUUUUUUURK"

durk = Durk()
durk.sassy("DUUUUUUUUUUUUUUUUUUUUUUURK")
print(type(durk))
print(durk)

# POLYMORPHISM: SHARING METHOD BETWEEN CLASSES WITH SAME NAMES BUT DIFFERENT OPERATION
# TO BE ABLE TO USE PYTHON METHODS ON YOUR CLASSES, USE MAGIC METHODS OR DUNDER (DOUBLE UNDERSCORE) METHODS
# TO DELETE THINGS FROM MEMORY, USE KEYWORD 'del'
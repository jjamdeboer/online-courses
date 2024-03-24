#  THIS IS HOW TO MAKE LIST COMPREHENSION RECURSIVE:

a = [2]
prime_list = [ a := a + [ p ] for p in range( 3, 10**5, 2 ) if all( map( lambda x: p % x, a ) ) ]
print( 'WITH LIST COMPREHENSION\n' )
print( a, '\n', 'Length: ', len( a ), '\n' )

#  THIS IS THE PREFERRED WAY FOR LARGER LISTS, SINCE THIS IS WITH A GENERATOR, RATHER THAN A LIST OF LISTS
a = [2]
prime_generator = ( a := a + [ p ] for p in range( 3, 10**5, 2 ) if all( map( lambda x: p % x, a ) ) )
for p in prime_generator:
    pass
print( 'WITH GENERATOR COMPREHENSION\n' )
print( a, '\n', 'Length: ', len( a ) )

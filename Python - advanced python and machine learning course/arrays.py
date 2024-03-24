import numpy

durk = [ 1, 'HELLO', 5.6, True ]

print( "ARRAY OF LIST ", numpy.array( durk ) )
print( type( numpy.array( durk ) ) )
print( "MATRIX/ ARRAY OF LIST OF LISTS ", numpy.array([ durk, durk, durk ]) )
print( "DATATYPE IN PREVIOUS MATRIX ", numpy.array([ durk, durk, durk ]).dtype )
print( "VECTOR GENERATED WITH RANGE FUNCTION ",numpy.arange( 0, 100, 13 ) )
print( "EVENLY DISTRIBUTE A VECTOR INCLUDING 6, 70 in steps of 19 ", a:= numpy.linspace( 6, 70, 19 ) )
print( "MAXIMUM AND MINIMUM OF PREVIOUS ARRAY ", a.max(), a.min() )
print( "BOOLEAN REPRESENTATION OF ALL ENTRIES OF EVENLY DISTRIBUTED VECTOR > 50 ", a > 50 )
print( "ARRAY OF ALL VALUES OF EVENLY DISTRIBUTED VECTOR > 50 ", a[ a > 50 ] )
print( "ARRAY OF ALL VALUES OF EVENLY DISTRIBUTED VECTOR > 50 AND SMALLER THAN 60", a[ ( a > 50 ) & ( a < 60 ) ] )
print( "LOCATIONS OF MAXIMUM AND MINIMUM OF PREVIOUS ARRAY ", a.argmax(), a.argmin() )

# INPUT TUPLE OF MORE THAN 1 DIMENSION
print( "THIS IS ZEROS 3, 9\n", numpy.zeros(( 3, 9 )) )
print( "... ONES 2, 5, 3\n", numpy.ones(( 2, 5, 3)) )
print( "RESHAPING THE PREVIOUS MATRIX AS 2x15\n", numpy.ones(( 2, 5, 3 )).reshape( 2, 15) )
print( "THE DIMENSIONALITY OF PREVIOUS ORIGINAL MATRIX\n", numpy.ones(( 2, 5, 3 )).shape )
print( "IDENTITY MATRIX OF 7x7\n", e := numpy.eye( 7 ) )
print( "RESHUFFLING OF PREVIOUS IDENTITY MATRIX\n", e[[ 5, 6, 0, 3, 2, 1, 4 ]] )
# INPUT NOT A TUPLE, ALTHOUGH MORE THAN 1 DIMENSION
print( "ARRAY OF 3x5 RANDOM NUMBERS BETWEEN 0 AND 1\n", numpy.random.rand( 3, 5 ) )
print( "ARRAY OF 2x8 RANDOM NUMBERS OF GAUSSIAN AROUND 0\n", numpy.random.randn( 2, 8 ) )
# INPUT TUPLE OF MORE THAN 1 DIMENSION
print( "ARRAY OF 3x4 OF RANDOM NUMBERS BETWEEN 4 AND 500\n", numpy.random.randint( 4, 500, (3,4) ) )

# SLICING:
#  INDEXING CAN BE DONE WITH DOUBLE AND SINGLE BRACKETS IN CASE OF MATRICES/TENSORS
print( "SLICING OF MATRIX/ ARRAY OF LIST OF LISTS\n", numpy.array([ durk, durk, durk ])[ 1: ][ 1 ][ 2: ] )
print( "SLICING OF MATRIX/ ARRAY OF LIST OF LISTS\n", numpy.array([ durk, durk, durk ])[ 1:,  2: ] )
# CASTING ON MULTIPLE POSITION OF THE ARRAY:
# WATCH OUT, LIKE LISTS, WHENEVER A COPY IS MADE (EVEN SLICED) ORIGINAL ARRAY ALSO CHANGED AFTER CASTING!
DURKUDURK = numpy.array([ durk, durk, durk ])
DURKUDURK[ 1: ][ 0 ][ 2: ] = 1e17
print( "A CAST ARRAY\n", DURKUDURK )

# ARRAY OPERATIONS:
# ROWS ARE 0 AXIS, COLUMNS 1 AXIS
print( "TWO ADDED IDENTITY MATRICES OF 7x7 AND A MATRIX OF 1'S\n", ( b := e + e ) + (c := numpy.ones(( 7, 7 )) ) )
print( "ELEMENT-WISE MULTIPLICATION OF PREVIOUS ARRAY AND (TWO ADDED IDENTITY MATRICES)\n", 
( b + c )*( b ) )
print( "SCALAR PLUS OR TIMES OR EXPONENTIATE (IDENTITY) MATRIX\n", ( d:= numpy.eye(8) ) + 5.2, '\n', d*6, '\n', ( d * 6 )**8 )
# CAN ALSO DO REGULAR OPERATIONS SUCH AS LOG, EXP, SIN, COS ON WHOLE ARRAYS:
print( "SINE OF TWO ADDED IDENTITY MATRICES OF 7x7 AND A MATRIX OF 1'S\n", numpy.sin( b + c ) )

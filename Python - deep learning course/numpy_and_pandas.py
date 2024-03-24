#  NUMPY IS SHORT FOR 'NUMERICAL PYTHON' AND ITS ARRAYS USES MUCH LESS MEMORY THAN REGULAR LISTS
#  PANDAS IS SHORT FOR PANEL DATA; HEAVILY BASED ON NUMPY ARRAYS

import numpy as np
import pandas as pd

#####  CREATING ARRAYS
a = np.array([ [1, 2], [0, 2], [9, 2] ])
print( a, '\n', a.shape )
#  NOTE THAT THIS RETURNS POINTS WITHIN THE INTERVAL -- 3 POINTS IN THIS CASE
b = np.arange( 3, 15, 5 )
print( b, '\n', b.shape )
#  MULTIPLICATION
print( np.dot( b, a ), np.matmul( b, a ) )
#  NOTE THAT THIS RETURNS EVENLY SPACED POINTS IN THE INTERVAL -- 5 IN THIS CASE
c = np.linspace( 3, 15, 5 )
print( c, '\n', c.shape )
#  FOR CREATING ZEROES OR RANDOM NUMBERS
d = np.zeros(( 3, 15 ))
print( d, '\n', d.shape )
d = np.ones(( 3, 15 ))
print( d, '\n', d.shape )
d = np.eye( 3 )
print( d, '\n', d.shape )
#  UNIFORM DISTRO; NOTE THE SINGLE BRACKETS HERE!
d = np.random.rand( 3, 15 )
print( d, '\n', d.shape )
#  GAUSSIAN DISTRO; NOTE THE SINGLE BRACKETS HERE!
d = np.random.randn( 3, 15 )
print( d, '\n', d.shape )
#  RANDOM INTEGER IN A GIVEN RANGE: START, STOP, (SHAPE)
d = np.random.randint( 3, 15, ( 3, 15 ) )
print( d, '\n', d.shape )
#  RESHAPING TO ANOTHER MATRIX WITH SAME NUMBER OF ELEMENTS
print( d.reshape( 45, ), '\n', d.reshape( 45, ).shape )
#  RETRIEVING MAX/MIN AND LOCATION OF MAX/MIN
print( a, '\n', a.max(), a.argmax(), a.min(), a.argmin() )


#####  SELECTING
print( d, '\n', d.shape )
print( d[ 1, 2 ] )
#  BROADCASTING MULTIPLE VALUES OF AN ARRAY
d[ 1:, 2:7:2 ] = 20
#  NOTE THAT SLICING GOES: START:END:STEP
print( d, '\n', d.shape )
print( d[ 1:, 2:7:2 ] )
#  CONDITIONAL SELECTION
print( d, '\n', d.shape )
print( ( d < 10 ) & ( d % 2 == 0 ) )
print( d[ ( d < 10 ) & ( d % 2 == 0 ) ] )

 
#####  CREATING ARRAYS
e = pd.Series( np.linspace( 1, 2039, 10  ), list( 'abcdefghij' ) )
#  SELECTIONS ON SERIES
print( 
    #  ALL 
    e, 
    '\n', 
    #  ONLY ONE ITEM BY NAME
    e[ 'e' ], 
    '\n', 
    #  ONLY ONE ITEM BY INDEX (IF NAMED WITH A NUMBER, NAMING TAKES PRECEDENCE)
    e[ 5 ], 
    '\n', 
    #  SLICING ON NAME
    e[ 'e': ], 
    '\n', 
    #  SLICING ON INDEX
    e[ 8: ], 
)
f = pd.DataFrame( d, index = [ 'a', 'b', 'c' ], columns = np.arange( 1, 30, 2 ) )
#  DEFINING A NEW COLUMN
f[ 4 ] = f[ 3 ]
#  DEFINING A NEW ROW
f.loc[ 'f' ] = f.loc[ 'b' ]
#  SELECTIONS ON DATAFRAME
print( 
    #  ALL 
    f, 
    '\n', 
    #  ONE ITEM PER COLUMN KEY
    f[ 3 ], 
    '\n', 
    #  TWO ITEM PER COLUMN KEY
    f[[ 3, 17 ]], 
    '\n', 
    #  NOTE THAT SLICING IMPLIES THE INDEX (CONFUSING!) AND NO SLICING IMPLIES A KEY
    #  ALSO NOTE THAT SLICING ALWAYS RETURNS A DATAFRAME, WHEREAS A SINGLE COLUMN KEY OR SINGLE INDEX IN .loc RETURNS A SERIES!
    f[ 1: ], 
    '\n', 
    #  THE SAME RESULT AS STEP BEFORE
    f[ 'b': ], 
    '\n', 
    #  IDEM
    f.loc[ 'b': ],
    '\n', 
    #  SLICING BY COLUMN
    f.loc[ :, 21: ],
    '\n', 
    #  SLICING A PART OF THE DATAFRAME BY BOTH INDEX AND COLUMN
    f.loc[ 'b':, 17: ], 
    '\n', 
    #  SLICING ON CONDITION, IN A BROADCASTING FASHION, WHERE SERIES ARE CAST ON ALL COLUMNS
    f[ f[ 17 ] > 8 ], 
    '\n', 
    #  SLICING ON CONDITION, IN A BROADCASTING FASHION, WHERE SERIES ARE CAST ON ALL ROWS
    f.T[ f.loc[ 'b' ] > 8 ].T,
    '\n', 
    #  SLICING ON CONDITION, IN A BROADCASTING FASHION, WHERE SERIES ARE CAST ON ALL COLUMNS
    f[ ( f[ 7 ] > 1 ) & ( f[ 7 ] < 10 ) ], 
    '\n', 
    #  NOTE THAT SINGLE ITEM IS BROADCAST TO WHOLE DATAFRAME! ONLY WORKS WHEN COMBINED WITH A SERIES OR DATAFRAME
    f[ ( f[ 3 ] < 10 ) | ( f.loc[ 'b', 3 ] < 12 ) ], 
    '\n', 
    #  CONDITION WITH SERIES AND DATAFRAME, THE DATAFRAME TAKES PRECEDENCE:
    f[ ( f[ 5 ] < 90 ) | ( f.loc[ 'b':, 17:] > 8 ) ], 
    '\n', 
    #  CONDITION WITH TWO DATAFRAMES
    f[ ( f < 12 ) & ( f > 8 ) ], 
    '\n', 
    #  NOTE THAT BROADCASTING HAPPENS ON COLUMN-BASIS, WHICH CAN BE SEEN HERE, SINCE THE ADDITIONAL VALUES ARE ONLY ADDED ON TOP
    #  BEHAVIOUR IS VERY SIMILAR TO CONCAT, WHERE NON-OVERLAPPING COLUMNS/INDICES GET A NAN
    f[ ( f < 90 ) | ( f.loc[ 'b':, 17:] > 8 ) ], 
    '\n', 
    #  NOTE THAT THE ORDER MATTERS: LARGEST ARRAY FIRST AND THEN SECOND ARRAY ON TOP TO AVOID UNEXPECTED BEHAVIOUR
    #  IN THIS EXAMPLE, THE LARGER SET COMES FIRST, THE SECOND SET NARROWS DOWN THE COLUMNS
    #  BEHAVIOUR IS VERY SIMILAR TO CONCAT, WHERE NON-OVERLAPPING COLUMNS/INDICES GET A NAN
    f[ ( f.loc[ :, 17:] > 8 ) | ( f.loc[ 'a':'b', 1:19 ] < 90 ) ], 
    '\n', 
)
#  ONE-HOT ENCODING IN PYTHON IS WITH THE FUNCTION 'get_dummies'

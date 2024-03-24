import numpy
import pandas

# SERIES:
label = ['one',[1,2.4],6.7,{3,7,6}]
values = [1,1,2,1]
value_array = numpy.array(values)
label_value_pair = {'DURK':{1:2,5:9000}, 'DURKUDURK':['HELLO DURK',8.9], 'DURKUDURKUDURK':numpy.array(values)}
# EITHER LISTS OR ARRAYS, DOESN'T MATTER
# IF DICTIONARY IS PUT IN, KEYS ARE TAKEN AS LABEL, VALUE AS VALUE
print( "PANDA SERIES WITH LISTS \n",pandas.Series(values,label))
print( "PANDA SERIES WITH LISTS REVERSED \n",pandas.Series(label,values))
# CONTRARY TO DICTIONAIRIES WHERE ONLY ONE VALUE IS RETURNED, HERE 
#   ALL VALUES ARE RETURNED WITH CORRESPONDING LABEL VALUE
print( "PANDA SERIES LOOKUP LAST RESULT KEY = 1 \n",pandas.Series(label,values)[1])
print( "PANDA SERIES WITH ARRAY \n",pandas.Series(value_array,label))
print( "PANDA SERIES WITH DICTIONAIRY \n",pandas.Series(label_value_pair))
# ADDING SERIES:
print( "ADDED PANDA SERIES \n",pandas.Series({'DURK':'DURK!!!! ', 'DURKUDURK':2, 'DURKUDURKUDURK':5.6})
+pandas.Series({'DURK':'DURK!!!!', 'DURKUDURK':6.7, 'DURKUDURKUDURK':9000,'DURKUDURKDURKDUDKRKRUDKR':8e90}))
print( '\n\n\n\n' )

# DATAFRAMES:
# FIRST AXIS CAN CONTAIN EVERY DATA TYPE, BUT MAKES LOOKUPS IMPOSSIBLE. 
# SECOND AXIS CAN CONTAIN ONLY STRINGS AND NUMBERS. BOTH CAN CONTAIN IDENTICAL VALUES. BUT BEWARE OF IDENTICAL LABELS, BECAUSE OF ARITHMETIC.
# SECOND INPUT (COLUMN) ARE ALL PANDA SERIES, THE FIRST INPUT IS A SHARED LABEL.
# THE FIRST INPUT CAN ALSO BE RETURNED AS PANDA SERIES.
print( "DATA FRAME \n", a:= pandas.DataFrame(numpy.random.rand(4,5),
[1,["HELLO"],{3,7,"DURK"},{'a':"DURK"}],
['a',3.7,"DURK",6.7,"DURK"]) )
print( "INDICES AND COLUMNS OF PREVIOUS DATA FRAME: \n", a.index, a.columns)
# CAN ALSO USE DICTIONAIRIES FOR GENERATING DATA FRAMES:
exemplum = {1:[5,6,7.6],'a':[2,3.4,4],"DURK":[numpy.nan,numpy.nan,3]}
print( "DATAFRAME OF A DICTIONAIRY \n",pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]))
# FOR RETRIEVING COLUMNS, SIMPLY USE data_frame_variable[NAME OF COLUMN] OR data_frame_variable[[NAME OF COLUMNS]]
print( "DATAFRAME OF COLUMN 'a' \n", a['a'])
print( "NEW DATAFRAME\n", b := pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"]) )
print( "DATAFRAME OF COLUMN 'a' LABEL 'DURK' \n", b['a']["DURK"])
# FOR RETRIEVING ROWS, USE loc OR iloc
#  NORMAL RETRIEVING IS FOR COLUMNS, LOC DEFAULTS TO ROWS
#  FOR RETRIEVING BOTH ROWS AND COLUMNS, USE LOC WITH LOC[ROW,COLUMN] OR LOC[[ROWS],[COLUMNS]]
# loc and iloc WORK WITH '[ROWS], [COLUMNS]'
print( "DATAFRAME OF ROW '1' \n", b.loc[1])
print( "DATAFRAME OF ROW AT POSITION (1,3), 2 \n", b.iloc[[1,3],2])
print( "DATAFRAME OF COLUMN 'a' and 3.7 \n", b[['a',3.7]])

print( '\n\n\n\n' )
murk = pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"])
#  ASSIGNING A NEW COLUMN CAN SIMPLY BE DONE AS IF A DICTIONARY
murk['NEW SERIES'] = murk['a']**murk[3.7] + numpy.sin(murk[6.7])
# CAN ALSO ADD A PRE-MADE SERIES OR A LIST, AS LONG AS DIMENSIONS WITH NUMBERS OF ROWS MATCH
print( "CREATING A NEW SERIES WITH ARITHMETIC ON OLD SERIES \n", murk )
# REMOVING SERIES/COLUMNS OR LABELS:
# murk = murk.drop('NEW SERIES',1)
# murk = murk.drop([1,"DURK"],0)
# ROWS ARE 0 AXIS, COLUMNS 1 AXIS
print( "CREATING A NEW SERIES WITH SERIES AND LABELS REMOVED \n",murk.drop('NEW SERIES', axis = 1).drop([1,"DURK"], axis = 0) )
print( "DATA FRAME OF A DICTIONARY USED FOR STEP HEREAFTER \n", d:= pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]))
print( "REMOVING ROWS WITH NAN OF PREVIOUS DATA FRAME WITH THRESHOLD OF AMOUNT OF NON-NAN-VALUES \n",
d.dropna( axis = 0, thresh = 3 ) )
print( "REMOVING COLUMNS WITH NAN OF PREVIOUS DATA FRAME \n", d.dropna( axis = 1 ) )
print( "REPLACING ALL NAN OF PREVIOUS DATA FRAME WITH 'DURK' \n", d.fillna('DURK'))
print( "REPLACING ALL NAN OF PREVIOUS DATA FRAME WITH MEAN OF DATA FRAME \n",
        e := d.fillna( d.mean() ) )
print( "ADDING LAST DATAFRAME TO AN ADOPTED VERSION OF THE ORIGINAL\n",
        d.dropna( axis = 1 ).drop( 'b', axis = 0 ) + e )

import numpy
import pandas

# SERIES:
label = ['one',[1,2.4],6.7,{3,7,6}]
values = [1,1,2,1]
value_array = numpy.array(values)
label_value_pair = {'DURK':{1:2,5:9000}, 'DURKUDURK':['HELLO DURK',8.9], 'DURKUDURKUDURK':numpy.array(values)}
# EITHER LISTS OR ARRAYS, DOESN'T MATTER
# IF DICTIONARY IS PUT IN, KEYS ARE TAKEN AS LABEL, VALUE AS VALUE
print("PANDA SERIES WITH LISTS \n",pandas.Series(values,label))
print("PANDA SERIES WITH LISTS REVERSED \n",pandas.Series(label,values))
# CONTRARY TO DICTIONAIRIES WHERE ONLY ONE VALUE IS RETURNED, HERE 
#   ALL VALUES ARE RETURNED WITH CORRESPONDING LABEL VALUE
print("PANDA SERIES LOOKUP LAST RESULT KEY = 1 \n",pandas.Series(label,values)[1])
print("PANDA SERIES WITH ARRAY \n",pandas.Series(value_array,label))
print("PANDA SERIES WITH DICTIONAIRY \n",pandas.Series(label_value_pair))
# ADDING SERIES:
print("ADDED PANDA SERIES \n",pandas.Series({'DURK':'DURK!!!! ', 'DURKUDURK':2, 'DURKUDURKUDURK':5.6})
+pandas.Series({'DURK':'DURK!!!!', 'DURKUDURK':6.7, 'DURKUDURKUDURK':9000,'DURKUDURKDURKDUDKRKRUDKR':8e90}))

# DATAFRAMES:
# FIRST AXIS CAN CONTAIN EVERY DATA TYPE, BUT MAKES LOOKPUPS IMPOSSIBLE. 
# SECOND AXIS CAN CONTAIN ONLY STRINGS AND NUMBERS. BOTH CAN CONTAIN IDENTICAL VALUES. BUT BEWARE OF IDENTICAL LABELS, BECAUSE OF ARITHMETIC.
# SECOND INPUT (COLUMN) ARE ALL PANDA SERIES, THE FIRST INPUT IS A SHARED LABEL.
# THE FIRST INPUT CAN ALSO BE RETURNED AS PANDA SERIES.
print("DATA FRAME \n",pandas.DataFrame(numpy.random.rand(4,5),
[1,["HELLO"],{3,7,"DURK"},{'a':"DURK"}],
['a',3.7,"DURK",6.7,"DURK"]))
print("INDICES AND COLUMNS OF PREVIOUS DATA FRAME: \n",pandas.DataFrame(numpy.random.rand(4,5),
[1,["HELLO"],{3,7,"DURK"},{'a':"DURK"}],
['a',3.7,"DURK",6.7,"DURK"]).index,pandas.DataFrame(numpy.random.rand(4,5),
[1,["HELLO"],{3,7,"DURK"},{'a':"DURK"}],
['a',3.7,"DURK",6.7,"DURK"]).columns)
# CAN ALSO USE DICTIONAIRIES FOR GENERATING DATA FRAMES:
exemplum = {1:[5,6,7.6],'a':[2,3.4,4],"DURK":[numpy.nan,numpy.nan,3]}
print("DATAFRAME OF A DICTIONAIRY \n",pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]))
# FOR RETRIEVING COLUMNS, SIMPLY USE data_frame_variable[NAME OF COLUMN]
print("DATAFRAME OF COLUMN 'a' \n",pandas.DataFrame(numpy.random.rand(4,5),
[1,["HELLO"],{3,7,"DURK"},{'a':"DURK"}],
['a',3.7,"DURK",6.7,"DURK"])['a'])
print("DATAFRAME OF COLUMN 'a' LABEL 'DURK' \n",pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"])['a']["DURK"])
# FOR RETRIEVING ROWS, USE loc OR iloc
# loc and iloc WORK WITH '[ROWS], [COLUMNS]'
print("DATAFRAME OF ROW '1' \n",pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"]).loc[1])
print("DATAFRAME OF ROW AT POSITION (1,3), 2 \n",pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"]).iloc[[1,3],2])
print("DATAFRAME OF COLUMN 'a' and 3.7 \n",pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"])[['a',3.7]])

murk = pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"])
murk['NEW SERIES'] = murk['a']**murk[3.7] + numpy.sin(murk[6.7])
# CAN ALSO ADD A PRE-MADE SERIES OR A LIST, AS LONG AS DIMENSIONS WITH NUMBERS OF ROWS MATCH
print("CREATING A NEW SERIES WITH ARITHMETIC ON OLD SERIES \n",murk)
# REMOVING SERIES/COLUMNS OR LABELS:
# murk = murk.drop('NEW SERIES',1)
# murk = murk.drop([1,"DURK"],0)
# ROWS ARE 0 AXIS, COLUMNS 1 AXIS
print("CREATING A NEW SERIES WITH SERIES AND LABELS REMOVED \n",murk.drop('NEW SERIES',1).drop([1,"DURK"],0))
print("DATA FRAME OF A DICTIONAIRY USED FOR STEP HEREAFTER \n",pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]))
print("REMOVING ROWS WITH NAN OF PREVIOUS DATA FRAME WITH THRESHOLD OF AMOUNT OF NON-NAN-VALUES \n",
pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]).dropna(0,thresh=3))
print("REMOVING COLUMNS WITH NAN OF PREVIOUS DATA FRAME \n",pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]).dropna(1))
print("REPLACING ALL NAN OF PREVIOUS DATA FRAME WITH 'DURK' \n",pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]).fillna('DURK'))
print("REPLACING ALL NAN OF PREVIOUS DATA FRAME WITH MEAN OF DATA FRAME \n",
pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]).fillna(pandas.DataFrame(exemplum,['b',3,"DURKUDURK"]).mean()))
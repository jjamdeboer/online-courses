import numpy
import pandas

label = ['one',[1,2.4],6.7,{3,7,6}]
values = [1,1,2,1]
value_array = numpy.array(values)
label_value_pair = {'DURK':{1:2,5:9000}, 'DURKUDURK':['HELLO DURK',8.9], 'DURKUDURKUDURK':numpy.array(values)}
exemplum = {1:[5,6,7.6],'a':[2,3.4,4],"DURK":[numpy.nan,numpy.nan,3]}
murk = pandas.DataFrame(numpy.random.rand(4,5),
[1,"HELLO","DURK","DURK"],
['a',3.7,"DURK",6.7,"DURK"])

# GROUPING BY DATA:
grouping_dictionairy = {'a':[1,1,2,2,3,3],'DURK':[2,3,4,5,6,7]}
print("DATA FRAME OF DICTIONAIRY \n", d := pandas.DataFrame(grouping_dictionairy,['b',3,"DURKUDURK",4,6.7,7]) )
# OTHER FUNCTIONS ARE 'count', 'max', 'min', 'std', 'sum', 'mean', 'describe' (ALL PREVIOUS ONES)
print("GROUPING DATA FRAME OF DICTIONAIRY BY 'a' AND THEN TAKE MEAN OF GROUP \n", d.groupby('a').mean())
print("SORTING BY VALUES IN COLUMN 'a' AND INDEX 'b': \n", d.sort_values('a', axis = 0),
'\n', d.sort_values('b', axis = 1))
print( '\n\n\n\n' )

# CONDITIONAL SELECTION (ALSO BOOLEAN, LIKE WITH NUMPY):
# THE RETURN VALUE IS ALSO A DATAFRAME!
print("CONDITIONAL SELECTION OF ALL ROWS WHERE RANDOM GENERATED MATRIX IN COLUMN 'a' > 0.5 \n", ( r:= pandas.DataFrame(numpy.random.rand(3,4),
[1,"HELLO","DURK"],
['a',3.7,"DURK",6.7]) )[r['a']>0.5])
# EVEN MULTIPLE CONDITIONS ARE POSSIBLE
# DON'T USE 'and' 'or' BUT USE & | INSTEAD TO COMPARE SERIES 
print("PREVIOUS CONDITION AND WHERE COLUMN 6.7 > 0,01, SO STACKED CONDITIONS \n", r[
( r[ 'a' ] > 0.5 ) & ( r[ 6.7 ] > 0.01 )
])
print("CONDITIONAL SELECTION WHERE RANDOM GENERATED MATRIX > 0.5 AND THE COLUMNS ARE 'a' AND 3.7 \n", r[r[['a',3.7]]>0.5])
print( '\n\n\n\n' )
# FOR HIERARCHIC DATA FRAMES, USE METHOD .xs(ROW NAME, level = LEVEL OF THE ROW)

# CONCATINATION (REMINDER: ROWS ARE 0 AXIS, COLUMNS 1 AXIS):
print("CONCATINATION ON ROWS: \n",pandas.concat([murk,murk],axis = 0))
print("CONCATINATION ON COLUMNS: \n",pandas.concat([murk,murk],axis = 1))

# MERGING:
print("MERGING ON COLUMNS 'a' AND '6.7': \n", pandas.merge(murk, murk, how = 'inner', on = ['a',6.7]))

# JOINING (IS SAME AS MERGING, BUT THEN ON INDEX INSTEAD OF SPECIFIC COLUMNS):
#  DEFAULT BEHAVIOUR IS LEFT JOIN, BUT CAN BE SPECIFIED
print("LEFT-JOINING PREVIOUS DATA FRAME AND A RANDOM OTHER ONE: \n", t := murk.join( v := pandas.DataFrame(numpy.random.rand( 4, 2 ) ) ) )
#  THIS IS ALMOST IDENTICAL TO CONCAT ON AXIS = 1, ALBEIT THAT IT ALLOW FOR NON-UNIQUE INDICES, WHEREAS CONCAT DOES NOT
print("OUTER-JOINING LAST STEP: \n", murk.join( v, how = 'outer' ) )
print("NOW TWO OTHER DATAFRAMES WITH CONCAT (FOR COMPARISON): \n",pandas.concat([r,v],axis = 1))
print( '\n\n\n\n' )

# FINDING UNIQUE VALUES:
print("UNIQUE VALUES IN COLUMN 'a' IN DATA FRAME: \n", t['a'].unique())
print("NUMBER OF UNIQUE VALUES IN COLUMN 'a' IN DATA FRAME: \n", t['a'].nunique())
print("RETURNING COUNT OF EACH VALUE IN COLUMN 'a' IN DATA FRAME: \n ", t['a'].value_counts())

# APPLYING OTHER FUNCTIONS ON A COLUMN, THAN BUILT-IN FUNCTIONS:
#  DIFFERENCE APPLY, MAP AND APPLYMAP IS THAT MAP IS FOR SERIES AND APPLYMAP FOR DATAFRAMES, WHEREAS APPLY IS FOR BOTH
print("APPLYING TIMES 30 TO EVERY VALUE (APPLYMAP): \n", murk.applymap( lambda x: x*30 ) )
print("APPLYING TIMES 30 TO EVERY ONE COLUMN (MAP): \n", murk['a'].map( lambda x: x*30 ) )
#  print("APPLYING TIMES 30 TO SUM OF TWO COLUMNS (APPLY): \n", murk[['DURK']] )
#  print("APPLYING TIMES 30 TO SUM OF TWO COLUMNS (APPLY): \n", murk[['DURK']].apply( lambda x,y: (x+y)*30, axis = 1 ) )
print("APPLYING TIMES 30 TO SUM OF TWO COLUMNS 'DURK' (APPLY): \n", murk[['DURK']].apply( lambda x: 30 * numpy.sum(x), axis = 1 ) )
print("APPLYING TIMES 30 TO SUM OF ALL ROWS FOR TWO COLUMNS 'DURK' (APPLY): \n", murk[['DURK']].apply( lambda x: 30 * numpy.sum(x), axis = 0 ) )

# FOR READING CSV-FILES, USE pandas.read_csv('path or filename')
# FOR READING EXCEL-FILES WITHOUT IMAGES, FORMULAS AND MACROS, USE pandas.read_excel('path or filename')
# FOR READING SQL-FILES, USE pandas.read_sql('path or filename')
# FOR READING SQL-TABLES, USE pandas.read_sql_table('path or filename')
# FOR READING HTML-FILE, USE pandas.read_html('path or filename or webaddress') RETURNS A LOT OF DATA, THE 0TH ELEMENT IS THE DATA FRAME
# FOR READING JSON-FILE, USE pandas.read_json('path or filename')

# FOR WRITING CSV-FILES, USE pandas.to_csv('path or filename')
# FOR WRITING EXCEL-FILES WITHOUT IMAGES, FORMULAS AND MACROS, USE pandas.to_excel('path or filename')
# FOR WRITING SQL-FILES, USE pandas.to_sql('path or filename')
# FOR WRITING SQL-TABLES, USE pandas.to_sql_table('path or filename')
# FOR WRITING HTML-FILE, USE pandas.to_html('path or filename')
# FOR WRITING JSON-FILE, USE pandas.to_json('path or filename')

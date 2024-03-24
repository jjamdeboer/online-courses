#  MATPLOTLIB IS THE DE FACTO STANDARD FOR DATA ANALYSIS
#  SEABORN IS HEAVILY BASED ON SEABORN

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#####  MATPLOTLIB
#  OBJECT-ORIENTED WAY TO CREATE SUBPLOTS
#  NOTE THAT AXES ARE ARRAY HERE, SO ONE CAN INDEX IT
#  NOTE THE ADDITIONAL FIGSIZE PARAMETER TO TWEAK THE SIZE OF THE FIGURE
canvas, axes = plt.subplots( figsize = ( 14, 8 ), nrows = 1, ncols = 2 ) 
#  LINE PLOT:
axes[0].plot( 
    np.arange( 0, 99, 2 ), 
    np.linspace( -10, 20, 50 )**3,
    linewidth = 5,
    c = 'darkgreen',
)
axes[0].set_xlabel("RANGE")
axes[0].set_ylabel("I'VE GOT THE POWER OF 3")
axes[0].set_title("OBJECT-ORIENTED LINE")
#  SCATTER PLOT
axes[1].scatter( 
    data = ( a := pd.DataFrame( np.random.randn( 125, 4 ), columns = [ 'durk', 'murk', 'durkudurk', 'murkumurk' ] ) ), 
    x = 'durk', 
    y = 'murk',
    label = 'labiel',
    s = np.abs( a['durkudurk'] ) * 50,
    c = 'murkumurk',
    edgecolor = 'black',
    linewidth = 3,
    cmap = 'plasma',
)
axes[1].set_xlim( -3, 3 )
axes[1].set_ylim( -5, 5 )
axes[1].set_xlabel("DURK")
axes[1].set_ylabel("MURK")
axes[1].set_title("OBJECT-ORIENTED SCATTER")
axes[1].legend()
# TO CREATE AXES THAT ARE FURTHER APART:
plt.tight_layout()
plt.show()

#####  SEABORN
heart = pd.read_csv( 'heart.csv' )
#  OBJECT-ORIENTED WAY TO CREATE SUBPLOTS
#  NOTE THAT AXES ARE ARRAY HERE, SO ONE CAN INDEX IT
#  NOTE THE ADDITIONAL FIGSIZE PARAMETER TO TWEAK THE SIZE OF THE FIGURE
canvas, axes = plt.subplots( figsize = ( 14, 8 ), nrows = 1, ncols = 2 ) 
sns.histplot(  
    x = 'age', 
    data = heart, 
    ax = axes[0], 
    kde = False, 
    palette = 'plasma', 
    linewidth = 5, 
    hue = 'sex', 
    bins = 10 
)
sns.violinplot(  
    x = 'sex', 
    y = 'age', 
    data = heart, 
    ax = axes[1], 
    palette = 'plasma', 
    hue = 'target', 
    fill = False, 
    linewidth = 5, 
    orient = 'v', 
    split = True, 
    bins = 10 
)
axes[0].set_title("OBJECT-ORIENTED HISTPLOT")
axes[1].set_title("OBJECT-ORIENTED VIOLINPLOT")
plt.tight_layout()
plt.show()

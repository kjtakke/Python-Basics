import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

#https://matplotlib.org/

#print(pd.DataFrame(plt.style.available))
#Styles
#        Solarize_Light2
#    _classic_test_patch
#                    bmh
#                classic
#        dark_background
#                   fast
#       fivethirtyeight
#                ggplot
#             grayscale
#                seaborn
#        seaborn-bright
#    seaborn-colorblind
#          seaborn-dark
#  seaborn-dark-palette
#      seaborn-darkgrid
#          seaborn-deep
#         seaborn-muted
#      seaborn-notebook
#         seaborn-paper
#        seaborn-pastel
#        seaborn-poster
#          seaborn-talk
#         seaborn-ticks
#         seaborn-white
#     seaborn-whitegrid
#  tableau-colorblind10


# Markers
# https://matplotlib.org/api/markers_api.html?highlight=markers#module-matplotlib.markers

#   Linestyle	        Description
#   '-' or 'solid'	    solid line
#   '--' or 'dashed'	dashed line
#   '-.' or 'dashdot'	dash-dotted line
#   ':' or 'dotted'	    dotted line

# Colors:
#  https://htmlcolorcodes.com/

#print(df)  # country  year  pop continent  lifeExp   gdpPercap
            # Asia  Africa


#Pandas_________________________________________________________________________
path = r"http://bit.ly/2cLzoxH"
df = pd.read_csv(path)



#PLOT CHART
#_______________________________________________________________________________
#Style__________________________________________________________________________
plt.style.use('seaborn-poster')
plt.figure(figsize=(16,8))

plt.grid()
plt.title('Mean Life Exp')


#_______________________________________________________________________________
#Data___________________________________________________________________________

    #Plot 1
#plt.subplot(221, frameon=False) #Subplot (Top Left)
        #Data
df_pivot = df.pivot_table(index=['year'],  values=['lifeExp'], aggfunc=np.mean)
df_unpivot = pd.DataFrame(df_pivot.to_records())
#print(df_unpivot)

        #Plt
x_year = df_unpivot[['year']]
y_Life_Exp = df_unpivot[['lifeExp']]
plt.plot(x_year, y_Life_Exp, color='#DF2C06', linewidth=3, label='All')

    #_______________________________________________________________________________

    #Plot 2
#plt.subplot(222, frameon=False) #Subplot (Top Right)
        #Data
df_filtered = df[df['continent'] == 'Africa']
df_pivot = df_filtered.pivot_table(index=['year'],  values=['lifeExp'], aggfunc=np.mean)
df_unpivot = pd.DataFrame(df_pivot.to_records())
#print(df_unpivot)

        #Plt
x_year = df_unpivot[['year']]
y_Life_Exp = df_unpivot[['lifeExp']]
plt.plot(x_year, y_Life_Exp, color='#47588F', linewidth=3, label='Africa', linestyle='--')

    #Plot 3
#plt.subplot(223, frameon=False) #Subplot (Top Right)
        #Data
df_filtered = df[df['continent'] == 'Asia']
df_pivot = df_filtered.pivot_table(index=['year'],  values=['lifeExp'], aggfunc=np.mean)
df_unpivot = pd.DataFrame(df_pivot.to_records())
#print(df_unpivot)

        #Plt
x_year = df_unpivot[['year']]
y_Life_Exp = df_unpivot[['lifeExp']]
plt.plot(x_year, y_Life_Exp, color='#47588F', linewidth=3, label='Asia', linestyle='--')

#_______________________________________________________________________________

    #Plot 3
#plt.subplot(224, frameon=False) #Subplot (Top Right)
        #Data
df_filtered = df[df['continent'] == 'Europe']
df_pivot = df_filtered.pivot_table(index=['year'],  values=['lifeExp'], aggfunc=np.mean)
df_unpivot = pd.DataFrame(df_pivot.to_records())
#print(df_unpivot)

        #Plt
x_year = df_unpivot[['year']]
y_Life_Exp = df_unpivot[['lifeExp']]
plt.plot(x_year, y_Life_Exp, color='#8F4755', linewidth=3, label='Europe', linestyle='--')

#_______________________________________________________________________________
#Display________________________________________________________________________

plt.legend()
plt.show()

#_______________________________________________________________________________










#BAR & BARH CHART
#_______________________________________________________________________________
#Style__________________________________________________________________________

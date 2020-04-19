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
#plt.style.use('seaborn-poster')
#plt.figure(figsize=(16,8))

#plt.grid()
#plt.title('Mean Life Exp')


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
#plt.plot(x_year, y_Life_Exp, color='#DF2C06', linewidth=3, label='All')

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
#plt.plot(x_year, y_Life_Exp, color='#47588F', linewidth=3, label='Africa', linestyle='--')

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
#plt.plot(x_year, y_Life_Exp, color='#47588F', linewidth=3, label='Asia', linestyle='--')

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
#plt.plot(x_year, y_Life_Exp, color='#8F4755', linewidth=3, label='Europe', linestyle='--')

#_______________________________________________________________________________
#Display________________________________________________________________________

#plt.legend()
#plt.show()

#_______________________________________________________________________________







#BAR & BARH CHART
#_______________________________________________________________________________
#Style
#plt.style.use('seaborn-poster')
#plt.figure(figsize=(16,8))
#plt.grid()



#Data
df_pivot = df.pivot_table(index=['year'],  values=['lifeExp'], aggfunc=np.mean)
df_unpivot = pd.DataFrame(df_pivot.to_records())


#Convert to x and y lists
xy = pd.DataFrame(df_unpivot)
x = list(xy['year'])
x = list(map(str,  x)) # used to convert a list of Numbers to a list of strings
y = list(xy['lifeExp'])

#Show Lables
#plt.title('Life Exp')
#plt.xlabel('Year')
#plt.xlabel('Average')

#Show Chart
#plt.bar(x,y)
#plt.show()




#_______________________________________________________________________________


#Style
#plt.figure(1, figsize=(16,8))
#window_color = plt.figure(1)
#plt.grid(1)
#window_color.patch.set_facecolor('#999999')
#plt.style.use('seaborn-poster')


#Data
df_pivot = df.pivot_table(index=['continent'],  values=['lifeExp'], aggfunc=np.mean)
df_unpivot = pd.DataFrame(df_pivot.to_records())


#Convert to x and y lists
xy = pd.DataFrame(df_unpivot)
x = list(xy['continent'])
y = list(xy['lifeExp'])


#Show Lables
#plt.title('Life Exp')
#plt.xlabel('Continent')
#plt.xlabel('Average')


#Show Chart
#plt.barh(x,y, color='#478F4B')
#bg_color = plt.gca()
#bg_color.set_facecolor('#999999')
#plt.show()








#_________________________________________________________________________
#PIE CHART
xy = pd.DataFrame(df_unpivot)
x = list(xy['continent'])
y = list(xy['lifeExp'])


#Creating a list of explode widths
explode = []
for i in x:
    explode.append(0.1)
#print(explode)
#plt.figure(1, figsize=(12,8))
#Colours
color_set = ('#478F4B', '#8F6A47', '#47758F', '#8F8C47', '#8F474F', '#48478F', '#8F476D', '#82478F')

#Create Chart
#plt.pie(y, labels=x, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%', colors=color_set)

#Show Chart
#plt.legend(x, bbox_to_anchor=(1.1, 1.05))
#plt.show()






#HISTOGRAM____________________________________________________________________________________

#Filter Data
#df = df[df['year'] > 2000]

#Styles
#plt.figure(1, figsize=(16,8))
#window_color = plt.figure(1)
#window_color.patch.set_facecolor('#999999')
#plt.style.use('seaborn-poster')
#plt.grid(1)

#Lables
#plt.title('Life Exp')
#plt.xlabel('Continent')
#plt.xlabel('Histogram')

#Create Chart                                     Types: bar', 'barstacked', 'step', 'stepfilled
#plt.hist('lifeExp', bins=[i for i in range(100)], histtype='bar', data=df, color='#478F4B')

#Show
#bg_color = plt.gca()
#bg_color.set_facecolor('#999999')
#plt.show()
print(df)

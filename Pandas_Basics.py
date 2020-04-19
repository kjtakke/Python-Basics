import pandas as pd
from pandas import DataFrame
import numpy as np


cars = [["Ford", "Red"], ["Volvo", "Blue"], ["BMW", "Green"]]
#print(cars)

#print(pd.DataFrame(cars))
cars.append(["Holden","Purple"])
#print(pd.DataFrame(cars))




cars_columns = ["Make", "Colour"]
cars = pd.DataFrame(cars, columns=cars_columns)
#print(cars)


#print(cars[["Make"]])

cars_row_count = np.size(cars[["Make"]])
#print(cars_row_count)

cars = pd.DataFrame(cars, columns=cars_columns, index=range(1, cars_row_count))
#print(cars)







#From CSV____________________________________________________________
path = r"http://bit.ly/2cLzoxH"

df = pd.read_csv(path)
#print(df.head())
#print(df.describe())

#print(df.isnull())

#print(df[['year','lifeExp']])

#print(df.iloc[1:3])

#print(df.mean())
#print(df[['lifeExp']].mean())
#print((df[['lifeExp']].max()))
#print((df[['lifeExp']].sum()))
#print((df[['lifeExp']].std()))






#Filtering
#print(df[df['year'] > 2000])
#print(df[[df['year'] > 2000] and df['lifeExp'] < 50])

# or statment
df2 = df[df['year'] > 2000]
#print(df2)

df3 = df[df['lifeExp'] < 50]
#print(df3)

df4 = df2.append(df3)
#print(df4)









# Pivots and Charts
df_pivot = df.pivot_table(index=['country'], columns=['continent'], values=['lifeExp'], aggfunc=sum )
#print(df_pivot)
df5 = df[df['continent'] == 'Americas']
#print(df5)


df_pivot2 = df5.pivot_table(index=['country'], values=['lifeExp', 'gdpPercap'], aggfunc=sum )
#print(df_pivot2)

import matplotlib
from matplotlib import pyplot as plt
#df_pivot2.plot.barh(figsize=(8,8))
#plt.show()
#print(df)


df_bar = df.pivot_table(index=['year'], values=['lifeExp'], aggfunc=np.mean)
#print(df_bar)
#df_bar.plot.barh(figsize=(8,8))
#plt.show()


#plt.scatter(data=df, x='lifeExp', y='gdpPercap')
#plt.show()

#plt.hist('lifeExp', bins=[i for i in range(100)], histtype='bar', data=df)
#plt.show()

df_pivot = df.pivot_table(index=['year'], values=['lifeExp'], aggfunc=np.mean)
#df_pivot.plot()
#plt.show()

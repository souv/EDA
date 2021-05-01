#descriptive stats : measure of center, variability , quantile , table and graphs
import seaborn as sns
import pandas as pd

#descriptive stats: 
#1.you want to know the mean of all the customer spend a month.
#2.you can draw a histogram that show the customer spend in a month to know the trend.
#3.you can draw different card type customer spend in a month together to see the difference.
#4.you can use boxplot to see the quantile of each card type customer.
#5.you can also draw the rfm distribution to track the customers behavior.
#6.rebuy rate and loss rate
#7.see the customer spend sd:standard_deviation = df['Price'].std()
#8.if you want to see the spending sd through categories, you should use cv instead.
#9.draw some plot 
#draw boxplot to see the quantile of num data
sns.set(style="whitegrid")
plt.figure(figsize=(10,8))
ax = sns.boxplot(x='Type', y='real_amount', data=orderdata, orient="v")

#draw dist plot to see the distribution of the num data
plt.figure(figsize=(14,8))
sns.distplot(filter_data['Price'], kde=False)

#draw piechart 
type_counts = df['card_type'].value_counts()
df2 = pd.DataFrame({'card_type': type_counts}, 
                     index = ['b', 'g', 'w']
                   )
df2.plot.pie(y='card_type', figsize=(10,10), autopct='%1.1f%%')

#draw barchart
sns.set(style='darkgrid')
plt.figure(figsize=(20,10))
ax = sns.countplot(x='Regionname', data=df)

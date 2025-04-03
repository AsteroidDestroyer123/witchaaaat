import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import sklearn.linear_model
import csv
df=pd.read_csv('датасет-1.csv',sep=';')

df['price']=df['price'].str.replace(',','.') 
df['price']=df['price'].astype(float)



reg = sklearn.linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

a=reg.coef_
b=reg.intercept_
plt.scatter(df.area,df.price,color='red')
plt.plot(df.area,reg.predict(df[['area']])) 
plt.xlabel('площадь(кв.м.)') 
plt.ylabel('стоимость(млн.руб)')
plt.show() 
data_predict=pd.read_csv('prediction_price.csv',sep=';')

predictions = reg.predict(data_predict[['area']])
print(predictions)

output_df = data_predict.copy()
output_df['Predicted Price'] = predictions



output_df.to_excel('predicted_prices.xlsx', index=False)

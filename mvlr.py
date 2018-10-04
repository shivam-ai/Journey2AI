import numpy as np 
import pandas as pd 
import sys

np.random.seed(42)
a= np.random.randint(1, 25, 5)
b= np.random.randint(100, 1000, 5)
c= 11 + 2 * a + 5 * b

#a= a/ (max(a) - min(a))
#b= b/ (max(b) - min(b))
#c= c/ (max(c) - min(c))

"""
data= pd.DataFrame({"TV":a, "Radio":b, "Sales":c})
X= data[['TV','Radio']]
y= data['Sales']
#print(data.head(2))

"""
data= pd.read_csv('Files/Advertising.csv', index_col= 0)
feature_cols= ['TV', 'Radio', 'Newspaper']
target_col= 'Sales'
X= data[feature_cols]
y= data[target_col]




m= X.shape[0]
n= X.shape[1]

X= X.values
y= y.values


print("XX",(X[:,0]/ (max(X[:,0]) - min(X[:, 0]))))
print("max",max(X[:, 0]))


X= X/ (X.max(axis=0) - X.min(axis= 0))
y= y/ (max(y) - min(y))


from sklearn.linear_model import LinearRegression
linreg= LinearRegression()
linreg.fit(X, y)
print(linreg.intercept_, linreg.coef_)
print("+"*70)




n+=1
X= np.insert(X, 0, 1, axis= 1)

print("X",X)
print("y",y)

y= y[None]
y= y.transpose()
print("X:",X.shape)
print("y:",y.shape)






alpha= 0.1
theta= (np.ones(n)*10)[None]
theta= theta.transpose()
print("theta:",theta.shape)


print("X",X)
print("y",y)
print("Theta",theta)

"""
prediction= np.dot(X, theta)
print("Pred:",prediction)

error= (prediction - y)**2
print("Error:",error.shape)
cost= sum(error) / m
cost = cost / 2.0
temp= prediction - y
print("temp:",temp)

temp= temp.transpose()
temp= np.dot(temp, X)
print("temp2:",temp)


temp= temp * alpha
temp= temp / m
temp= temp.transpose()
print("temp3:",temp)


theta= theta - temp
print("theta:",theta.shape)
print("{}. Cost: {}, theta: {}".format(i,cost,theta))
"""




print("="*50)
import math
pc= math.inf
change= 1
i=0
while(change>0.000000000001):
    hyp= np.dot(X, theta)
    temp= (hyp - y)
    temp= temp.transpose()
    temp= np.dot(temp, X)
    temp= temp * alpha
    temp= temp / m
    temp= temp.transpose()
    theta= theta - temp

    prediction= np.dot(X, theta)
    error= (prediction - y)**2
    cost= sum(error) / m
    cost = cost / 2.0
    change= pc - cost
    pc= cost
    i+=1
    if(i%10==0):
        print("{}. Cost: {}, theta: {}".format(i, cost, theta.transpose()))

print("+"*70)
print("sklearn: theta: ",linreg.intercept_, linreg.coef_)
print("+"*70)
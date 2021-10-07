#!/usr/bin/env python
# coding: utf-8

# project regarding preprocessing

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# ****Hai this is my project regarding preprocessing****

# In[12]:


#read dataset
df=pd.read_csv("/Users/subhasree/Desktop/My project/train.csv")


# pip install seaborn for installing packages if not present
# 
# the following code simply prints the column details

# In[14]:


print("The columns are")
s = list(df.columns.values)
for i in range(1,len(s)):
    print(i,". ",s[i])


# #dropping a column from dataset(just for my reference)
# print("please enter the target variable")
# target=input()
# print("You have opted", target,"are you sure (Y/N)")
# op=input()
# if op == 'y' or op == 'Y':
#     df.drop([target],axis=1,inplace=True)
#     print("Dropped successfully")
# else:
#     print("kindly enter correct option")
# 

# In[15]:


class data_desc:
        
    def menu(self):
        print("******* Menu *********")
        while (True):
            print("Task - Data Description")
            print(" 1. Describe each column\n 2. show properties of each column\n 3. show data set\n")
            print("What do you want to do? press -1 for exit")
            chdd=int(input())
            if chdd == 1:
                dd_obj.desc()
                
            elif chdd == 2:
                dd_obj.prop()
                
            elif chdd == 3:
                dd_obj.show()
                
            elif chdd == -1:
                print("thank you")
                break
        return
            
#A function that shows properties (mean, standard deviation, percentiles, total number of values, maximum, minimum) of each numeric column. This function should also show the datatypes along with the null value count of each column.           
        
    def desc(self):
         s = list(df.columns.values)
         for i in range(1,len(s)):
             print(s[i])
         print("Which Column?")
         c=input("enter column name")
         df1=df.dropna()
         print("Count",df1[c].count())
         print("mean",df1[c].mean())
         print("std",df1[c].std())
         print("min",df1[c].min())
         print("25%",np.percentile(df1.Age,25))
         print("50%",np.percentile(df1.Age,50))
         print("75%",np.percentile(df1.Age,75))
         print("max",df1[c].max())
        
#A function that shows the property of any specific column.

    def prop(self):
        df.info()
        df.describe()

#A function that takes a number of rows as input and prints the dataset. 
        
    def show(self):
        print("How many cols do u want to print(>0)")
        h=int(input())
        print(df[1:h+1])


# In[16]:


class handle_nul():
        
    def menu(self):
        while (True):
            print("Task - Handling Null Values")
            print(" 1. Show no of null values\n 2. remove columns\n 3. fill null values (with mean) \n 4. fill null values (with median) \n 5. fill null values (with mode) \n 6. Show dataset\n")
            print("What do you want to do? press -1 for exit")
            chdd=int(input())
            
            if chdd == 1:
                hn_obj.show_nul()
                
            if chdd == 2:
                hn_obj.remov()
                
            if chdd == 3:
                hn_obj.fill_mean()
            
            if chdd == 4:
                hn_obj.fill_median()
            
            if chdd == 5:
                hn_obj.fill_mode()
                
            if chdd == -1:
                break


    def show_nul(self):
        print("Null values of each column:")
        print(df.isnull().sum())   
   
#function that removes the specified column.   

    def remov(self):
        print("The columns are")
        s = list(df.columns.values)
        print(s)
        print("please enter the target variable")
        target=input()
        print("You have opted", target,"are you sure (Y/N)")
        op=input()
        if op == 'y' or 'Y':
            df.drop([target],axis=1,inplace=True)
        else:
            print("you have not clarified")
            
#Three respective functions that fill the null values in a column with mean, median and mode.



    def fill_mean(self):
        print("The columns are")
        s = list(df.columns.values)
        print(s)
        print("please enter the target variable")
        target=input()
        print("You have opted", target,"are you sure (Y/N)")
        op=input()
        if op == 'y' or 'Y':
            df[target].fillna(df[target].mean(),inplace = True)
        else:
            print("you have not clarified")
        
    def fill_median(self):
        print("The columns are")
        s = list(df.columns.values)
        print(s)
        print("please enter the target variable")
        target=input()
        print("You have opted", target,"are you sure (Y/N)")
        op=input()
        if op == 'y' or 'Y':
            li=[]
            for i in df[target]:
                if len(str(i))==1:
                    li.append(ord(i))
            df[target].fillna(statistics.median(li),inplace = True)
        else:
                print("you have not clarified")
        
    def fill_mode(self):
        print("The columns are")
        s = list(df.columns.values)
        print(s)
        print("please enter the target variable")
        target=input()
        print("You have opted", target,"are you sure (Y/N)")
        op=input()
        if op == 'y' or 'Y':
            li=[]
            for i in df[target]:
                if len(str(i))==1:
                    li.append(ord(i))
            df[target].fillna(statistics.mode(li),inplace = True)
        else:
            print("you have not clarified")
            
   



# In[17]:



class encode_cat():
        
    def menu(self):
        while (True):
            print("Task - Encode categorical data")
            print(" 1. Show Catagorical columns\n 2. Perform one hot encoding\n 3. Show dataset\n")
            print("What do you want to do? press -1 for exit")
            chdd=int(input())
            if chdd == 1:
                eobj.show_col()
                
            if chdd == 2:
                eobj.hot_encode()
                
            if chdd == 3:
                eobj.show()
                
            if chdd == -1:
                break
                
        
    def show_col(self):
      
        s = (df.dtypes == 'object') #selecting type as object and not numeric
        object_cols = list(s[s].index)
        print(object_cols) 
        #df.columns=['Catagorical column','unique value']
        for i in object_cols:
            print(i,"  ",df[i].nunique())
        print("---Catagorical")
         
            
    def hot_encode(self):
        
        while(True):
            print("please enter the target variable to hot encode or enter -1 to go back")
            target=input()
            if target != '-1':
                print("You have opted", target,"are you sure (Y/N)")
                op=input()
                if op == 'y' or 'Y':
                    labelencoder_X = LabelEncoder()    
                    df[target] = labelencoder_X.fit_transform(df[target])#it will hotencode and removes
                else:
                    print("confirm ")
            else:
                print("Exiting")
                break
                

    def show(self):
        print("How many cols do u want to print(>0)")
        h=int(input())
        print(df[1:h+1])


# In[18]:


#df=pd.read_csv("/Users/subhasree/Desktop/My project/train.csv")
class feature_scaling():
   

    #A function that performs normalization of any specific column or group of columns.
    def normalization(self):
        while(1):
            print("1. Normalize specific column ")
            print("2. Normalize group of column")
            print("3. Show dataset")
            df=pd.read_csv("/Users/subhasree/Desktop/My project/train.csv")
            op=int(input("Enter your option"))
            if op==1:
                print("Hai")
                s = (df.dtypes != 'object') #selecting type as object and not numeric
                object_cols = list(s[s].index)
                print(object_cols) 
                print("Enter the column names u want to normalize?")
                col=input()
                df_min_max_scaled = df.copy()

                # apply normalization technique
                df_min_max_scaled[col] = (df_min_max_scaled[col] - df_min_max_scaled[col].min()) / (df_min_max_scaled[col].max() - df_min_max_scaled[col].min())    

                # view normalized data
                display(df_min_max_scaled)

            elif op==2:
                x = df.values #returns a numpy array
                for i in df.dtypes:
                    if i != 'object':
                        min_max_scaler = preprocessing.MinMaxScaler()
                        x_scaled = min_max_scaler.fit_transform(x)
                        df = pd.DataFrame(x_scaled)    
                print(df)
            elif op==3:
                print(df)
            else:
                print("please enter correct option")
                break
    
    def show_dataset():
        print("How many cols do u want to print(>0)")
        h=int(input())
        print(df[1:h+1])




# In[ ]:


#Main program for preparing dataset and preprocessing

while(1):
    print("Lets Start Task Prepocessing")
    print(" 1. Data Description\n 2. Handling NULL values\n 3. Encoding Categorical Data\n 4.Feature Scaling\n 5. Download modified dataset")
    print("What do you want to do? press -1 for exit")
    ch=int(input())
    if ch == 1:
        dd_obj=data_desc()#object for data desc class
        dd_obj.menu()
    elif ch == 2:
        hn_obj=handle_nul()#object for handle null class
        hn_obj.menu()
    elif ch==3:
        eobj=encode_cat()#object for categorical class
        eobj.menu()
    elif ch == 4:
        fobj=feature_scaling() #object for feature scaling class
        fobj.normalization()
    elif ch==5:
        df.to_csv('output.csv', index=False)
        print("fdgfg")
        break
    elif ch == -1:
        exit()
    else:
        print("Enter correct option (1-5) and -1 to exit")
        break


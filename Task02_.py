import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
df.drop(['Cabin','PassengerId','Name','Ticket'],axis=1,inplace=True) #dropped ,that is removed cuz they are of no use and provide no useful data
#age and embarked have missing values ,fillna couldbe used 
miss_age = df['Age'].median()#median as its numerical value
df['Age'].fillna(miss_age,inplace=True)
#for embarked(mode is to be used as text)
miss_mode = df['Embarked'].mode()[0]
df['Embarked'].fillna(miss_mode,inplace=True)
#providing gender with unique value as machine only understand numeric value and similar for embarked 
df['Sex'] = df['Sex'].map({'male': 0 , 'female': 1})
#embarked 
df = pd.get_dummies(df , columns=['Embarked'] , drop_first=True)

# Performing EDA 

# More women survived than men. This shows gender played an important role
sns.barplot( x= 'Sex' , hue= 'Survived' , data=df , palette="viridis")
plt.show()

# 1st class passengers had better chances of survival than 2nd or 3rd class. People in 3rd class survived the least
plt.figure(figsize=(7,5))
sns.barplot( x= 'Pclass' , hue= 'Survived' , data=df , palette="viridis")
plt.show()

# Most ages look similar, but younger kids had a slightly higher chance of survival compared to older people
plt.figure(figsize=(6,5))
sns.boxplot(x='Sex', y='Age',hue='Survived', data=df ,palette="Set2")
plt.tight_layout()
plt.show()

# Survivors generally paid higher fares. Richer passengers had better chances to survive.
plt.figure(figsize=(6,5))
sns.boxplot(x='Pclass', y='Fare',hue='Survived',dodge=False, data=df)
plt.yscale('log')
plt.show()

''' Survival is linked to passenger class and fare.

 Age doesn’t matter much.

 Pclass and Fare are strongly related (rich people → higher class → survived more) '''
sns.heatmap(df.corr(), annot=True , cmap='coolwarm')
plt.show()

# Women in 1st and 2nd class survived the most. Men in 3rd class survived the least. This combines both gender and class effects.

sns.catplot(x='Pclass', hue='Sex', col='Survived', kind='count',data=df  )
plt.show()  
df.info()
'''From this analysis:

Women had higher survival chances.

1st class > 2nd class > 3rd class in survival.

Paying higher fares (rich passengers) helped survival.

Children survived more than older passengers.


So survival mainly depended on gender + class + wealth.'''


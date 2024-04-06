import pandas as pd
import numpy as np
'''
groupby的过程就是将原有的DataFrame按照groupby的字段（这里是company），划分为若干个分组DataFrame
在groupby之后的一系列操作（如agg、apply等），均是基于子DataFrame的操作
'''
company=["A","B","C"]

data=pd.DataFrame({ \
    "company":[company[x] for x in np.random.randint(0,len(company),10)], \
    "salary":np.random.randint(5,50,10), \
    "age":np.random.randint(15,50,10)})
print(data)
# agg
print(data.groupby("company").agg('mean'))
print(data.groupby('company').agg({'salary':'median','age':'mean'}))

# without transform vs transform
# without transform
avg_salary_dict = data.groupby('company')['salary'].mean().to_dict()
data['avg_salary'] = data['company'].map(avg_salary_dict)
print(data)
#with transform
data['avg_salary'] = data.groupby('company')['salary'].transform('mean')
print(data)

#apply
def get_oldest_staff(x: pd.DataFrame) -> pd.DataFrame:
    df = x.sort_values(by='age', ascending=True)
    return df.iloc[-1, :]

oldest_staff = data.groupby('company', as_index=False).apply(get_oldest_staff)
print(oldest_staff)
import pandas as pd

#merge, inner, left, right, outer
#inner:取key的交集
df_1 = pd.DataFrame(
    {
        "userid":['a', 'b', 'c', 'd', 'f'],
        "age":[23, 46, 32, 19, 45],
    }
)

df_2 = pd.DataFrame(
    {
        "userid":['a', 'c', 'a', 'b', 'e'],
        "payment":[2000, 3500, 500, 1000, 200],
    }
)

print(df_1.merge(df_2, how='inner', on='userid'))

#left: 以左表的key为基准进行配对，若左表的key在右表不存在，则用NaN填充
#right，类似left
print(df_1.merge(df_2,how='left',on='userid'))
print(df_1.merge(df_2,how='right',on='userid'))
#outer 取并集
print(df_1.merge(df_2,how='outer',on='userid'))


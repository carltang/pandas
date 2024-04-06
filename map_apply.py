import pandas as pd
import numpy as np


boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
data=pd.DataFrame({
    "height":np.random.randint(150,190,100),
    "weight":np.random.randint(40,90,100),
    "smoker":[boolean[x] for x in np.random.randint(0,2,100)],
    "gender":[gender[x] for x in np.random.randint(0,2,100)],
    "age":np.random.randint(15,90,100),
    "color":[color[x] for x in np.random.randint(0,len(color),100) ]
}
)
print("init data:")
print(data)

#把数据集中gender列的男替换为1，女替换为0
#①使用字典进行映射
data["gender"] = data["gender"].map({"男":1, "女":0})
print("gender map:")
print(data)
#②使用函数
def gender_map(x):
    gender = 1 if x == "男" else 0
    return gender
#注意这里传入的是函数名，不带括号
data["gender"] = data["gender"].map(gender_map)
print("gender map:")
print(data)
'''假设在数据统计的过程中，年龄age列有较大误差，需要对其进行调整（加上或减去一个值），由于这个加上或减去的值未知，故在定义函数时，需要加多一个参数bias，此时用map方法是操作不了的（传入map的函数只能接收一个参数），apply方法则可以解决这个问题'''
def apply_age(x,bias):
    return x+bias

#以元组的方式传入额外的参数，注意参数的传递格式
data["age"] = data["age"].apply(apply_age,args=(-3,))
print("apply age - 3:")
print(data)
# 当axis=0时，对每列columns执行指定函数；当axis=1时，对每行row执行指定函数
# 当沿着轴0（axis=0）进行操作时，会将各列(columns)默认以Series的形式作为参数，传入到你指定的操作函数中，操作后合并并返回相应的结果
# 沿着0轴求和
print("axis=0, sum:")
print(data[["height","weight","age"]].apply(np.sum, axis=0))
# 沿着0轴取对数
print("axis=0, log:")
print(data[["height","weight","age"]].apply(np.log, axis=0))
#沿着1轴计算BMI指数
def BMI(series):
    weight = series["weight"]
    height = series["height"]/100
    BMI = weight/height**2
    return BMI

# 当apply设置了axis=1对行进行操作时，会默认将每一行数据以Series的形式（Series的索引为列名）传入指定函数，返回相应的结果
data["BMI"] = data.apply(BMI,axis=1)
print("axis=1, BMI:")
print(data)

# applemap示例：
df = pd.DataFrame(
    {
        "A":np.random.randn(5),
        "B":np.random.randn(5),
        "C":np.random.randn(5),
        "D":np.random.randn(5),
        "E":np.random.randn(5),
    }
)
print(df.applymap(lambda x:"%.2f" % x))

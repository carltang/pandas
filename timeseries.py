import pandas as pd
import datetime

#切分的频率可以为任何时间频率，可以为季度Q、月度M、星期W、N天ND，也可以为时H、分T
#resample可以对原有的时间序列进行任何频率freq的采样，如果从低频到高频为升采样，高频到低频为降采样。整个操作过程和groupby基本一致，所以也可以对resample后的对象进行apply和transform等操作

#
data = pd.DataFrame(
    {
        "trade_date": ['20190102', '20190109', '20190209', '20190211', '20190307', '20190308', '20190408'],
        'close': [24.07, 25.08, 25.09, 25.18, 25.28, 25.38, 25.48],
        'open': [23.07, 24.09, 25.09, 25.18, 25.28, 25.38, 25.48],
        'high': [23.07, 24.09, 25.09, 25.18, 25.28, 25.38, 25.48],
        'low': [23.07, 24.09, 25.09, 25.18, 25.28, 25.38, 25.48],
    }
)
#当数据中的时间列（本数据中为trade_date列）已经转换为datetime64格式时，仅需调用.dt接口，即可快速求得想要的结果，下表中列出了.dt接口所提供的常见属性：

data["trade_date"] = pd.to_datetime(data.trade_date)
data1 = data.set_index('trade_date')
print(data1.loc['2019-01'])
print(data1.loc['2019-01':'2019-02'])
print(data.trade_date.dt.dayofyear[3])
print(data.trade_date.dt.isocalendar().week[3])
print(data.trade_date.dt.weekday[3])
print(data.trade_date.dt.day_name()[3])
print(data.trade_date.dt.month_name()[3])
print(data.trade_date.dt.quarter[3])
print(data.trade_date.dt.is_leap_year[3])
#降采样，切分的频率可以为任何时间频率，可以为季度Q、月度M、星期W、天D，也可以为时H、分T
print(data.resample('M', on='trade_date')['close'].mean())

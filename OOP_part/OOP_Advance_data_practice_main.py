"""
面向对象,数据分析案例,主业务逻辑代码
实现步骤:

1. 设计一个类,可以完成数据的封装

2. 设计一个抽象类,定义文件读取的相关功能,并使用了类实现具体功能

3. 读取文件,生产数据对象

4. 进行数据需求的逻辑计算(计算每一天的销售额)

5. 通过PyEcharts 进行图形绘制
"""
from OOP_Advanced_data_practice1 import Record
from OOP_Advanced_data_practice2 import FileReader,txtFileReader,jsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt = txtFileReader("2011年1月销售数据.txt")
res1 = txt.read_data()
# for record in res1:
#     print(record)
# print("-----------------")
js = jsonFileReader("2011年2月销售数据JSON.txt")
res2 = js.read_data()
# for record in res2:
#     print(record)

all_data = res1 + res2      # type : List[Record]
# 计算每一天的销售额
data_money={}
for i in all_data:
    if i.data in data_money.keys():
        data_money[i.data] += i.money
    else:
        data_money[i.data] = i.money
# print(data_money)

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_money.keys()))
bar.add_yaxis("销售额",list(data_money.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts = TitleOpts(title="每日销售数据")
)
bar.render("每日销售数据柱状图.html")


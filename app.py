# 1.导入Flask类。这个类的实例将会是我们的 WSGI 应用程序。
import json
from flask import Flask, render_template, Response, request
import pandas as pd


# 2.创建一个该类的实例，第一个参数是应用模块或者包的名称。
# 如果你使用单一的模块（如本例），你应该使用 __name__ ，因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 '__main__' 或实际的导入名）。
# 这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。详情见 Flask的文档。
app = Flask(__name__)

# 3.使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。这个函数的名字也在生成 URL 时被特定的函数采用，这个函数返回我们想要显示在用户浏览器中的信息。
# 输出helloworld页面
@app.route('/dynamic')
def hello_world():
    return render_template('dynamic-data2.html')

# 输出login success页面
@app.route('/login')
def login():
    return 'login success!'

@app.route('/index')
@app.route('/')
def index():
    data = pd.read_csv('static/pig1.csv')
    da = data.to_dict('list')  # 形成字典
    keys = ','.join(da.keys())
    # 变成列表
    # p = keys.split(',')
    p = ['time', ' ACC_X', ' ACC_Y', ' ACC_Z', ' B_X', ' B_Y', ' B_Z', ' GYRO_X', ' GYRO_Y', ' GYRO_Z','racc']
    p0 = da["time"]
    p1 = da[" ACC_X"]
    p2 = da[" ACC_Y"]
    p3 = da[" ACC_Z"]
    p4 = da[" B_X"]
    p5 = da[" B_Y"]
    p6 = da[" B_Z"]
    p7 = da[" GYRO_X"]
    p8 = da[" GYRO_Y"]
    p9 = da[" GYRO_Z"]

    return render_template('index.html', data1=p[1:-1], data2=p0, data3=p1, data4=p2, data5=p3,
                           data6=p4, data7=p5, data8=p6, data9=p7, data10=p8, data11=p9, name1=p[1],
                           name2=p[2], name3=p[3], name4=p[4], name5=p[5], name6=p[6], name7=p[7],
                           name8=p[8], name9=p[9])
#   name1 = p[1]= ACC_X
#   data2 = ["'2020-10-15 18:14:48 454'", "'2020-10-15 18:14:48 338'", "'2020-10-15 18:14:48 337'", "'2020-10-15 18:14:48 335'", "'2020-10-15 18:14:48 333'",....]
#   data1=p[1:-1] = [' ACC_X', ' ACC_Y', ' ACC_Z', ' B_X', ' B_Y', ' B_Z', ' GYRO_X', ' GYRO_Y', ' GYRO_Z']

@app.route('/index2')
def index2():
    data = pd.read_csv('static/pig2.csv')
    da = data.to_dict('list')  # 形成字典
    keys = ','.join(da.keys())
    # 变成列表
    # p = keys.split(',')
    p = ['time', ' ACC_X', ' ACC_Y', ' ACC_Z', ' B_X', ' B_Y', ' B_Z', ' GYRO_X', ' GYRO_Y', ' GYRO_Z','racc']
    p0 = da["time"]
    p1 = da[" ACC_X"]
    p2 = da[" ACC_Y"]
    p3 = da[" ACC_Z"]
    p4 = da[" B_X"]
    p5 = da[" B_Y"]
    p6 = da[" B_Z"]
    p7 = da[" GYRO_X"]
    p8 = da[" GYRO_Y"]
    p9 = da[" GYRO_Z"]

    return render_template('index2.html', data1=p[1:-1], data2=p0, data3=p1, data4=p2, data5=p3,
                           data6=p4, data7=p5, data8=p6, data9=p7, data10=p8, data11=p9, name1=p[1],
                           name2=p[2], name3=p[3], name4=p[4], name5=p[5], name6=p[6], name7=p[7],
                           name8=p[8], name9=p[9])
# 4.用run()函数运行在本地服务器上。 其中 if __name__ =='__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。
#web服务器
if __name__ == '__main__':
    app.run(debug=True)

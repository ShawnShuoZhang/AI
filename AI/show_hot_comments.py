# 绘制评论饼状图


import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

from baidu import path


def show_hot_comments():
    # 导入数据
    read_path = path + '/电视剧数据文件/hot_comments.json'
    read_path = read_path.replace('\\', '/')
    df = pd.read_json(read_path)
    # 提取需要数据
    feel = list(df['观看感受'])
    # print(feel)
    labels = ['力荐', '推荐', '还行', '很差', '较差', '无']
    values = [feel.count('力荐'), feel.count('推荐'), feel.count('还行'), feel.count('很差'), feel.count('较差'),
              feel.count('无')]
    # print(values)
    # 绘制
    pie = (
        Pie()
        .add(series_name='', data_pair=[(i, j) for i, j in zip(labels, values)])
        .set_global_opts(title_opts=opts.TitleOpts("热评前100观众评价分析"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    )
    pie.render(path + '/电视剧收视率分析图/hot_comments.html')

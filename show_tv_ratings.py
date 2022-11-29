# 绘制单个卫视收视率变化图


import pandas as pd
from pyecharts.charts import Line, Bar
from pyecharts import options as opts

from baidu import path


def show_tv_ratings(json_file):
    # 导入json数据
    read_path = path + '/电视剧数据文件/' + json_file
    read_path = read_path.replace('\\', '/')
    # print(read_path)
    df = pd.read_json(read_path, dtype={'播出日期': str})
    dates = list(df['播出日期'])
    ratings = list(df['收视率%'])
    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis("收视率%", ratings, is_connect_nones=True)
    )
    if str(json_file)[:-5] == 'dongfang':
        line.set_global_opts(title_opts=opts.TitleOpts(title="《平凡的荣耀》东方卫视收视率变化趋势图"))
    else:
        line.set_global_opts(title_opts=opts.TitleOpts(title="《平凡的荣耀》浙江卫视收视率变化趋势图"))
    line.render(path + '/电视剧收视率分析图/' + str(json_file)[:-5] + '_ratings.html')


# 绘制卫视收视份额对比图
def show_tvs_ratings():
    # 导入json数据
    dongfang = path + '/电视剧数据文件/dongfang.json'
    dongfang = dongfang.replace('\\', '/')
    zhejiang = path + '/电视剧数据文件/zhejiang.json'
    zhejiang = zhejiang.replace('\\', '/')
    df1 = pd.read_json(dongfang)
    df2 = pd.read_json(zhejiang)
    # 提取需要的数据
    dongfang_dates = list(df1['播出日期'])
    dongfang_ratings = list(df1['收视份额%'])
    # zhejiang_dates = list(df2['播出日期'])
    zhejiang_ratings = list(df2['收视份额%'])
    # 绘制
    bar = (
        Bar()
        .add_xaxis(dongfang_dates)
        .add_yaxis("东方卫视", dongfang_ratings)
        .add_yaxis("浙江卫视", zhejiang_ratings)
        .set_global_opts(title_opts=opts.TitleOpts("《平凡的荣耀》收视份额变化分析图"))
    )
    bar.render(path + '/电视剧收视率分析图/tvs_ratings.html')

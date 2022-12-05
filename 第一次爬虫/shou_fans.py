# 绘制粉丝数量图

import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

from baidu import path


def show_fans():
    # 读
    read_path = path + '/电视剧数据文件/actor_infos.json'
    read_path = read_path.replace('\\', '/')
    df = pd.read_json(read_path)
    actor_names = list(df['姓名'])
    actor_fans = list(df['粉丝量'])
    bar = (
        Bar()
        .add_xaxis(actor_names)
        .add_yaxis("粉丝数量", actor_fans)
        .set_global_opts(title_opts=opts.TitleOpts(title="《平凡的荣耀》主演粉丝数量分析图"))
    )
    bar.render(path + '/电视剧收视率分析图/fans.html')

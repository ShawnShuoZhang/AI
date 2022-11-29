# 爬取主函数
import time

from baidu import get_actors, get_one_actors
from douban import get_hot_comments
from shou_fans import show_fans
from show_hot_comments import show_hot_comments
from show_tv_ratings import show_tv_ratings, show_tvs_ratings
from weishi import get_ratings
from write_hot_comments import write_actor_infos, write_tvs_ratings, write_hot_comments


def get_all():
    get_actors()
    time.sleep(2)
    get_one_actors()
    time.sleep(2)
    get_ratings()
    time.sleep(2)
    get_hot_comments()
    time.sleep(2)


# 绘制分析图
def show_all():
    show_fans()
    show_tv_ratings('dongfang.json')
    show_tv_ratings('zhejiang.json')
    show_tvs_ratings()
    show_hot_comments()


# 数据存入Excel表
def write_all():
    write_actor_infos()
    time.sleep(2)
    write_tvs_ratings()
    time.sleep(2)
    write_hot_comments()
    time.sleep(2)

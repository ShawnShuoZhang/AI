# 将热评写入execl表
from os import path

from pandas.io import json


def write_hot_comments():
    file_path = path + '/电视剧数据文件/hot_comments.json'
    file_path = file_path.replace('\\', '/')
    with open(file_path, 'r', encoding='utf8') as f:
        comments = json.load(f)
    # print(comments)
    title = ['评论人', '观看感受', '评论时间', '评论内容', '评论点赞数']
    # 打开Excel
    wb = xw.Book()
    sht = wb.sheets('Sheet1')
    sht.range('A1').value = title
    line = 2
    for comment in comments:  # 循环字典
        # print(list(comment.values()))
        sht.range(f'A{line}').value = list(comment.values())
        line += 1


# 将演员数据存入Excel
def write_actor_infos():
    # 读数据
    file_path = path + '/电视剧数据文件/actor_infos.json'
    file_path = file_path.replace('\\', '/')
    with open(file_path, 'r', encoding='utf8') as f:
        actor_infos = json.load(f)
    # actor_infos = list(actor_infos)
    # 定义Excel表头
    title = ['姓名', '出生地', '出生日期', '星座', '血型', '身高', '体重', '粉丝量']
    # 打开Excel
    wb = xw.Book()
    sht = wb.sheets('Sheet1')
    sht.range('A1').value = title
    # 设置写入行索引，从第2行开始
    line = 2
    # 遍历每个演员数据
    for actor in actor_infos:
        # 获取单个演员字典的key值
        keys = list(actor.keys())
        values = list(actor.values())
        # 设置key值与value值一一对应的索引
        index = 0
        # 遍历key值进行属性匹配
        for key in keys:
            # 如果是姓名存入A列
            if key == '姓名':
                # print(values[index])
                sht.range(f'A{line}').value = values[index]
                index += 1
            if key == '出生地':
                sht.range(f'B{line}').value = values[index]
                index += 1
            if key == '出生日期':
                sht.range(f'C{line}').value = values[index]
                index += 1
            if key == '星座':
                sht.range(f'D{line}').value = values[index]
                index += 1
            if key == '血型':
                sht.range(f'E{line}').value = values[index]
                index += 1
            if key == '身高':
                sht.range(f'F{line}').value = values[index]
                index += 1
            if key == '体重':
                sht.range(f'G{line}').value = values[index]
                index += 1
            if key == '粉丝量':
                sht.range(f'H{line}').value = values[index]
                index += 1
        line += 1


# 将收视率存入Excel
def write_tvs_ratings():
    dongfang = path + '/电视剧数据文件/dongfang.json'
    dongfang = dongfang.replace('\\', '/')
    zhejiang = path + '/电视剧数据文件/zhejiang.json'
    zhejiang = zhejiang.replace('\\', '/')
    with open(dongfang, 'r', encoding='utf8') as f:
        dongfang = json.load(f)
    with open(zhejiang, 'r', encoding='utf8') as f:
        zhejiang = json.load(f)
    title = ['播出日期', '收视率%', '收视份额%', '收拾排名']
    wb = xw.Book()
    sht = wb.sheets('Sheet1')
    sht.range('A1').value = '东方卫视'
    sht.range('E1').value = '浙江卫视'
    sht.range('A2:D2').value = title
    sht.range('E2:H2').value = title
    line = 3
    for d in dongfang:
        sht.range(f'A{line}:D{line}').value = list(d.values())
        line += 1
    line = 3
    for z in zhejiang:
        sht.range(f'E{line}:H{line}').value = list(z.values())
        line += 1

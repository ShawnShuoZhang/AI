# 爬取收视情况
from json import dump

import requests
from bs4 import BeautifulSoup
from pandas.io import json

from baidu import path


def get_ratings():
    # 定义headers和网页
    headers = {
        # 'Host': 'baike.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
        'Cookie': '__yjsv5_shitong=1.0_7_1b511363715b8341a6b858c9784cf79473ec_300_1607592679535_218.56.38.242_f194afe3; yjs_js_security_passport=e2ee49471e3e645bb94ed5b037ce6cfba6955b66_1607592680_js'
    }
    url = 'https://baike.baidu.com/item/%E5%B9%B3%E5%87%A1%E7%9A%84%E8%8D%A3%E8%80%80/22358681?fromModule=lemma-qiyi_sense-lemma'
    # 获取response
    response = requests.get(url, headers=headers)
    # 转
    first_soup = BeautifulSoup(response.text, 'lxml')
    # 审查播出信息模块下收视情况子模块div，发现class=para
    # 提取class=para的div，因为不止收视情况div的class为该值，所以find_all
    second_soup = first_soup.find_all(name='div', attrs={'class': 'para'})
    # print(second_soup)
    # 遍历符合条件的div
    final_soup = ''
    for d in second_soup:
        # 如果div中文本为收视情况，则匹配成功并获取它下面的一个table
        if ''.join(str(d.text).split()) == '收视情况':
            final_soup = d.find_next(name='table')
    # 得到table中的所有tr
    trs = final_soup.find_all(name='tr')
    # print(trs)
    # 定义存放两个卫视收视情况的字典
    dongfang_datas = []
    zhejiang_datas = []
    # 遍历tr,获取播出期间各个卫视的收视情况
    for tr in trs[2:]:
        dongfang = {}
        zhejiang = {}
        tds = tr.find_all(name='td')
        dongfang['播出日期'] = tds[0].text
        dongfang['收视率%'] = tds[1].text
        dongfang['收视份额%'] = tds[2].text
        dongfang['排名'] = tds[3].text
        zhejiang['播出日期'] = tds[0].text
        zhejiang['收视率%'] = tds[4].text
        zhejiang['收视份额%'] = tds[5].text
        zhejiang['排名'] = tds[6].text
        dongfang_datas.append(dongfang)
        zhejiang_datas.append(zhejiang)
        # print(tds[2].text)
    # print(dongfang_datas)
    # print(zhejiang_datas)
    # 转格式
    json_dongdang_datas = json.loads(str(dongfang_datas).replace("\'", "\""))
    json_zhejiang_datas = json.loads(str(zhejiang_datas).replace("\'", "\""))
    print(path)
    dongfang_path = path + '/电视剧数据文件/dongfang.json'
    dongfang_path = dongfang_path.replace('\\', '/')
    zhejiang_path = path + '/电视剧数据文件/zhejiang.json'
    zhejiang_path = zhejiang_path.replace('\\', '/')
    # 将两个卫视的收视情况存入到两个json文件中
    with open(dongfang_path, 'w', encoding='UTF-8') as f:
        dump(json_dongdang_datas, f, ensure_ascii=False)
    with open(zhejiang_path, 'w', encoding='UTF-8') as f:
        dump(json_zhejiang_datas, f, ensure_ascii=False)

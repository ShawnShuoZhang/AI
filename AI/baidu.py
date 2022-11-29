# 获取当前路径
from json import dump

import requests as requests
from bs4 import BeautifulSoup
import os

path = os.getcwd()


# 爬取演员信息并返回html
def get_actors():
    # 定义headers和网页
    headers = {
        # 'Host': 'baike.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
        'Cookie': '__yjsv5_shitong = 1.0_7_1b511363715b8341a6b858c9784cf79473ec_300_1607592679535_218.56.38.242_f194afe3;yjs_js_security_passport = e2ee49471e3e645bb94ed5b037ce6cfba6955b66_1607592680_js'
    }
    url = 'https://baike.baidu.com/item/%E5%B9%B3%E5%87%A1%E7%9A%84%E8%8D%A3%E8%80%80/22358681?fromModule=lemma-qiyi_sense-lemma'
    # get
    response = requests.get(url, headers=headers)
    # 将一段文档传入BeautifulSoup的构造方法,就能得到一个文档的对象, 可以传入一段字符串
    # print(response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.find_all('li'))
    # 获取角色介绍模块div数据
    first_actors = soup.find(name='div', attrs={'class': 'lemmaWgt-roleIntroduction'})
    # print(first_actors)
    # 进一步得到模块中li标签中的演员数据
    second_actors = first_actors.find_all(name='li')
    # print(second_actors)
    # 演员数据提取
    actors = []
    for second_actor in second_actors:
        actor = {}
        if second_actor.find(name='div', attrs={'class': 'role-actor'}):
            # 提取演员名称及百科链接
            actor["name"] = second_actor.find('div', {'class': 'role-actor'}).find('a').text
            actor['link'] = 'https://baike.baidu.com' + second_actor.find('div', {'class': 'role-actor'}).find('a').get(
                'href')
        actors.append(actor)
    # print(actors)
    from pandas.io import json
    json_actors = json.loads(str(actors).replace("\'", "\""))
    # print(json_actors)
    file_path = path + '/电视剧数据文件/actors.json'
    file_path = file_path.replace('\\', '/')
    # print(file_path)
    # print(json_actors)
    # print(json.__file__)
    # print(json.__path__)
    with open(file_path, 'w', encoding='UTF-8') as f:
        dump(json_actors, f)


# 获取每个演员的百科信息
def get_one_actors():
    read_path = path + '/电视剧数据文件/actors.json'
    print(path)
    read_path = read_path.replace('\\', '/')
    print(read_path)
    # 读取json数据
    with open(read_path, 'r', encoding='UTF-8') as f:
        from pandas.io import json
        actors = json.loads(f.read())
    headers = {
        # 'Host': 'baike.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
    }
    # 存提取的百科数据
    actor_infos = []
    for actor in actors:
        actor_info = {}
        actor_info['姓名'] = actor['name']
        # 获取请求
        # print(actor['link'])
        response = requests.get(actor['link'], headers=headers)
        # 得到百科全部数据
        first_soup = BeautifulSoup(response.text, 'lxml')
        # 提取演员基本信息模块列表部分数据
        second_soup = first_soup.find(name='div', attrs={'class': 'basic-info J-basic-info cmn-clearfix'})
        # print(second_soup)
        # 得到div中的dl
        dls = second_soup.find_all(name='dl')
        # 遍历所有的dl
        for dl in dls:
            dts = dl.find_all(name='dt')
            # print(dts)
            # dds = dl.find_all(name='dd')
            # print(dds[index].text.strip())
            # 遍历单个dl的所有dt
            for dt in dts:
                # 匹配字符，通过join和split方法，提取dt中的纯文字
                if ''.join(str(dt.text).split()) == '出生地':
                    actor_info['出生地'] = dt.find_next(name='dd').text.strip().replace("\n", "")
                if ''.join(str(dt.text).split()) == '出生日期':
                    actor_info['出生日期'] = dt.find_next(name='dd').text.strip()
                if ''.join(str(dt.text).split()) == '血型':
                    actor_info['血型'] = dt.find_next(name='dd').text.strip()
                if ''.join(str(dt.text).split()) == '身高':
                    actor_info['身高'] = dt.find_next(name='dd').text.strip()
                if ''.join(str(dt.text).split()) == '体重':
                    actor_info['体重'] = dt.find_next(name='dd').text.strip()
                if ''.join(str(dt.text).split()) == '星座':
                    # print(''.join(str(dt.text)))
                    actor_info['星座'] = dt.find_next(name='dd').text.strip()
        # 获取百度数说模块
        first_fans = first_soup.find(name='div', attrs={'class': 'fans-portrait'})
        # 进一步得到粉丝总数部分数据
        try:
            fans = first_fans.find(name='span', attrs={'class': 'fans-total'}).text
            actor_info['粉丝量'] = fans
        except:
            actor_info['粉丝量'] = '未知'
        actor_infos.append(actor_info)
        json_actor_infos = json.loads(str(actor_infos).replace("\'", "\""))
        # 存
        file_path = path + '/电视剧数据文件/actor_infos.json'
        file_path = file_path.replace('\\', '/')
        with open(file_path, 'w', encoding='UTF-8') as f:
            dump(json_actor_infos, f, ensure_ascii=False)

# 爬取线上优酷热评
from json import dump

import requests
from bs4 import BeautifulSoup
from pandas.io import json

from baidu import path


def get_hot_comments():
    headers = {
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Cookie': '_vwo_uuid_v2=DE8F855EC24AE2DDC7761E12EAB48EAEF|c5c585e9feb33aa574682b87f0284a1c;_pk_id.100001.4cf6=45cef77f2b5a9960.1607930880.1.1607931254.1607930880.'
    }
    # 热评
    comments = []
    for i in range(5):
        url = f'https://movie.douban.com/subject/30186581/comments?start={i * 20}&status=P&sort=new_score'
        # 获取全部
        responce = requests.get(url, headers=headers)
        # 转bs4
        first_soup = BeautifulSoup(responce.text, 'lxml')
        # 提取"平凡的荣耀 短评"下的评论模块
        second_soup = first_soup.find(name='div', attrs={'class': 'article'})
        # 提取100条热评
        first_hot_comments = second_soup.find(name='div', attrs={'class': 'mod-bd'})
        second_hot_comments = first_hot_comments.find_all(name='div', attrs={'class': 'comment'})
        # print(second_hot_comments)
        for comment in second_hot_comments:
            c = {}
            # 获取存用户名、观影感受和评论时间的span
            first_user = comment.find(name='span', attrs={'class': 'comment-info'})
            user = first_user.find(name='a').text
            date = first_user.find(name='span', attrs={'class': 'comment-time'})
            feel = date.find_previous(name='span')
            # print(user,date)
            c['评论人'] = user
            try:
                c['观看感受'] = feel['title']
            except:
                c['观看感受'] = '无'
            c['评论日期'] = date.text.strip()
            # 获取评论内容
            content = comment.find(name='p').text.strip().replace("\n", "")
            # print(content)
            c['内容'] = content
            # 获取存点赞数的span
            first_vote = comment.find(name='span', attrs={'class': 'comment-vote'})
            vote = first_vote.find(name='span', attrs={'class': 'votes vote-count'}).text
            c['点赞数'] = vote
            comments.append(c)
    # print(comments)
    # print(len(comments))
    # 存
    json_hot_comments = json.loads(str(comments).replace("\'", "\""))
    file_path = path + '/电视剧数据文件/hot_comments.json'
    file_path = file_path.replace('\\', '/')
    with open(file_path, 'w', encoding='UTF-8') as f:
        dump(json_hot_comments, f, ensure_ascii=False)

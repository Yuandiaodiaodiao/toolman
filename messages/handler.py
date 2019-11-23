import requests
import json
import os
import base64
import random
from urllib import request
from myConfig.configJson import configJs

RSSHUB_URL = "https://rsshub.app"
OUR_RSSHUB_URL = configJs["RSSHUB_URL"]
POST_URL = f"http://{configJs['serverip']}:{configJs['messageServerListen']}"
PATH_THIS_FLODER = os.path.dirname(os.path.abspath(__file__))
PATH_FATHER_FLODER = os.path.dirname(PATH_THIS_FLODER)
PATH_IMAGE_LIST = os.path.join(PATH_THIS_FLODER, 'image_list.json')
PATH_RSS_LIST = os.path.join(PATH_FATHER_FLODER, 'rss_fetch/rss_list.json')
# 表情包初始化
bqb = json.load(open(PATH_IMAGE_LIST, encoding='utf-8'))


def check_url(url):
    try:
        res = requests.get(url.replace(RSSHUB_URL, OUR_RSSHUB_URL))
    except Exception as e:
        print('url 不能访问' + str(e))
        return False
    return res.status_code == 200


def send_message(qq_group_id, qq_id_list, text, img, ensure_private=False):
    data = json.dumps({
        "qq_group_id": qq_group_id,
        "qq_id_list": qq_id_list,
        "text": text,
        "img": img,
        "ensure_private": ensure_private
    }, ensure_ascii=False)
    print(data)
    try:
        requests.post(POST_URL, data=data.encode('utf-8'))
    except requests.exceptions.InvalidSchema:
        print("网络错误")


def simple_send_message(data, text):
    send_message(data['qq_group_id'], [], text, "")


def add_rss_url(data, rss_url, at):
    if not check_url(rss_url):
        send_message(data['qq_group_id'], [data['qq_id']], f"你给的 url 不能访问！", "")
        return
    json_list = json.load(open(PATH_RSS_LIST))
    json_item = json_list[data['qq_group_id']]
    if rss_url in json_item.keys() and not at:  # 他想添加这个 url，但是已存在
        send_message("", [data['qq_id']], f"👴已经订阅这个 url 了，不要重复订阅！", "", ensure_private=True)
    if rss_url not in json_item.keys():  # 不存在 添加！
        json_item[rss_url] = []
        send_message("", [data['qq_id']], f"为群({data['qq_group_id']})添加了 {rss_url} 订阅源。", "", ensure_private=True)
    if at:
        json_item[rss_url].append(data['qq_id'])
        json_item[rss_url] = list(set(json_item[rss_url]))
        send_message("", [data['qq_id']], f"当 {rss_url} 更新时会提醒你。", "", ensure_private=True)
    json.dump(json_list, open(PATH_RSS_LIST, "w"), ensure_ascii=False)


def del_rss_url(data, rss_url, at):
    json_list = json.load(open(PATH_RSS_LIST))
    json_item = json_list[data['qq_group_id']]
    if rss_url not in json_item.keys():  # 删除这个 url，但是不存在
        send_message("", [data['qq_id']], f"此 url 未被订阅", "", ensure_private=True)
    if rss_url in json_item.keys() and not at:  # 删除此订阅源
        if len(json_item[rss_url])>1:
            send_message(data['qq_group_id'], json_item[rss_url], f"你订阅的 {rss_url} 订阅源已被删除", "")
        send_message("", [data['qq_id']], f"{rss_url} 订阅源已被删除", "", ensure_private=True)
        json_item.pop(rss_url)
    if at:
        json_item[rss_url].remove(data['qq_id'])
        send_message("", [data['qq_id']], f"已将你从 {rss_url} 的提醒列表中删除。", "", ensure_private=True)
    json.dump(json_list, open(PATH_RSS_LIST, "w"), ensure_ascii=False)


# def add_bqb(data, key_word, img_url_list):
#     global bqb
#     print(key_word)
#     bqb = json.load(open(PATH_IMAGE_LIST, encoding='utf-8'))
#     if key_word not in bqb:
#         bqb[key_word] = []
#     bqb[key_word] += img_url_list
#     json.dump(bqb, open(PATH_IMAGE_LIST, 'w', encoding='utf-8'), ensure_ascii=False)
#     simple_send_message(data, f'已添加 {key_word}')


# def del_bqb(data, key_word):
#     global bqb
#     bqb = json.load(open(PATH_IMAGE_LIST, encoding='utf-8'))
#     if key_word not in bqb:
#         bqb[key_word] = []
#     bqb.pop(key_word)
#     json.dump(bqb, open(PATH_IMAGE_LIST, 'w', encoding='utf-8'), ensure_ascii=False)
#     simple_send_message(data, f'已删除 {key_word}')


def handler_command(data):
    message_help = """
“🍰 万物皆可 RSS” 
结合 https://docs.rsshub.app 使用效果更佳⭐
出于稳定考虑，本 bot 在抓取 RSS 时会使用 http://server.oops-sdu.cn:1200 替换 RSS url 中的 https://rsshub.app。

---
在 QQ 群中：
# add_rss url：添加 RSS 订阅
# add_rss url -at：此源更新时 at 你
# del_rss url：删除 RSS 订阅
# del_rss url -at：此源更新时不再 at 你

在私聊窗口：
#：会私聊你帮助信息
# status：会私聊你现在 qq_bot rss 的配置文件

举例：
# add_rss https://rsshub.app/sdu/cs/0 -at
# del_rss https://rsshub.app/sdu/cs/0
"""
    json_list = json.load(open(PATH_RSS_LIST))
    text = data['text'].split()
    if data['qq_group_id'] in json_list.keys():
        if len(text) > 2 and text[1] == 'add_rss':
            add_rss_url(data, text[2], '-at' in text)
        elif len(text) > 2 and text[1] == 'del_rss':
            del_rss_url(data, text[2], '-at' in text)
        else:
            send_message("", [data['qq_id']], "命令错误", "", ensure_private=True)
            send_message("", [data['qq_id']], message_help, "", ensure_private=True)
    if data['qq_group_id'] == "":
        if len(text) == 1:
            send_message("", [data['qq_id']], message_help, "", ensure_private=True)
        elif len(text) > 1 and text[1] == 'status':
            send_message("", [data['qq_id']], '🐎订阅列表：\n'
                         + json.dumps(json.load(open(PATH_RSS_LIST)), indent=2, ensure_ascii=False), "", ensure_private=True)

    # elif len(text) > 2 and text[1] == 'add_bqb':
    #     add_bqb(data, text[2], data['img'])
    # elif len(text) > 2 and text[1] == 'del_bqb':
    #     del_bqb(data, text[2])


# 你应该修改这个
def handler_plain(data):
    pass
    # text = data['text'].strip()
    # if text == 'yzh':
    #     simple_send_message(data, 'cy!!!')
    #     return
    # if text in bqb:
    #     send_message(data['qq_group_id'], [], '', random.choice(bqb[text]))


def handler(data):
    """
    :param data:
        "qq_group_id": "967636480",
        "qq_id": "2523897396",
        "text": "在炮弹里洗个澡吧",
        "img": None
    :return:
    """
    json_list = json.load(open(PATH_RSS_LIST))
    data['text'] = data['text'].strip()
    print('--------')
    print(data)

    if len(data["text"]) > 0 and data["text"][0] == '#':
        handler_command(data)
    else:
        handler_plain(data)


if __name__ == '__main__':
    pass
    # data_test = {
    #     "qq_group_id": "967636480",
    #     "qq_id": "2523897396",
    #     "text": "在炮弹里洗个澡吧",
    #     "img": ""
    # }
    # while True:
    #     text_ = input()
    #     data_test['text'] = text_
    #     handler(data_test)
    # res = check_url('https://rsshub.app/bilibili/user/video/5055')
    # print(res)

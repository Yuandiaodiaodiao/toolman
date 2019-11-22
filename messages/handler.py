import requests
import json
import os
import base64
import random
from urllib import request

RSSHUB_URL = "https://rsshub.app"
OUR_RSSHUB_URL = "http://server.oops-sdu.cn:1200"
POST_URL = "http://127.0.0.1:9003"
PATH_THIS_FLODER=os.path.dirname(os.path.abspath(__file__))
PATH_FATHER_FLODER=os.path.dirname(PATH_THIS_FLODER)
PATH_IMAGE_LIST=os.path.join(PATH_THIS_FLODER,'image_list.json')
PATH_RSS_LIST=os.path.join(PATH_FATHER_FLODER,'rss_fetch/rss_list.json')
# 表情包初始化
bqb = json.load(open(PATH_IMAGE_LIST, encoding='utf-8'))


def check_url(url):
    try:
        res = requests.get(url.replace(RSSHUB_URL, OUR_RSSHUB_URL))
    except Exception as e:
        print('url 不能访问' + str(e))
        return False
    return res.status_code == 200


def send_message(qq_group_id, qq_id_list, text, img):
    data = json.dumps({
        "qq_group_id": qq_group_id,
        "qq_id_list": qq_id_list,
        "text": text,
        "img": img
    },ensure_ascii=False)
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
        send_message(data['qq_group_id'], [data['qq_id']], f"👴已经订阅这个 url 了，不要重复订阅！", "")
    if rss_url not in json_item.keys():  # 不存在 添加！
        json_item[rss_url] = []
        send_message(data['qq_group_id'], [], f"此群添加了 {rss_url} 订阅源。", "")
    if at:
        json_item[rss_url].append(data['qq_id'])
        json_item[rss_url] = list(set(json_item[rss_url]))
        send_message(data['qq_group_id'], [data['qq_id']], f"当 {rss_url} 更新时会提醒你。", "")
    json.dump(json_list, open(PATH_RSS_LIST, "w"), ensure_ascii=False)


def del_rss_url(data, rss_url, at):
    json_list = json.load(open(PATH_RSS_LIST))
    json_item = json_list[data['qq_group_id']]
    if rss_url not in json_item.keys():  # 删除这个 url，但是不存在
        send_message(data['qq_group_id'], [data['qq_id']], f"此 url 未被订阅", "")
    if rss_url in json_item.keys() and not at:  # 删除此订阅源
        send_message(data['qq_group_id'], json_item[rss_url], f"{rss_url} 订阅源已被删除", "")
        json_item.pop(rss_url)
    if at:
        json_item[rss_url].remove(data['qq_id'])
        send_message(data['qq_group_id'], [data['qq_id']], f"已将你从 {rss_url} 的提醒列表中删除。", "")
    json.dump(json_list, open(PATH_RSS_LIST, "w"), ensure_ascii=False)


def add_bqb(data, key_word, img_url_list):
    global bqb
    print(key_word)
    bqb = json.load(open(PATH_IMAGE_LIST, encoding='utf-8'))
    if key_word not in bqb:
        bqb[key_word] = []
    bqb[key_word] += img_url_list
    json.dump(bqb, open(PATH_IMAGE_LIST, 'w', encoding='utf-8'), ensure_ascii=False)
    simple_send_message(data, f'已添加 {key_word}')


def del_bqb(data, key_word):
    global bqb
    bqb = json.load(open(PATH_IMAGE_LIST, encoding='utf-8'))
    if key_word not in bqb:
        bqb[key_word] = []
    bqb.pop(key_word)
    json.dump(bqb, open(PATH_IMAGE_LIST, 'w', encoding='utf-8'), ensure_ascii=False)
    simple_send_message(data, f'已删除 {key_word}')


def handler_command(data):
    message_help = """
结合 https://docs.rsshub.app 使用效果更佳
出于稳定考虑，本 bot 在抓取 RSS 时会使用 http://server.oops-sdu.cn:1200 进行替换
---
# : 帮助
# add_rss url : 添加 RSS 订阅
# add_rss url -at : 此源更新时 at 你
# del_rss url : 删除 RSS 订阅
# del_rss url -at : 此源更新时不再 at 你
# add_bqb 关键词 图片 : 添加表情包
# del_bqb 关键词: 删除表情包
# status
"""
    text = data['text'].split()
    if len(text) == 1:
        send_message(data['qq_group_id'], [data['qq_id']], message_help, "")
    elif len(text) > 2 and text[1] == 'add_rss':
        add_rss_url(data, text[2], '-at' in text)
    elif len(text) > 2 and text[1] == 'del_rss':
        del_rss_url(data, text[2], '-at' in text)
    elif len(text) > 2 and text[1] == 'add_bqb':
        add_bqb(data, text[2], data['img'])
    elif len(text) > 2 and text[1] == 'del_bqb':
        del_bqb(data, text[2])
    elif len(text) > 1 and text[1] == 'status':
        send_message(data['qq_group_id'], [data['qq_id']], '🐎订阅列表：\n'
                     + json.dumps(json.load(open(PATH_RSS_LIST)), indent=2, ensure_ascii=False)
                     + '\n🐎表情包列表：\n' + json.dumps(bqb, indent=2, ensure_ascii=False), "")
    else:
        send_message(data['qq_group_id'], [data['qq_id']], "星际玩家，给👴把文档看清楚再发命令！", "")
        send_message(data['qq_group_id'], [data['qq_id']], message_help, "")


# 你应该修改这个
def handler_plain(data):
    text = data['text'].strip()
    if text == 'yzh':
        simple_send_message(data, 'cy!!!')
        return
    if text in bqb:
        send_message(data['qq_group_id'], [], '', random.choice(bqb[text]))


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
    if data['qq_group_id'] not in json_list.keys():
        return

    if len(data["text"]) > 0 and data["text"][0] == '#':
        handler_command(data)
    else:
        handler_plain(data)


if __name__ == '__main__':
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
    pass

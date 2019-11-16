import requests
import json

RSSHUB_URL = "https://rsshub.app"
OUR_RSSHUB_URL = "http://server.oops-sdu.cn:1200"
POST_URL = "http://192.168.137.1:50382"


def send_message(qq_group_id, qq_id_list, text, img):
    data = json.dumps({
        "qq_group_id": qq_group_id,
        "qq_id_list": qq_id_list,
        "text": text,
        "img": img
    })
    print(data)
    try:
        requests.post(POST_URL, data=data)
    except requests.exceptions.InvalidSchema:
        print("网络错误")


def simple_send_message(data, text):
    send_message(data['qq_group_id'], [], text, "")


def add_rss_url(data, rss_url, at):
    json_list = json.load(open("../rss_fetch/rss_list.json"))
    json_item = json_list[data['qq_group_id']]
    if rss_url in json_item.keys() and not at:  # 他想添加这个 url，但是已存在
        send_message(data['qq_group_id'], [data['qq_id']], f"此 url 已被订阅。", "")
    if rss_url not in json_item.keys():  # 不存在 添加！
        json_item[rss_url] = []
        send_message(data['qq_group_id'], [], f"此群添加了 {rss_url} 订阅源。", "")
    if at:
        json_item[rss_url].append(data['qq_id'])
        json_item[rss_url] = list(set(json_item[rss_url]))
        send_message(data['qq_group_id'], [data['qq_id']], f"当 {rss_url} 更新时会提醒你。", "")
    json.dump(json_list, open("../rss_fetch/rss_list.json", "w"))


def del_rss_url(data, rss_url, at):
    json_list = json.load(open("../rss_fetch/rss_list.json"))
    json_item = json_list[data['qq_group_id']]
    if rss_url not in json_item.keys():  # 删除这个 url，但是不存在
        send_message(data['qq_group_id'], [data['qq_id']], f"此 url 未被订阅", "")
    if rss_url in json_item.keys() and not at:  # 删除此订阅源
        send_message(data['qq_group_id'], json_item[rss_url], f"{rss_url} 订阅源已被删除", "")
        json_item.pop(rss_url)
    if at:
        json_item[rss_url].remove(data['qq_id'])
        send_message(data['qq_group_id'], [data['qq_id']], f"已将你从 {rss_url} 的提醒列表中删除。", "")
    json.dump(json_list, open("../rss_fetch/rss_list.json", "w"))


def handler_command(data):
    message_help = """
结合 https://docs.rsshub.app 使用效果更佳
出于稳定考虑，本 bot 在抓取 RSS 时会使用 http://server.oops-sdu.cn:1200 进行替换
---
# : 帮助
# add rss_url : 添加 RSS 订阅
# add rss_url -at : 此源更新时 at 你
# del rss_url : 删除 RSS 订阅
# del rss_url -at : 此源更新时不再 at 你
# status
"""
    text = data['text'].split()
    if len(text) == 1:
        send_message(data['qq_group_id'], [data['qq_id']], message_help, "")
    elif len(text) > 1 and text[1] == 'add':
        add_rss_url(data, text[2], '-at' in text)
    elif len(text) > 1 and text[1] == 'del':
        del_rss_url(data, text[2], '-at' in text)
    elif len(text) > 1 and text[1] == 'status':
        send_message(data['qq_group_id'], [data['qq_id']], json.dumps(json.load(open("../rss_fetch/rss_list.json")), indent=2), "")
    else:
        send_message(data['qq_group_id'], [data['qq_id']], message_help, "")


# 你应该修改这个
def handler_plain(data):
    text = data['text'].strip()
    


def handler(data):
    """
    :param data:
      "qq_group_id": "967636480",
        "qq_id": "2523897396",
        "text": "在炮弹里洗个澡吧",
        "img": None
    :return:
    """

    json_list = json.load(open("../rss_fetch/rss_list.json"))
    data['text'] = data['text'].strip()
    print('--------')
    print(data)
    if data['qq_group_id'] not in json_list.keys():
        return

    if data["text"][0] == '#':
        handler_command(data)
    else:
        handler_plain(data)


if __name__ == '__main__':
    data_test = {
        "qq_group_id": "967636480",
        "qq_id": "2523897396",
        "text": "在炮弹里洗个澡吧",
        "img": ""
    }
    while True:
        text_ = input()
        data_test['text'] = text_
        handler(data_test)

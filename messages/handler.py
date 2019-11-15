# qq_group_id: "123456789"
# qq_id: "1243265436"
# text: "哈哈哈哈哈哈"
# img: "base64154332432643614234"
# 如果私聊 qq_group_id = None
# 如果群聊中普通消息 qq_id = None
# --------------- 可用命令 ------------------
# help
import json

RSSHUB_URL = "http://server.oops-sdu.cn:1200"


def send_message(qq_group_id, qq_id_list, text, img):
    print(qq_group_id, qq_id_list, text, img)

    pass


def add_rss_url(data, rss_url, at):
    # add
    json_list = json.load(open("../rss_fetch/rss_list.json"))
    json_item = json_list[data['qq_group_id']]
    if rss_url in json_item.keys() and not at:  # 他想添加这个 url，但是已存在
        send_message(data['qq_group_id'], [data['qq_id']], f"此 url 已被订阅。", None)
    if rss_url not in json_item.keys():  # 不存在 添加！
        json_item[rss_url] = []
        send_message(data['qq_group_id'], [], f"此群添加了 {rss_url} 订阅源。", None)
    if at:
        json_item[rss_url].append(data['qq_id'])
        send_message(data['qq_group_id'], [data['qq_id']], f"当 {rss_url} 更新时会提醒你。", None)
    json.dump(json_list, open("../rss_fetch/rss_list.json", "w"))


def del_rss_url(data, rss_url, at):
    json_list = json.load(open("../rss_fetch/rss_list.json"))
    json_item = json_list[data['qq_group_id']]
    if rss_url not in json_item.keys():  # 删除这个 url，但是不存在
        send_message(data['qq_group_id'], [data['qq_id']], f"此 url 未被订阅", None)
    if rss_url in json_item.keys() and not at:  # 删除此订阅源
        send_message(data['qq_group_id'], json_item[rss_url], f"{rss_url} 订阅源已被删除", None)
        json_item.pop(rss_url)
    if at:
        json_item[rss_url].remove(data['qq_id'])
        send_message(data['qq_group_id'], [data['qq_id']], f"已将你从 {rss_url} 的提醒列表中删除。", None)
    json.dump(json_list, open("../rss_fetch/rss_list.json", "w"))


def handler_command(data):
    message_help = """
结合 https://docs.rsshub.app 使用效果更佳
出于稳定考虑，本 bot 会使用 http://server.oops-sdu.cn:1200 进行替换
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
        send_message(data['qq_group_id'], [data['qq_id']], message_help, None)
        return
    if text[1] == 'add':
        add_rss_url(data, text[2], '-at' in text)
    if text[1] == 'del':
        del_rss_url(data, text[2], '-at' in text)
    if text[1] == 'status':
        send_message(data['qq_group_id'], [data['qq_id']], json.load(open("../rss_fetch/rss_list.json")), None)


def handler_plain(data):
    pass


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
        "img": None
    }
    while True:
        text = input()
        data_test['text'] = text
        handler(data_test)

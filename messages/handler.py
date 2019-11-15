# qq_group_id: "123456789"
# qq_id: "1243265436"
# text: "哈哈哈哈哈哈"
# img: "base64154332432643614234"
# 如果私聊 qq_group_id = None
# 如果群聊中普通消息 qq_id = None
# --------------- 可用命令 ------------------
# help
import argparse

RSSHUB_URL = "http://server.oops-sdu.cn:1200"

parser = argparse.ArgumentParser(
    description='This is a PyMOTW sample program',
)


def handler_command(text):
    message_help = """
结合 https://docs.rsshub.app 使用效果更佳
出于稳定考虑，本 bot 会使用 http://server.oops-sdu.cn:1200 进行替换
---
# : 帮助
# add rss_url : 添加 RSS 订阅
# add rss_url -at : 此源更新时 at 你
# del rss_url : 删除 RSS 订阅
# del rss_url -at : 此源更新时不再 at 你
"""
    try:
        text = text.split()
    except BaseException:
        res = message_help
    return res


def handler(qq_group_id: str, qq_id: str, text: str, img: str):
    if text[0] == '#':

    qq_id_list = [qq_id]
    return qq_group_id, qq_id_list, text, img


if __name__ == '__main__':
    res = handler("967636480", None, "在炮弹里洗个澡吧", None)

# qq_group_id: "123456789"
# qq_id: "1243265436"
# text: "哈哈哈哈哈哈"
# img: "base641543lkrdslknoids"
# 如果私聊 qq_group_id = None
# 如果群聊中普通消息 qq_id = None
def handler(qq_group_id, qq_id, text, img):
    qq_id_list = [qq_id]
    return qq_group_id, qq_id_list, text, img

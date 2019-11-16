class Node(object):
    def __init__(self):
        self.next = None


def add_word(root: Node, word: str) -> None:
    """
    添加单个敏感词，核心算法
    :param root: 根节点
    :param word: 单个敏感词
    """
    parent = root
    for w in word:
        if parent.next == None:
            parent.next = {}
            parent.next[w] = Node()

        if w not in parent.next:
            parent.next[w] = Node()

        parent = parent.next[w]


def read_file(sensitive_file: str) -> set:
    """
    读取敏感词字典
    :param sensitive_file: 敏感词文件
    :return: 敏感词集合
    """
    print(sensitive_file)
    ret = set()
    with open(sensitive_file, 'r', encoding='utf8') as fd:
        for line in fd.readlines():
            ret.add(line.strip())
    return ret


def add_sensitives(root: Node, words: set) -> None:
    """
    构建敏感词字典库
    """
    for key in words:
        add_word(root, key)


def api_contain(msg: str, root: Node, stop: bool = True) -> (bool, set):
    """
    查找敏感词，是否需要找到所有敏感词
    :param msg: 文本
    :param root: 敏感词字典树
    :param stop: 是否继续寻找
    :return: (状态,敏感词)
    """
    if root.next == None:
        raise ValueError("sensitive word is empty")

    ret = set()  # 保存敏感词
    stat = False  # 是否包含敏感词
    for idx, m in enumerate(msg):  # 遍历文本
        j = idx
        _root = root
        while _root.next != None and msg[j] in _root.next:  # 从根开始寻找
            _root = _root.next.get(msg[j])  # 依次向下寻找
            j += 1

        if _root.next == None:  # 最后一个次是否结束
            stat = True
            ret.add(msg[idx:j])  # 添加到敏感词集合
            if stop:
                break

    return stat, ret

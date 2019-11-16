from api import api_contain, Node
from api import read_file, add_word, add_sensitives


class DFA(object):
    def __init__(self, filename):
        self._words = set()
        self._filename = filename
        self._root = Node()
        self.read_file()
        self.add_words(self._words)

    def read_file(self):
        """读取敏感词文件 """
        self._words = read_file(self._filename)

    def create_node(self):
        """新建Node对象"""
        return Node()

    def dfa(self, content: str):
        """扫描文本"""
        return contain(msg=content, root=self._root)

    def add_word(self, word: str):
        """动态添加敏感词"""
        add_word(self._root, word=word)

    def add_words(self, words: set):
        """ 动态添加多个敏感词"""
        add_sensitives(root=self._root, words=words)


def contain(msg: str, root: Node) -> (bool, set):
    """
    文本中包含敏感词
    :return: 状态，敏感词
    """
    return api_contain(msg, root, stop=False)


def is_contain(msg: str, root: Node) -> bool:
    """
    是否包含敏感词
    """
    stat, _ = api_contain(msg, root)
    return stat

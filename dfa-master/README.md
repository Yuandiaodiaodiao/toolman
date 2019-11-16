# DFA
scan sensitive word use dfa

基于DFA的敏感词扫描模块


```buildoutcfg
__author__ = "Black"
__email__ = "cj194832@163.com"
__version = "V1.0"
```

1. 支持自定义敏感词文件
    ```python
    dfa = DFA(filename)
    ```
2. 支持动态添加单个敏感词
    ```python
    dfa.add_word(sensitive_word)
    ```
3. 支持动态添加多个敏感词
    ```python
    dfa.add_words(sensitive_words)
    ```

```python
from app.dfa import DFA

def main():
    """
    主函数入口
    """
    content = """
    毒品包括海洛因，冰毒，大麻等，我国禁止AV，三级片，禁止未成年人吸食毒品，涉黄等行为
    """
    filename = "SensitiveWord.txt"
    dfa = DFA(filename)
    dfa.add_word("毒品")
    print(dfa.dfa(content))


if __name__ == '__main__':
    main()
```

```buildoutcfg
>>> (True, {'三级片', '毒品', '海洛因', '冰毒', '大麻'})
```
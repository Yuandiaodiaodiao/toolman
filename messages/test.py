import json

a = {
    "967636480": {
        "http://www.ruanyifeng.com/blog/atom.xml": [
            "2523897396"
        ],
        "https://rsshub.app/sdu/cs/0": [
            "2523897396"
        ]
    },
    "967636481": {}
}
a.pop("967636480")
print(a)

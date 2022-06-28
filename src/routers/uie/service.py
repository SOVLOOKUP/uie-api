from typing import List, Union, Dict
from paddlenlp import Taskflow
from pprint import pprint

Schema = Union[
    # ['时间', '赛手', '赛事名称', '情感倾向[正向，负向]']  实体抽取 分类任务需要[]来设置分类的label
    str,
    # {'歌曲名称': ['歌手', '所属专辑']} 实体属性抽取
    Dict[str, List[str]]
]

class UIE:
    def __init__(self, task_path: str = None):
        self.ie = Taskflow('information_extraction', task_path, schema=[])

    def __call__(self, text: List[str], schema: Union[List[Schema], None] = None):
        if schema != None:
            self.ie.set_schema(schema)
        return self.ie(text)

def main():
    schema = ['时间', '赛事名称', {'选手': ['成绩']}] 
    ie = UIE()
    # Better print results using pprint
    pprint(ie(["2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"], schema))

if __name__ == "__main__":
    main()

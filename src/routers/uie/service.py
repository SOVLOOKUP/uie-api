from typing import List, Union, Dict
from paddlenlp import Taskflow

Schema = Union[
    # ['时间', '赛手', '赛事名称', '情感倾向[正向，负向]']  实体抽取 分类任务需要[]来设置分类的label
    str,
    # {'歌曲名称': ['歌手', '所属专辑']} 实体属性抽取
    Dict[str, List[str]]
]

class UIE(Taskflow):
    def __init__(self, task_path: str = None):
        if task_path != None:
            super().__init__('information_extraction', task_path=task_path, schema=[])
        else:
            super().__init__('information_extraction', schema=[])

    def set_schema(self, schema: Union[List[Schema], None] = None):
        return super().set_schema(schema)

    def __call__(self, text: List[str]):
        return super().__call__(text)

def main():
    schema = ['时间', '赛事名称', {'选手': ['成绩']}] 
    ie = UIE()
    ie.set_schema(schema)
    print(ie(["2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"]))

if __name__ == "__main__":
    main()

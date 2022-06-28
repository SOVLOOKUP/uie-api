import time
from fastapi import APIRouter, HTTPException
from .service import Schema, UIE
from typing import List, Union

router = APIRouter(
    prefix="/uie",
    tags=["uie models"]
)

uie_task_dict = {}
uie_info_dict = {}

# 列出所有运行的自定义 UIE 实例
@router.get("/")
async def list_uie():
    return uie_info_dict

# 创建 UIE 实例
@router.put("/")
async def create_uie(task_name: str, task_path: Union[str, None] = None):
    # 创建实例
    ie = UIE(task_path)
    uie_task_dict[task_name] = ie

    # 记录信息
    info = {
        "task_path": ie.ie.task_path(),
        "create_time": time.time(),
        "schema": []
    }
    uie_info_dict[task_name] = info
    return info

# 关闭 UIE 实例
@router.delete("/")
async def delete_uie(task_name: str):
    del uie_task_dict[task_name]
    del uie_info_dict[task_name]
    return uie_info_dict

# 运行 UIE 实例
@router.post("/")
async def run_uie(task_name: str, text: List[str], schema: Union[List[Schema], None] = None):
    uie_unit = uie_task_dict.get(task_name)

    # 没有创建这个实例
    if uie_unit == None:
        raise HTTPException(status_code=404, detail="Item not found")

    # 改变了 schema
    if schema != None:
        uie_info_dict[task_name]["schema"] = schema

    return uie_unit(text, schema)
import time
from fastapi import APIRouter, HTTPException
from .service import Schema, UIE
from typing import Dict, List, Any
import os.path
    
router = APIRouter(
    prefix="/uie",
    tags=["uie models"]
)

uie_task_dict: Dict[str, UIE] = {}
uie_info_dict: Dict[str, Dict[str, Any]] = {}

# 列出所有运行的自定义 UIE 实例
@router.get("/")
async def list_uie():
    return uie_info_dict

# 创建 UIE 实例
@router.put("/")
async def create_uie(model_name: str, model_path: str = ''):
    if model_path!= '' and not os.path.isdir(model_path):
        raise HTTPException(status_code=404, detail="Model dictory not found")

    if model_path == '':
        model_path = None
    
    # 创建实例
    ie = UIE(model_path)
    uie_task_dict[model_name] = ie

    # 记录信息
    info = {
        "model_path": ie.task_path(),
        "create_time": time.time(),
        "schema": []
    }
    uie_info_dict[model_name] = info
    return uie_info_dict

# 关闭 UIE 实例
@router.delete("/")
async def delete_uie(model_name: str):
    # 没有创建这个实例
    if uie_task_dict.get(model_name) == None:
        raise HTTPException(status_code=404, detail="Item not found")

    del uie_task_dict[model_name]
    del uie_info_dict[model_name]
    return uie_info_dict

# 设置 Schema
@router.post("/")
async def run_uie(model_name: str, schema: List[Schema]):
    uie_unit = uie_task_dict.get(model_name)

    # 没有创建这个实例
    if uie_unit == None:
        raise HTTPException(status_code=404, detail="Item not found")

    uie_unit.set_schema(schema)
    uie_info_dict[model_name]["schema"] = schema
    
    return uie_info_dict[model_name]

# 运行 UIE 实例
@router.post("/{model_name}")
async def run_uie(model_name: str, text: List[str]):
    uie_unit = uie_task_dict.get(model_name)

    # 没有创建这个实例
    if uie_unit == None:
        raise HTTPException(status_code=404, detail="Item not found")

    return uie_unit(text)
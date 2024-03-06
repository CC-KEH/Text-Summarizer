import os,sys,yaml,json
from pathlib import Path
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from src.txt_sm.logging import logger
from typing import Any
from box import ConfigBox

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path,'r') as file:
            content = yaml.safe_load(file)
            logger.info('YAML file: {path} Loaded Successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dirs(path_to_dirs: list,verbose=True):
    for path in path_to_dirs:
        os.makedirs(path,exist_ok = True)
        if verbose:
            logger.info('Successfully Created Directory at: {path}')



@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'
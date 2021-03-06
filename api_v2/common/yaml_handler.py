"""读取yaml文件"""
import os
import yaml
from config.path import config_path


def read_yaml(fpath):
    """通过fpath路径获取yaml数据,得到一个字典"""
    with open(fpath, encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data


yaml_path = os.path.join(config_path, 'config.yaml')
yaml_config = read_yaml(yaml_path)


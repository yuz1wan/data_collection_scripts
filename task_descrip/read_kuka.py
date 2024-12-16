import sys

import yaml
sys.path.append("/DATA")
import os
import json
import re



import tensorflow_datasets as tfds
import tensorflow as tf

def dataset_to_path(dataset_name: str, dir_name: str) -> str:
    version = '0.1.0'
    return f'{dir_name}/{dataset_name}/{version}'



class openx:
    def __init__(self, root):
        self.root = root

    def get_description(self):
        descips = []
        # return f'{dir_name}/{dataset_name}/{version}' dataset_name是集合里的
        # DATASET_DIR = 'data/datasets/openx_embod'
        DATASET_NAME = 'kuka'
        # DATASET_NAME = 'fractal20220817_data'
        # DATASET_NAME = 'jaco_play'
        # Load the dataset
        seen = set()
        descrip = []
        dataset = tfds.builder_from_directory(
            builder_dir=dataset_to_path(
                DATASET_NAME, self.root))
        dataset = dataset.as_dataset(split='all')
        for episode in dataset:  # 只查看前5个样本
            for step in episode['steps']:
                language_instruction = step['observation']['natural_language_instruction']
                match = re.search(r"b'(.*?)'", str(language_instruction))
                if match:
                    descrip.append(match.group(1))
                # seen.add(str(language_instruction))
                print(language_instruction.numpy().decode('utf-8'))  # 将字节转换为字符串并打印
                break  # 提取语言指令
        return descrip            
        # 将列表写入文件
        


def create_dataloader(dataset):
    if dataset == "ARIO":
        return ARIO
    elif dataset == "aloha_lerobot":
        return aloha
    elif dataset == "rh20t":
        return rh20t
    elif dataset == "openx_embod":
        return openx
    else:
        raise ValueError("dataset not supported")

def save_description(dataset):
    dataloader = create_dataloader(dataset)
    root = f"/DATA/{dataset}"
    data = dataloader(root)
    descs = data.get_description()
    # with open(f"./semantic_alignment/dataset_labels/{dataset}.txt", "w") as f:
    #     for desc in descs:
    #         f.write(desc + "\n")
    with open("./semantic_alignment/dataset_labels/kuka.txt", 'w') as file:
        for item in list(descs):
            file.write(item + '\n')

if __name__ == "__main__":
    save_description("openx_embod")
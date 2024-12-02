import sys

import yaml
sys.path.append("/DATA")
import os
import json


class aloha:
    def __init__(self, root):
        self.root = root

    def get_description(self):
        descips = []
        for task_dir in os.listdir(self.root):
            if not os.path.isdir(os.path.join(self.root, task_dir)):
                print(f"Skipping {task_dir}, not a directory")
                continue
            json_path = os.path.join(self.root, task_dir, "meta", "tasks.jsonl")
            if not os.path.exists(json_path):
                print(f"Skipping {task_dir}, no tasks.jsonl")
                continue

            tasks_dict = json.load(open(json_path))
            task_description = tasks_dict["task"]

            descips.append(task_description)
        return descips
    
    def write_node(self, nodes):
        for task_dir in os.listdir(self.root):
            if not os.path.isdir(os.path.join(self.root, task_dir)):
                print(f"Skipping {task_dir}, not a directory")
                continue
            json_path = os.path.join(self.root, task_dir, "meta", "tasks.jsonl")
            if not os.path.exists(json_path):
                print(f"Skipping {task_dir}, no tasks.jsonl")
                continue

            tasks_dict = json.load(open(json_path))
            task_description = tasks_dict["task"]
            tasks_dict["node"] = nodes[task_description]
            with open(json_path, 'w') as f:
                json.dump(tasks_dict, f, indent=4)

    def get_nodes(self):
        nodes = {}
        for task_dir in os.listdir(self.root):
            if not os.path.isdir(os.path.join(self.root, task_dir)):
                print(f"Skipping {task_dir}, not a directory")
                continue
            json_path = os.path.join(self.root, task_dir, "meta", "tasks.jsonl")
            if not os.path.exists(json_path):
                print(f"Skipping {task_dir}, no tasks.jsonl")
                continue

            tasks_dict = json.load(open(json_path))
            task_description = tasks_dict["task"]
            nodes[task_description] = tasks_dict["node"]
        return nodes

class ARIO:
    def __init__(self, root):
        self.root = root

    def get_description(self):
        descips = []
        for scene in os.listdir(self.root):
            if not os.path.isdir(os.path.join(self.root, scene)):
                print(f"Skipping {scene}, not a directory")
                continue
            scene_path = os.path.join(self.root, scene, "series-1")
            if not os.path.exists(scene_path):
                print(f"Skipping {scene}, no series-1")
                continue

            for task_dir in os.listdir(scene_path):
                if not os.path.isdir(os.path.join(scene_path, task_dir)):
                    print(f"Skipping {task_dir}, not a directory")
                    continue
                json_path = os.path.join(scene_path, task_dir, "description.yaml")
                if not os.path.exists(json_path):
                    print(f"Skipping {task_dir}, no tasks.jsonl")
                    continue

                # load yaml file
                with open(json_path, 'r') as stream:
                    try:
                        tasks_dict = yaml.safe_load(stream)
                    except yaml.YAMLError as exc:
                        print(exc)

                # print(tasks_dict)
                task_description = tasks_dict["instruction_EN"]

                descips.append(task_description)

        return descips
    
    def write_node(self, nodes):
        for scene in os.listdir(self.root):
            if not os.path.isdir(os.path.join(self.root, scene)):
                print(f"Skipping {scene}, not a directory")
                continue
            scene_path = os.path.join(self.root, scene, "series-1")
            if not os.path.exists(scene_path):
                print(f"Skipping {scene}, no series-1")
                continue

            for task_dir in os.listdir(scene_path):
                if not os.path.isdir(os.path.join(scene_path, task_dir)):
                    print(f"Skipping {task_dir}, not a directory")
                    continue
                json_path = os.path.join(scene_path, task_dir, "description.yaml")
                if not os.path.exists(json_path):
                    print(f"Skipping {task_dir}, no tasks.jsonl")
                    continue

                tasks_dict = yaml.load(open(json_path))
                task_description = tasks_dict["instruction_EN"]
                tasks_dict["node"] = nodes[task_description]
                with open(json_path, 'w') as f:
                    yaml.dump(tasks_dict, f)

    def get_nodes(self):
        nodes = {}
        for scene in os.listdir(self.root):
            if not os.path.isdir(os.path.join(self.root, scene)):
                print(f"Skipping {scene}, not a directory")
                continue
            scene_path = os.path.join(self.root, scene, "series-1")
            if not os.path.exists(scene_path):
                print(f"Skipping {scene}, no series-1")
                continue

            for task_dir in os.listdir(scene_path):
                if not os.path.isdir(os.path.join(scene_path, task_dir)):
                    print(f"Skipping {task_dir}, not a directory")
                    continue
                json_path = os.path.join(scene_path, task_dir, "description.yaml")
                if not os.path.exists(json_path):
                    print(f"Skipping {task_dir}, no tasks.jsonl")
                    continue

                tasks_dict = yaml.load(open(json_path))
                task_description = tasks_dict["instruction_EN"]
                nodes[task_description] = tasks_dict["node"]
        return nodes
    
if __name__ == "__main__":
    root = "/DATA/ARIO"
    ario = ARIO(root)
    descs = ario.get_description()
    print(descs)
    # nodes = ario.get_nodes()
    # print(nodes)
    # ario.write_node(nodes)
    # 写入txt文件
    with open("task_descrip/ario.txt", "w") as f:
        for desc in descs:
            f.write(desc + "\n")

    print("=====================================")
    root = "/DATA/aloha_lerobot"
    aloha = aloha(root)
    descs = aloha.get_description()
    print(descs)
    # nodes = aloha.get_nodes()
    # print(nodes)
    # aloha.write_node(nodes)
    # 写入txt文件
    with open("task_descrip/aloha.txt", "w") as f:
        for desc in descs:
            f.write(desc + "\n")
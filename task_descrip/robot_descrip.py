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
    
class rh20t:
    def __init__(self, root):
        self.root = root

    def get_description(self):
        descips = []
        json_path = os.path.join(self.root, "task_description.json")
        if not os.path.exists(json_path):
            print(f"Skipping {task_dir}, no task_description.json")
            return descips

        tasks_dict = json.load(open(json_path))
        for key, task in tasks_dict.items():
            task_description = task["task_description_english"]
            descips.append(task_description)
        return descips

    def write_node(self, nodes):
        json_path = os.path.join(self.root, "task_description.json")
        if not os.path.exists(json_path):
            print(f"Skipping {task_dir}, no task_description.json")
            return

        tasks_dict = json.load(open(json_path))
        for task in tasks_dict:
            task_description = task["task_description_english"]
            task["node"] = nodes[task_description]
        with open(json_path, 'w') as f:
            json.dump(tasks_dict, f, indent=4)

    def get_nodes(self):
        nodes = {}
        json_path = os.path.join(self.root, "task_description.json")
        if not os.path.exists(json_path):
            print(f"Skipping {task_dir}, no task_description.json")
            return nodes

        tasks_dict = json.load(open(json_path))
        for task in tasks_dict:
            task_description = task["task_description_english"]
            nodes[task_description] = task["node"]
        return nodes

def create_dataloader(dataset):
    if dataset == "ARIO":
        return ARIO
    elif dataset == "aloha_lerobot":
        return aloha
    elif dataset == "rh20t":
        return rh20t
    else:
        raise ValueError("dataset not supported")

def save_description(dataset):
    dataloader = create_dataloader(dataset)
    root = f"/DATA/{dataset}"
    data = dataloader(root)
    descs = data.get_description()
    with open(f"./semantic_alignment/dataset_labels/{dataset}.txt", "w") as f:
        for desc in descs:
            f.write(desc + "\n")


if __name__ == "__main__":
    save_description("rh20t")
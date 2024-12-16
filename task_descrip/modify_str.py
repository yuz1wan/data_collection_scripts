import re

# 文件路径
file_path = "fractal_unique_strings.txt"

# Step 1: 读取文件内容
with open(file_path, 'r') as file:
# Step 2: 使用正则表达式提取并替换 tf.Tensor(b'...') 部分
# 匹配 tf.Tensor(b'...') 中的 b'...' 内容

    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(lines)
    line1 = []
    for line in lines:
        match = re.search(r"b'(.*?)'", line)
        if match:
            line1.append(match.group(1))
    # lines = [re.search(r"b'(.*?)'", line).group(1) for line in lines]

    # Step 2: 去除每行末尾的换行符（可选）
# Step 3: 将修改后的内容写回文件
with open(file_path, 'w') as file:
    # 使用 writelines 时需要手动添加换行符
    file.writelines(line + '\n' for line in line1)

print("文件已更新")

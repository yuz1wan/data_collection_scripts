# 命令行输入参数
# $1: 数据集名称
# $2: 数据集REPO地址

DATA=$1
DOWNLOAD_PATH=$2

# 如果路径不存在则创建
if [ ! -d "../../${DATA}" ]; then
    mkdir -p ../../${DATA}
fi

export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --repo-type dataset --resume-download ${DOWNLOAD_PATH} --local-dir ../../${DATA}

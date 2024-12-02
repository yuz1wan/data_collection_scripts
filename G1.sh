conda activate rdt

echo "G1_Pouring_Dataset start at $(date)" >> G1_log.txt
source hf_download.sh G1/G1_Pouring_Dataset unitreerobotics/G1_Pouring_Dataset
echo "G1_Pouring_Dataset end at $(date)" >> G1_log.txt

echo "UnitreeG1_DualArmGrasping start at $(date)" >> G1_log.txt
source hf_download.sh G1/UnitreeG1_DualArmGrasping unitreerobotics/UnitreeG1_DualArmGrasping
echo "UnitreeG1_DualArmGrasping end at $(date)" >> G1_log.txt

echo "G1_ObjectPlacement_Dataset start at $(date)" >> G1_log.txt
source hf_download.sh G1/G1_ObjectPlacement_Dataset unitreerobotics/G1_ObjectPlacement_Dataset
echo "G1_ObjectPlacement_Dataset end at $(date)" >> G1_log.txt

echo "G1_CameraPackaging_Dataset start at $(date)" >> G1_log.txt
source hf_download.sh G1/G1_CameraPackaging_Dataset unitreerobotics/G1_CameraPackaging_Dataset
echo "G1_CameraPackaging_Dataset end at $(date)" >> G1_log.txt

# 发送邮件提醒
source mail.sh "G1数据集下载结束" "G1 Downloading Finished. Please check the log file for details."
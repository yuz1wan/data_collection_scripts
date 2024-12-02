conda activate rdt

echo "aloha_mobile_cabinet start at $(date)" >> aloha_log.txt
source hf_download.sh aloha_lerobot/aloha_mobile_cabinet lerobot/aloha_mobile_cabinet
echo "aloha_mobile_cabinet end at $(date)" >> aloha_log.txt

echo "aloha_mobile_chair start at $(date)" >> aloha_log.txt
source hf_download.sh aloha_lerobot/aloha_mobile_chair lerobot/aloha_mobile_chair
echo "aloha_mobile_chair end at $(date)" >> aloha_log.txt

echo "aloha_mobile_wipe_wine start at $(date)" >> aloha_log.txt
source hf_download.sh aloha_lerobot/aloha_mobile_wipe_wine lerobot/aloha_mobile_wipe_wine
echo "aloha_mobile_wipe_wine end at $(date)" >> aloha_log.txt

echo "aloha_mobile_wash_pan start at $(date)" >> aloha_log.txt
source hf_download.sh aloha_lerobot/aloha_mobile_wash_pan lerobot/aloha_mobile_wash_pan
echo "aloha_mobile_wash_pan end at $(date)" >> aloha_log.txt

echo "aloha_mobile_elevator start at $(date)" >> aloha_log.txt
source hf_download.sh aloha_lerobot/aloha_mobile_elevator lerobot/aloha_mobile_elevator
echo "aloha_mobile_elevator end at $(date)" >> aloha_log.txt

# 发送邮件提醒
source mail.sh "aloha_lerobot数据集下载结束" "aloha_lerobot Downloading Finished. Please check the log file for details."
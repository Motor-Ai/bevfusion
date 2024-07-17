source tools/download_pretrained.sh
torchpack dist-run -np 4 python tools/train.py configs/nuscenes/det/transfusion/secfpn/lidar/voxelnet_0p075.yaml
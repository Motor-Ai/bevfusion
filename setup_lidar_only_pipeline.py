import argparse
import subprocess

if __name__ == '__main__':
    subprocess.run(["bash", "bash_scripts/conda_deps.sh"])
    subprocess.run(["bash", "bash_scripts/torch_deps.sh"])
    subprocess.run(["bash", "bash_scripts/git_source_deps.sh"])
    subprocess.run(["bash", "bash_scripts/openmim_deps.sh"])
    subprocess.run(["python", "mmdet3d_setup.py", "develop"])
    subprocess.run(["bash", "bash_scripts/train_lidar_only.sh"])
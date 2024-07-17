import argparse
import subprocess

if __name__ == '__main__':
    subprocess.run(["bash", "bash_scripts/system_deps.sh"])
    subprocess.run(["bash", "bash_scripts/torch_deps.sh"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    subprocess.run(["bash", "bash_scripts/source_deps.sh"])
    subprocess.run(["bash", "bash_scripts/openmim_deps.sh"])
    subprocess.run(["python", "setup.py", "develop"])
    subprocess.run(["bash", "bash_scripts/train_lidar_only.sh"])
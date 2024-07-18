# apt-get install libgl1-mesa-glx libglib2.0-0 -y
# apt-get install openmpi-bin openmpi-common libopenmpi-dev libgtk2.0-dev git -y
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install gtk3
conda install openmpi
pip install --force-reinstall pip==23.1.2
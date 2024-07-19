conda config --add channels conda-forge
conda config --set channel_priority strict
conda install gtk3
conda install openmpi
pip install --force-reinstall pip==23.1.2
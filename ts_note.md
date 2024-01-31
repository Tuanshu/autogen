依照https://microsoft.github.io/autogen/docs/installation/Docker

docker build -f .devcontainer/full/Dockerfile -t autogen_full_img https://github.com/microsoft/autogen.git


同時也run conda環境 (這是為了要玩notebook)
conda create -n pyautogen python=3.10

conda activate pyautogen

pip uninstall pyautogen

pip install -e .
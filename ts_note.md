依照https://microsoft.github.io/autogen/docs/installation/Docker

docker build -f .devcontainer/full/Dockerfile -t autogen_full_img https://github.com/microsoft/autogen.git


同時也run conda環境 (這是為了要玩notebook)
conda create -n pyautogen python=3.10

conda activate pyautogen

pip uninstall pyautogen

pip install -e .

使用generate_oai_reply方法決定下一個agent.
要求他在複數agents中選擇, 但使用內網模型經常會失敗

在這裡沒有explictly指定llm, 有可能是不小心用到deepseek
待會改順序可能有幫助
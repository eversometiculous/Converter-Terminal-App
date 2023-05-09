# !/bin/bash

python3 -m venv converter-venv
source converter-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py #*insert inputfile_name.ext* *insert format you want* *insert file_name you want*
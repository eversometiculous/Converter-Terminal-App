# !/bin/bash

python3 -m venv converter-venv
source converter-venv/bin/activate
pip3 install argparse markdown pdfkit PyPDF2 html2text
clear
python3 main.py
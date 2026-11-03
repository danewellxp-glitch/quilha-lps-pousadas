#!/usr/bin/env bash
# Prepara o ambiente do gerador (rodar uma vez por sessão/máquina, de dentro da pasta gerador/)
set -e
pip install --break-system-packages -q jinja2 pillow numpy "opencv-contrib-python-headless==4.10.0.84" playwright 2>/dev/null || \
pip install -q jinja2 pillow numpy "opencv-contrib-python-headless==4.10.0.84" playwright
mkdir -p models
[ -f models/FSRCNN_x2.pb ] || curl -sSLo models/FSRCNN_x2.pb https://raw.githubusercontent.com/Saafke/FSRCNN_Tensorflow/master/models/FSRCNN_x2.pb
python3 -c "import cv2;assert hasattr(cv2,'dnn_superres');print('ok opencv',cv2.__version__)"

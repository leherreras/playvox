#!/usr/bin/env bash

echo "[INFO] Move to src folder"
cd src

echo "[INFO] Installing dependencies ..."
pip install -r requirements.txt


echo "[INFO] Run webserver"

cd ..
export PYTHONPATH=/opt/playvox/src/
echo "[INFO] Running the app ..."
export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST=0.0.0.0
export FLASK_APP=src/app.py

flask run
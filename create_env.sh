#!/bin/bash
python virtualenv.py dev \
&& rm virtualenv.pyc \
&&source dev/bin/activate \
&& pip install -r requirements.txt \
&& deactivate
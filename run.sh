export RUN_OPT=../config.py

source venv/bin/activate
sudo restart kkuziri

tail -f /var/log/uwsgi/kkuziri.log

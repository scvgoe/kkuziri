export RUN_OPT=../config.py

source venv/bin/activate
docker-compose up -d postgresql
python wsgi.py

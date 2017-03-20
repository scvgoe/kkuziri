import os
import subprocess
import datetime

import boto3
from kkuziri import s3_client

BUCKET_NAME = 'kkuziri-backup'

def backup():
    now = datetime.datetime.now()

    filename = '/backup/' + str(now)

    result = subprocess.call(
        ['docker exec -i $(docker ps -f \'name=kkuziri_postgresql_1\' -q) \
                pg_dump -U kkuziri > \'%s\'' % (filename)],
        shell=True,
        stdout=subprocess.PIPE
    )

    print result

    print 'Uploading %s to Amazon S3...' % filename
    _upload(filename)

def _upload(filename):
    with open(filename, 'rb') as data:
        s3_client.upload_fileobj(data, BUCKET_NAME, os.path.basename(filename))

if __name__=='__main__':
    backup()

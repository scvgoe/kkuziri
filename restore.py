import os
import subprocess
import datetime
import json

import boto3
from kkuziri import s3_client

BUCKET_NAME = 'kkuziri-backup'

def restore():
    filename = _download()

    result = subprocess.call(
        ['docker exec -i $(docker ps -f \'name=kkuziri_postgresql_1\' -q) \
            psql -U kkuziri < \'%s\'' % (filename)],
        shell=True,
        stdout=subprocess.PIPE
    )
    print result


def _download():
    response = s3_client.list_objects(
	Bucket=BUCKET_NAME
    )

    sorted_contents = sorted(response['Contents'], key=lambda obj: \
            obj['LastModified'], reverse=True)

    key = sorted_contents[0]['Key']
    filename = '/backup/' + key

    print 'Downloading %s from Amazon S3...' % key

    with open(filename, 'wb') as data:
        s3_client.download_fileobj(BUCKET_NAME, key, data)

    return filename

if __name__=='__main__':
    restore()

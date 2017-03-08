#!/bin/sh

docker pull palobo/certbot

GetCert() {
    docker run -it \
        --rm \
        -p 443:443 \
        -v $(pwd)/letsencrypt/etc:/etc/letsencrypt \
        -v $(pwd)/letsencrypt/log:/var/log/letsencrypt \
        palobo/certbot certonly --standalone -t  \
        $@
}

echo "Getting certificates..."
GetCert -m scvgoe@gmail.com -d kkuziri.io

echo "Done"

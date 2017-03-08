#!/bin/sh

docker pull palobo/certbot

GetCert() {
    docker run -it \
        --rm \
        -v ./letsencrypt/etc:/etc/letsencrypt \
        -v ./letsencrypt/lib:/var/lib/letsencrypt \
        -v ./letsencrypt/www:/var/www/.well-known \
        palobo/certbot -t certonly --webroot -w /var/www \
        --keep-until-expiring \
        $@
}

echo "Getting certificates..."
GetCert -d kkuziri.io

echo "Restarting kkuziri..."
docker-compose down
docker-compose up -d

echo "Done"

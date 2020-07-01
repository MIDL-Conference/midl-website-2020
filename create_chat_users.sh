#!/bin/bash -ex


TOKEN=9Idc0_ce14KxYqFQ_Z5FJa9oe652foQ3d-pX-2A5rYE
ID=5tvBJ6z2z2DRiEGiA


while IFS=, read -r name email
do
        password=`openssl rand -hex 8`
        username=`echo $name | tr ' ' '.' | awk '{print tolower($0)}'`
        echo $name $email $password $username
        curl -H "X-Auth-Token: $TOKEN" \
             -H "X-User-Id: $ID" \
             -H "Content-type:application/json" \
             http://localhost:3000/api/v1/users.create \
             -d '{"name": "'"$name"'", "email": "'"$email"'", "password": "'"$password"'", "username": "'"$username"'", "requirePasswordChange": true, "verified": false, "sendWelcomeEmail": true, "joinDefaultChannels": false}'
done < to_create.csv


# curl -H "X-Auth-Token: 9Idc0_ce14KxYqFQ_Z5FJa9oe652foQ3d-pX-2A5rYE" \
#      -H "X-User-Id: 5tvBJ6z2z2DRiEGiA" \
#      -H "Content-type:application/json" \
#      http://localhost:3000/api/v1/users.create \
#      -d '{"name": "Cd midl", "email": "cdmidl@hoel.kervadec.bzh", "password": "7359a2e6ad9d138f", "username": "cd.midl", "requirePasswordChange": true, "verified": false, "sendWelcomeEmail": true, "joinDefaultChannels": false}'

curl -H "X-Auth-Token: 9Idc0_ce14KxYqFQ_Z5FJa9oe652foQ3d-pX-2A5rYE" \
     -H "X-User-Id: 5tvBJ6z2z2DRiEGiA" \
     -H "Content-type:application/json" \
     http://localhost:3000/api/v1/users.create \
     -d '{"name": "Auto Test 2", "email": "autotest2@hoel.kervadec.science", "password": "ihugdbksyt", "username": "autotest2", "requirePasswordChange": true, "verified": false, "sendWelcomeEmail": true}'

curl -H "X-Auth-Token: 9Idc0_ce14KxYqFQ_Z5FJa9oe652foQ3d-pX-2A5rYE" -H "X-User-Id: 5tvBJ6z2z2DRiEGiA" -H "Content-type:application/json" http://localhost:3000/api/v1/users.create -d '{"name": "Coco lasticot", "email": "coco@hoel.kervadec.bzh", "password": "afc8be795e64ff9a", "username": "coco.lasticot", "requirePasswordChange": true, "verified": false, "sendWelcomeEmail": true, "joinDefaultChannels": false}'

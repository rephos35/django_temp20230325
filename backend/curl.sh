#! /bin/bash

# ok
curl -X POST -H 'Content-Type: application/json' -d '{"account": "t1", "email": "t1@mail.com", "name": "flaky", "password": "1234", "phone": "123"}' http://192.168.91.130:8787/api/accounts/register/
curl -X POST -d 'account=t1&password=1234' http://192.168.91.130:8787/api/accounts/login/
curl -X POST http://192.168.91.130:8787/api/accounts/logout/



# 192.168.6.128
curl -X POST -H 'Content-Type: application/json'   -d '{"account": "t1", "email": "t1@mail.com", "name": "flaky", "password": "1234", "phone": "123", "g-recaptcha-response": "PASSED"}' http://192.168.6.128:8787/api/accounts/register/
curl -X POST -H 'Content-Type: application/json' -d '{"account": "t1", "password": "1234", "g-recaptcha-response": "PASSED"}' http://192.168.6.128:8787/api/accounts/login/
curl -X POST http://192.168.6.128:8787/api/accounts/logout/

# 192.168.91.130
curl -X POST -H 'Content-Type: application/json'   -d '{"account": "t1", "email": "t1@mail.com", "name": "flaky", "password": "1234", "phone": "123", "g-recaptcha-response": "PASSED"}' http://192.168.91.130:8787/api/accounts/register/
curl -X POST -H 'Content-Type: application/json' -d '{"account": "t1", "password": "1234", "g-recaptcha-response": "PASSED"}' http://192.168.91.130:8787/api/accounts/login/
curl -X POST http://192.168.91.130:8787/api/accounts/logout/


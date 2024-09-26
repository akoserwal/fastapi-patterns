

```python -m uvicorn main:app --reload```


```uvicorn main:app --host 0.0.0.0 --port 8000 \
    --ssl-keyfile=./tls-certs/server-key.pem \
    --ssl-certfile=./tls-certs/server-cert.pem \
    --ssl-ca-certs=./tls-certs/ca-cert.pem \
    --ssl-cert-reqs 1
 ```

 --ssl-keyfile TEXT              SSL key file
  --ssl-certfile TEXT             SSL certificate file
  --ssl-keyfile-password TEXT     SSL keyfile password
  --ssl-version INTEGER           SSL version to use (see stdlib ssl module's)
                                  [default: 17]
  --ssl-cert-reqs INTEGER         Whether client certificate is required (see
                                  stdlib ssl module's)  [default: 0]
  --ssl-ca-certs TEXT             CA certificates file
  --ssl-ciphers TEXT          



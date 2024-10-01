# Securing FastAPI mTLS with Self-Signed Certificates

FastAPI application and a Python client using mTLS with self-signed certificates.

# Run API 

Activate virtual venv
`source .venv/bin/activate`

## Run API using unicorn
```python -m uvicorn main:app --reload```


## Run API using unicorn with TLS
```uvicorn main:app --host 0.0.0.0 --port 8000 \
    --ssl-keyfile=./tls-certs/server-key.pem \
    --ssl-certfile=./tls-certs/server-cert.pem \
    --ssl-ca-certs=./tls-certs/ca-cert.pem \
    --ssl-cert-reqs 1
 ```

## Client
```python client.py```

# TLS certs
[tls-certs](./tls-certs)

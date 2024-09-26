#!/bin/bash

# Default values for certificate details
DAYS_VALID=365000
BITS=2048

# Prompt for inputs
read -p "Enter Country (2 letter code) [US]: " COUNTRY
COUNTRY=${COUNTRY:-US}

read -p "Enter State or Province [California]: " STATE
STATE=${STATE:-California}

read -p "Enter Locality (City) [San Francisco]: " LOCALITY
LOCALITY=${LOCALITY:-San Francisco}

read -p "Enter Organization [My Company]: " ORGANIZATION
ORGANIZATION=${ORGANIZATION:-My Company}

read -p "Enter Common Name for CA [MyCA]: " CA_CN
CA_CN=${CA_CN:-MyCA}

read -p "Enter Common Name for Server [localhost]: " SERVER_CN
SERVER_CN=${SERVER_CN:-localhost}

read -p "Enter Common Name for Client [client]: " CLIENT_CN
CLIENT_CN=${CLIENT_CN:-client}

# Prompt for passwords
echo "Enter password for CA private key:"
read -s CA_PASSWORD
echo "Confirm password for CA private key:"
read -s CA_PASSWORD_CONFIRM
if [ "$CA_PASSWORD" != "$CA_PASSWORD_CONFIRM" ]; then
    echo "Passwords do not match. Exiting..."
    exit 1
fi

echo "Enter password for Server private key:"
read -s SERVER_PASSWORD
echo "Confirm password for Server private key:"
read -s SERVER_PASSWORD_CONFIRM
if [ "$SERVER_PASSWORD" != "$SERVER_PASSWORD_CONFIRM" ]; then
    echo "Passwords do not match. Exiting..."
    exit 1
fi

echo "Enter password for Client private key:"
read -s CLIENT_PASSWORD
echo "Confirm password for Client private key:"
read -s CLIENT_PASSWORD_CONFIRM
if [ "$CLIENT_PASSWORD" != "$CLIENT_PASSWORD_CONFIRM" ]; then
    echo "Passwords do not match. Exiting..."
    exit 1
fi

# Generate a private key for the CA
echo "Generating CA private key..."
openssl genrsa -aes256 -passout pass:$CA_PASSWORD $BITS > ca-key.pem

# Generate the X509 certificate for the CA
echo "Generating CA certificate..."
openssl req -new -x509 -nodes -days $DAYS_VALID \
  -key ca-key.pem -passin pass:$CA_PASSWORD \
  -out ca-cert.pem \
  -subj "/C=$COUNTRY/ST=$STATE/L=$LOCALITY/O=$ORGANIZATION/CN=$CA_CN"

# Create a configuration file for the server certificate
echo "Creating OpenSSL config file for server certificate (localhost)..."
cat > localhost.cnf <<EOL
[ req ]
default_bits       = $BITS
distinguished_name = req_distinguished_name
req_extensions     = req_ext
x509_extensions    = v3_ext
prompt             = no

[ req_distinguished_name ]
C  = $COUNTRY
ST = $STATE
L  = $LOCALITY
O  = $ORGANIZATION
CN = $SERVER_CN

[ req_ext ]
subjectAltName = @alt_names

[ v3_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = localhost
EOL

# Generate the private key and certificate request for the server
echo "Generating server private key and CSR..."
openssl genrsa -aes256 -passout pass:$SERVER_PASSWORD -out server-key.pem $BITS
openssl req -new -key server-key.pem -passin pass:$SERVER_PASSWORD -out server-req.pem -config localhost.cnf

# Generate the X509 certificate for the server signed by the CA
echo "Generating server certificate..."
openssl x509 -req -days $DAYS_VALID -set_serial 01 \
  -in server-req.pem \
  -out server-cert.pem \
  -CA ca-cert.pem \
  -CAkey ca-key.pem \
  -passin pass:$CA_PASSWORD \
  -extfile localhost.cnf \
  -extensions v3_ext

# Generate the private key and certificate request for the client
echo "Generating client private key and CSR..."
openssl genrsa -aes256 -passout pass:$CLIENT_PASSWORD -out client-key.pem $BITS

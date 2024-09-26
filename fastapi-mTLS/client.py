import httpx

# Client certificate and key
client_cert = ("./tls-certs/client-cert.pem", "./tls-certs/client-key.pem")
ca_cert = "./tls-certs/ca-cert.pem"


def data():
    try:
        with httpx.Client(verify=ca_cert, cert=client_cert) as client:
            response = client.get("https://localhost:8000/data")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code}: {e.response.text}")
    except Exception as e:
        print(f"Request failed: {e}")


def root():
    try:
        with httpx.Client(verify=ca_cert, cert=client_cert) as client:
            response = client.get("https://localhost:8000")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code}: {e.response.text}")
    except Exception as e:
        print(f"Request failed: {e}")


def hello():
    try:
        with httpx.Client(verify=ca_cert, cert=client_cert) as client:
            response = client.get("https://localhost:8000/hello/test")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code}: {e.response.text}")
    except Exception as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    data = data()
    root = root()
    hello = hello()
    print(hello)
    print(root)
    print(data)

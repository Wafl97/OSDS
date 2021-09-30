# L5

## E1

```
openssl genrsa -des3 -out rootCA.key 2048

openssl req -x509 -new -nodes -key rootCA.key .sha256 -days 1024 -out rootCA.pem

openssl req -new -shq256 -nodes -out server.csr -newkey rsa:2048 -keyout nice.key

touch v3.ext
```
v3.ext
```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
```
```
openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreatserial -out nice.crt -days 1000 -sha256 -extfile v3.ext

openssl x509 -in nice.crt -text -nout

openssl verify -CAfile rootCA.pem nice.crt
```


## E2

Nav to php dir

```
sudo docker build -t l2e2 .

sudo docker tag l2e2 wafl/l2e2

sudo docker push wafl/l2e2
```

Nav to mysql dir

```
sudo docker build -t l2e4.

sudo docker tag l2e4 wafl/l2e4

sudo docker push wafl/l2e4
```

## E4

install kubernetes (kubectl)

place the config file in home/.kube

## E5

Nav to E5
```
kubectl apply -f .

kubectl get pods

kubectl delete -f .
```


## E6

make a yml and deploy it -_-



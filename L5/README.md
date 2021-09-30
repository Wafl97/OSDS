# L5

## E1

```
openssl genrsa -des3 -out rootCA.key 2048

openssl req -x509 -new -nodes -key rootCA.key .sha256 -days 1024 -out rootCA.pem
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


# L3

## E1

```
docker run -it --rm --network='host' apline
```

link = MAC
addr = ip


## E2

```
ip addr add 192.168.16.16/16 dev eth0

ip route add 192.168.0.0/16 dev eth0

ping [ip from other on network]
```

* This does not work on WSL2 because windows internal routing

## E3



## E4



## E5

One-to-Many NAT bruges til at mappe en offentlig ip adresse til flere private adresser.

Basic NAT kan bruges til at connecte to inkompatible netværk. 

Hjælper med at løse konflikter mellem samme ip adresser. Bruges meget i IPv4, da IPv4 er ved at løbe tør for addresser.

## E6

En protocol det tildeler ip adresser til enheder

Arbejder sammen med NAT på den lokale side at routeren

Uddeler en ip til en enheder når det skal bruges

## E7

Firewall
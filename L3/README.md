# L3

## E1

```
docker run -it --rm --network='host' apline
```

link = MAC
addr = ip


## E2

```
ip addr show
```
Here we can find the interface.
In this case it was `eth0`

```
ip addr add 192.168.16.16/16 dev eth0

ip route add 192.168.0.0/16 dev eth0

ping [ip from other on network]
```

* This does not work on WSL2 because windows internal routing

## E3

TCP/IP vs OSI

## E4

Hvordan kommer en besked fra A til B gennem et netwærk

## E5 - NAT


SNAT - skifter source

DNAT - skifter destination 

One-to-Many NAT bruges til at mappe en offentlig ip adresse til flere private adresser.

Basic NAT kan bruges til at connecte to inkompatible netværk. 

Hjælper med at løse konflikter mellem samme ip adresser. Bruges meget i IPv4, da IPv4 er ved at løbe tør for addresser.

## E6 - DHCP

En protocol det tildeler ip adresser til enheder

Arbejder sammen med NAT på den lokale side at routeren

Uddeler en ip til en enheder når det skal bruges

## E7 - Firewall

Et knude punk for indgående kommunikation

Fungere som en slaks dørmand, bestemmer hvad der er tiladt adgang og hvad der er nægtet
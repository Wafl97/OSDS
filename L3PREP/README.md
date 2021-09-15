# L3 PREP

# iproute2

- open a linux container with docker:
```powershell
docker run -it --rm --network='host' ubuntu /bin/bash
```
- update linux and get the `iproute2` package:
```bash
apt-get update

apt-get install iproute2
```
- use the ip command:
```bash
ip addr show
```
- other commands:

| Command                 | Note                                 |
|:------------------------|--------------------------------------|
| ip addr, ip link, ip -s | Address and link configuration       |
| ip route                | Routing tables                       |
| ip neigh                | Neighbors                            |
| ip tunnel               | Tunnels                              |
| ip link set name        | Rename network interfase             |
| ip maddr                | Multicast                            |
| ip -s, ss, ip route     | Show various networking statistics   |
| brigde                  | Handle brigde addressing and devices |
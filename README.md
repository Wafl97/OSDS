# OSDS

## VM/Containers

Infrastucture -> Host OS -> Hypervisor -> Guest OS -> bins/libs -> App

Infrastucture -> Host OS -> Dockerengine -> bins/libs -> App

Dockerfile -$ docker build -t \<tag> \<file>> Docker image -docker run <tag>> Docker container


## Kubernetes

.yaml of .json

Container Orchestation

Pods: Contains containers

Deployments: Manages replicators for pods among nodes in cluster

Services: Exposes a set of pods on the cluster

## Linux

## Network

OSI-Model (all networks):

    1. Application (HTTP)
    2. Presentation
    3. Session
    4. Transport (TCP/UDP)
    5. Network
    6. Data link
    7. Physical

TCP/IP model(only internet):

    5. Application:    HTTP, FTP, SMTP, DNS, RPC...                         Data
    4. Transport:      TCP, UDP (addressing with ports)                     Segment
    3. Network:        IP (addressing with ip addresses)                    Packet
    2. Data link:      Ethernet, Wifi, ARP (addressing with MAC addresses)  Frame
    1. Physical:       10BASE-T, 802.11 (addressing with wires)             Bits

Physical (Layer 1):

    100BASE-T
    Cat5 cables, twisted pair
    4B5B (line coding)
    MTL-3 (line coding)

    Encoding
    Filtering
    Electronics
    Error detection/correction

Data link (Layer 2):

    MAC addresses (unique interface ID)

    Error detection
    Error correction
    Switches

Network (Layer 3):

    IP addresses
    CIDR
    Routing


Loadbalancing (layer 4) IPs and Ports:

    Round robin
    Least connections
    Sticky session/hash

Loadbalancing (layer 7) HTTP header information:

    SSL/TLS-termination
    HTTP routing
    Header rewriting
    Authenticated users

## Protocols

IP - Internet Protocol

    v4
    32 bits
    
    v6
    128 bits

DHCP - Dynamic Host Configuration Protocol

    1 server on network
    multiple clients

TCP
    
    SYN -> SYN/ACK -> ACK

HTTP

    Request (method, resources, headers, content)
    Respone (status code, headers, content)

    Methods:
       - GET
       - POST
       - PUT
       - PATCH
       - DELETE
       - HEAD
       - ...

    Status codes:
       - 1-- information
       - 2-- successful
       - 3-- redirection
       - 4-- client error
       - 5-- server error

SSL/TLS

    encryption
    intregrity

    TLS 1.2:
        Client hello
        Server hello
        Certificate
        Server key exchange
        Server hello done
        Client key exchange
        Change cipher spec (Client)
        Finished (Client)
        Change cipher spec (Server)
        Finished (Server)


## Archetectures

Centralized - one nodes does everything

Distributed - nodes distribute work on sub-nodes

Decentralized - nodes are only connected to peers

Client-Server

    Server
       - Resources
    Client
       - Needs resources

Broker

    Clients contact a broker insted of a server
    The broker connects the client with a server


Peer-2-Peer

    Direct connection between peers

    example:
       - Bittorrent

Monolithic Architecture

    All in one program

Service Oriented Architecture (SOA)

    More than one service

Microservice Architecture

    Every function is its own small program

    Good for scaling out

## OS

Resources management:

    Processing(Scheduling)
    Memory
    Storage

Layers:

    Program
    Shell
    Kernal
    Hardware

Boot:

    BIOS - Basic I/O System (Firmware on motherboard)
       - Perform POST
       - Loads MBR
    MBR - Master Boot Record
       - Loads GRUB2 boot loader
    GRUB2
       - Loads the `vmlinuz` kernal image
       - Extracts the contents of `initramfs` images
    Kernal
       - Loads necessary driver modules from initrd image
       - Starts systems 1st process - `systemd`
    Systemd
       - Reads configuration files from the `etc/systemd` directory
       - Reads file linked by `etc/systemd/system/deafult.target`
       - Brings the system to the state definded by system target

## Storage

Partition

    Split a drive into different parts

Filesystem

    Logical     OPEN, CLOSE, READ, WRITE...
    Virtual
    Phycial     HDD, SSD, CD, DVD

Filetypes

    .so  .s     .ddl        Object or linked libraries
    .sh         .bat        Shell scripts
    .deb        .msi        Installers
    .tar.gz     .zip        Compressed files
    .bin        .exe        Executables

Directory

    1. Filename, file index(inode) - Most used, Linux
    2. Filename, metadata, pointer to data - FAT, Microsoft

FAT - File Alloctaion Table

Indexed Allocation

    Filename -> Inode -> Data
    Contains...
    Metadata
    Direct block pointers(12) to block data
    Indirect block pointers(single, double, triple) to direct block pointer to block data

RAID - Redundant Array of Indipendent Disks

    0
       - Split data across multiple drives
       - +Preformance
       - -Reliability
       - Tolerance: None
       - Min 2 Drives
    1
       - Dublicate data across multiple drives
       - +Reliability
       - +Read performance
       - -Waste of disks 
       - Tolerance: n-1 drives
       - Min 2 Drives
    2
       - .
       - Tolerance: 1 drive
       - Min 3 Drives
    3
       - .
       - Tolerance: 1 drive
       - Min 3 Drives
    4
       - .
       - Tolerance: 1 drive
       - Min 3 Drives
    5
       - Split data and parity bit on multiple disks
       - +Reliability
       - -Wasted disk space. Loss in performance
       - Tolerance: 1 drive
       - Min 3 Drives
    6
       - Split data and parity bits on multiple disks
       - Use two dirves for redunancy
       - +Reliability
       - -Wasted disk space. Loss in performance
       - Tolerance: 2 drives
       - Min 4 Drives

## Multithreading

Multitastking

- Process-based
- Programs run by OS
- Easier development
- Memoty overhead

Multithreading

- Thread-based
- Threads within programs
- Faster (if the CPU has multiple cores)
- Error prone

Hyper-Threading - A core split into threads

A program has process, a process can have multiple threads, and a job is multiple processes

Task

    Is..
    A peace of work
    Run as a thread or process
    Implemented as a method/function

    Can be...
    Ready
    Running
    Terminated
    Blocked

Thread and process

    Threads
      - Share memoty, file descriptors
    Processes
      - Share nothing

Mutex
- Locks resources in code

Scheduling algorithms

    First come first serve
    Prioity
    Shortsest remaing time
    Shortsest job
    Round robin
    Multilevel queue

## IPC

Inter-Process Communication

Pipes - Take output from 1 process as input for another

## Memory

Physical memory - Acctual memory (RAM)

Virtual memory - Program memory

Page tables - Links virtual to physical

Registers -> L1 cache -> L2 cache -> RAM -> HDD/SSD

------------------Time to access------------------>

MMU - Memoty Mangement Unit

```
Kernal

Stack - Grows down, local variables and function arguments          int = 0;

Memory mapping segment - Grows down, malloc(), mmap()

Heap - Grows up, A a = new A()                                      ptr = new Object();

BSS segment - Uninitialized static variabler(all zeros)             static int;

Data segment - Static variabler initialized by the programmer       static int = 1337;

Text segment (ELF) - Stores the binary image of the process         String s = "Hello";
```

## Streaming

Unicast - only send to 1

Multicast - cast to all who are intersted

Broadcast - cast to all

## DevOps

CI/CD

Continuous Integation

Build ---Auto---> Unit Tests ---Auto---> Deploy to Stage ---Auto---> Acceptance Tests

Continuous Delivery

Build ---Auto---> Unit Tests ---Auto---> Deploy to Stage ---Auto---> Acceptance Tests ---Manuel---> Deploy to Production

Continuous Deployment

Build ---Auto---> Unit Tests ---Auto---> Deploy to Stage ---Auto---> Acceptance Tests ---Autp---> Deploy to Production

## Todo

L6

L7

L8
import json
import requests_unixsocket

session = requests_unixsocket.Session()


def getDocker():
    r = session.get("http+unix://%2Fvar%2Frun%2Fdocker.sock/containers/json").json()
    
    for thing in r:
        print(thing)

if __name__ == '__main__':
    getDocker()

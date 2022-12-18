import json
import requests
import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument("--method",type=str, help='Available methods: dns, ping, http, tcp')
parser.add_argument("--host", type=str, help='IP or URL of the host to check')

args = parser.parse_args()


def dns(host):
    id_key = json.loads(requests.get(f"https://check-host.net/check-dns", params={'host': host,'max_nodes': 1}, headers={"Accept": "application/json"}).text)
    time.sleep(5)
    result_key = json.loads(requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text)
    for key in result_key:
        if type(result_key[key]) == list:
            for key2 in result_key[key][0]:
                if result_key[key][0][key2] == []:
                    print('Failed to convert domain name')
                    break   
                if key2 == 'PTR':
                    print(f"Domain name:{result_key[key][0]['PTR']}")
                if key2 == 'A':
                    print(f"Domain IP: {result_key[key][0]['A']}")
        if result_key[key] is None:
                print('Check is still going on')
 

def ping(host):
    id_key = json.loads(requests.get(f"https://check-host.net/check-ping", params={'host': host,'max_nodes': 1}, headers={"Accept": "application/json"}).text)
    time.sleep(5)
    result_key = json.loads(requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text)
    for key in result_key:
        if type(result_key[key]) == list:
            if result_key[key][0][0] is None:
                print("Failed to connect to host")
            else:
                print(f"Result: {result_key[key][0][0]}")
        if result_key[key] is None:
                print('Check is still going on')


def http(host):
    id_key = json.loads(requests.get(f"https://check-host.net/check-http", params={'host': host,'max_nodes': 1}, headers={"Accept": "application/json"}).text)
    time.sleep(5)
    result_key = json.loads(requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text)
    for key in result_key:
        if type(result_key[key]) == list:
            print(f"Status: {result_key[key][0][2:4]}")
        if result_key[key] is None:
            print("Check is still going on")  


def tcp(host):
    id_key = json.loads(requests.get(f"https://check-host.net/check-tcp", params={'host': host,'max_nodes': 1}, headers={"Accept": "application/json"}).text)
    time.sleep(5)
    result_key = json.loads(requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text)
    for key in result_key:
        if type(result_key[key]) == list:
            print(f"Connection status: {result_key[key][0]}")
        if result_key[key] is None:
            print("Check is still going on") 
            

if args.method == "dns":
    dns(args.host)

if args.method == 'ping':
    ping(args.host)   

if args.method == 'http':
    http(args.host)

if args.method == 'tcp':
    tcp(args.host)    
   
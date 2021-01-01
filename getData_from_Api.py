import time
import requests
import json
import multiprocessing

json = []
processes = []

def postDatatoFlaskApi(data):
    print(data,"edw eisai file")
    url = 'http://localhost:5000/persons'
    headers = {'Content-type': 'Application/json'} 
    for row in data:
        print(row, 'auto einai to row pou prospathw na dwsw gia post')
        res = requests.post(url, headers=headers, json=row)
        if res.ok:
            print (res)
    json.clear()


def dataCleansing(row):
    json.append(row)
    postDatatoFlaskApi(json)

def getData():
    
    start = time.perf_counter()
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for row in data:
        p = multiprocessing.Process(target=dataCleansing, args=[row]) 
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()
    
     

if __name__ == "__main__":
    for _ in range(10):
        start = time.perf_counter()
        getData()
        finish = time.perf_counter()
        print(f'The entire script finished in {round(finish-start, 2)} seconds')
        time.sleep(2)


import requests
from prometheus_client import  start_http_server, Gauge
from requests.auth import HTTPBasicAuth

    
def collect_s():
    result = requests.get('http://localhost:6610/api/builds?offset=0&count=20',auth=HTTPBasicAuth('arash', 'aghaleo1'))
    successful_builds = 0 
    for job in result.json():
        if job['status'] == "SUCCESSFUL" :
            successful_builds += 1 
    return successful_builds  
        
def collect_f():
    result = requests.get('http://localhost:6610/api/builds?offset=0&count=20',auth=HTTPBasicAuth('arash', 'aghaleo1'))
    fail_builds = 0  
    for job in result.json():
        if job['status'] == "FAILED" :
            fail_builds += 1 
    return fail_builds   
        

s = Gauge("successful_builds", "Successful builds")        
s.set_function(collect_s)
    
f = Gauge("failed_builds", "Faild builds")
f.set_function(collect_f)
    
       


if __name__ == "__main__":
  start_http_server(8000)
  while True:
    pass

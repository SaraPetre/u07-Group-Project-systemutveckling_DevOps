import requests
from prometheus_client import  start_http_server, Gauge
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

    
def collect_s():
     # Get the credentials from the environment variable using os.
    result = requests.get('http://localhost:6610/api/builds?offset=0&count=100',
    auth=HTTPBasicAuth(os.getenv("ONDEV-USER"), os.getenv("ONDEV-PASSWORD")))
    successful_builds = 0
    # print(result['status'])
    for job in result.json():
        if job['status'] == "SUCCESSFUL":
            print(job['status'])
            successful_builds += 1
    return successful_builds
        
def collect_f():
    result = requests.get('http://localhost:6610/api/builds?offset=0&count=100',
    auth=HTTPBasicAuth(os.getenv("ONDEV-USER"), os.getenv("ONDEV-PASSWORD")))
    fail_builds = 0  
    for job in result.json():
        if job['status'] == "FAILED" :
            fail_builds += 1 
    return fail_builds   
        
def collect_p():
    result = requests.get('http://localhost:6610/api/projects?offset=0&count=100',
    auth=HTTPBasicAuth(os.getenv("ONDEV-USER"), os.getenv("ONDEV-PASSWORD")))
    projects = 0
    for _ in result.json():
            projects += 1
    return projects



s = Gauge("successful_builds", "Successful builds")
s.set_function(collect_s)

f = Gauge("failed_builds", "Failed builds")
f.set_function(collect_f)
    
p = Gauge("number_of_projects", "Number of projects")      
p.set_function(collect_p)

if __name__ == "__main__":
  start_http_server(8000)
  while True:
    pass

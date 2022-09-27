# Group project part 1

# Technologies
- Jira
- Docker
- Docker-compose
- Python

## Jira
- We used Jira for a kanban work environment for this project. (https://breakingbadsjira.atlassian.net/jira/software/projects/BREAK/boards/1?issueParent=10002)

## Docker
- Alpine image

## Docker-compose
- Prometheus
- Grafana
- Selfhosted docker image registry
- OneDev

## Python
- Prometheus_client library
- Requests
- Requests.auth

# First steps
- Use following git command to clone this repo:
    git clone https://gitlab.com/lura00/groupproject_1.git
- Create a virtual environment if you like, commando:
    virtualenv venv (virtualenv <name of env>)
    To activate:
        . venv/bin/activate or source venv/bin/activate
- Install dependencies:
    pip3 install -r requirements.txt

Now you should have everything ready to start the docker/docker-compose services (concidering you have docker and docker-compose already installed on your machine)

- Start services in docker-compose:
    docker-compose up -d
    All services are hosted on http://localhost:port
        For designated ports see our docker-compose file

# Compose services

## Prometheus (https://prometheus.io)
- Go to the url for prometheus, here you'll get prompt with a login
    page. Create an account, since it is only hosted on your local machine credentials is not so important. For example you can use, username: admin, password: admin. Add your credentials and email and continue. You should now be done and prometheus should be up and running.

## Grafana (Open source, https://grafana.com/docs)
- Very much like prometheus you need to create an account. Same here
    credentials is not important. Use something easy to remember.
    Grafana should be up and running as soon this is done.

## Selfhosted registry (https://docs.docker.com/registry)
- You can go to the url, which is "http://localhost:5000", here you
    will see nothing at first. First of all, we have not pushed anyting here yet, and second to see anything att all yoy need to go to "http://localhost:5000/v2/_catalog".

    To make sure the registry works you can try to push a testimage to it:
    - Pull down a docker image, perhaps small instance of alpine and tag it with "testimage" now:
    - docker tag alpine/git localhost:5000/alpine:git
    - docker image ls | grep alpine
    - docker push localhost:5000/alpine:git
    - go back to
    - http://localhost:5000/v2/_catalog
    - Then you will get prompt with:
        {"repositories":["alpine"]}
    - "docker pull localhost:5000/testimage"

## OneDev (https://code.onedev.io)
- Go to the url, create an account, same here use easy credentials.
    Once in, create your first project, click on the big plus sign on the first page. Name it and you are done, no need for any other than default conf.
    - Once you click create you can add files. click on:
        "pushing an existing repository" and you will get the usual git commandos.
        Now push your first code. Go back to the project you cloned down:
        - git remote add onedev http://localhost:6610/your-project-name
        - git add --all
        - git commit -m "inital commit"
        - git push -u onedev master
    - A pipeline will trigger since the repo already contains a
        .onedev-buildspec.yml file. The pipeline will fail.

## OneDev CI/CD pipeline
First we need to add a "job executor":
- Go to "Administration",
https://gitlab.com/lura00/groupproject_1/-/blob/erik/images/steg1.png
- Click "Job Executors"
- Click "Add Executor"
- Click on "choose one" and add "Server Docker Executor"
- Name the executor "server-docker" and test then save.
- See pictures for visuals.

- Now your pipeline should pass and build and push a docker image to
    your selfhosted registry. To see that it did you can first of    check that the pipeline really passed
    - go to your registry and see if you have your first entry!


# Part 2

## Python script
We use prometheus_client and requests lib to scrape metrics

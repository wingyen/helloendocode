# helloendocode
***A minimal Flask app***
### Prerequirements

- Docker
- pip (optional)
- Python 3.9 (optional)

## Steps to setup the project

1. If you prefer to run the app using python venv, run the flowing command(pwd:helloendocode), if not the jump to Step 2:
```
    $ make
    $ source venv/bin/activate
    $ make run
```
2. Build and run the app using Docker, it will build an image `helloflask` 

```
    $ make build
    $ make run
```
- When the server is up and running you should be able to access http://0.0.0.0:8080

- In the logs you see logs in this format: (ISO timestamp) (host addr) (request) (response code)


## Endpoints from k8s

- http://34.107.91.63/helloworld
- http://34.107.91.63/versionz

> About Graceful Shutdown: gunicorn has timeout=25, it should give some margine for workers to shutdown and exit master before Pod termination. 
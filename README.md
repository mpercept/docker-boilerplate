# docker-boilerplate
A barebone dockerized flask REST API.


## Steps

#### Build Docker Image
```bash
docker build -t <imagename> .
```
Example:  
```bash
docker build -t testapi .
```

#### Run Image
```bash
docker run -p <host_port>:<original_port> <imagename>
```

**example**  
```bash
docker run -p 8080:8000 testapi
```
This maps the original api (running in the container) at port 8000 to 8080 in the local system.

Open browser or any client that can handle HTTP requests and try the following url:  
```bash
http://localhost:8080/test
```

#### List Docker Processes
```bash
docker ps -a
```

#### List Docker Image
```bash
docker images
```

#### Remove All Stopped Processes
remove docker process using container id
```bash
docker rm <container_id>
```

#### remove all the stopped processes
```bash
docker container prune
```

#### kill the container process running in the background
```
docker kill <container_id>

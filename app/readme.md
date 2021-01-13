HOW to RUN the container 


1. make sure all previous container instances are not running

    docker ps 
    docker ps -a 

2. kill previous instance

    docker stop containerID
    docker kill containerID

3. if you want to build a new img , delete the previous one 

    docker images 
    docker rmi imageID

4. Verify your dockerfile

5. Build your img

    docker build . -t "name of your container"

6. RUN your container 

    docker run -p 8080:5000 flask-app:latest
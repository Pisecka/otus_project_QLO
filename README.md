# Project work for booking services QLO. Made automation test on Python with a usage of docker, selenoid, pytest, allure reports.

**How to work with this repository:**
1) Run a separate container with QLO app using command:
```docker run -tidp 80:80 -p 3306:3306 -p 2222:22 --name qloappsv150 -e USER_PASSWORD=qloappsuserpassword -e MYSQL_ROOT_PASSWORD=myrootpassword -e MYSQL_DATABASE=mydatabase --network otus_project_qlo_test_net webkul/qloapps_docker:latest```.   
2) Then you can run tests on your local machine using command ```pytest```.   
3) As well you can run test on Selenoid in Docker using command ```docker-compose up -d```.  

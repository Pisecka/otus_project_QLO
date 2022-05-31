1 Сначала запускаем отдельный контейнер с QLO app
с помощью команды 
```docker run -tidp 80:80 -p 3306:3306 -p 2222:22 --name qloappsv150 -e USER_PASSWORD=qloappsuserpassword -e MYSQL_ROOT_PASSWORD=myrootpassword -e MYSQL_DATABASE=mydatabase --network otus_project_qlo_test_net webkul/qloapps_docker:latest```

2. Далее можно запустить тесты на локальной машине
3. Или запустить тесты в селеноиде
4. 
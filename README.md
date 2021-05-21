### Руководство по запуску приложения

<hr>

####Клонировать приложение из репозитория
```git colone https://github.com/iNeedNew/Singlepage.git```

```cd Singlepage\```

####Забилдить приложение
```docker-compose build```
####Запустить приложение
```docker-compose up -d```
####Настройка миграции базы данных
```docker exec flask bash run_migration.sh```
<hr>

В логе сервиса flask будет адрес на веб страницу

```docker-compose logs backend```

Адресс такого типа ```172.18.0.3:5000``` может отличаться от вашего
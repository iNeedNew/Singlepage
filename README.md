### Руководство по запуску приложения

<hr>

#### Клонировать приложение из репозитория

```git clone https://github.com/iNeedNew/Singlepage.git```

```cd Singlepage/```

#### Забилдить приложение

```docker-compose build```

#### Запустить приложение

```docker-compose up``` или ```docker-compose up -d```


#### Настройка миграции базы данных

ВАЖНО:

- Миграцию можно делать, когда в логе базы ```docker-compose logs database``` будет сообщение ```ready for connections```
в ином же случае, будет выдаваться ошибка 
```Can't connect to MySQL server on 'mysql'``` 

```docker exec flask bash run_migration.sh```

<hr>

В логе сервиса backend ```docker-compose logs backend``` будет адрес на веб страницу

Адрессы такого типа ```172.18.0.3:5000``` или ```192.168.48.3:5000``` могут отличаться от вашего

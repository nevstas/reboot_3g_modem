# Скрипт перезагрузки 3G модемов Huawei e3276s-920

Скрипт предназначен для перезагрузки (включения/выключения) модемов Huawei e3276s-920, тем самым меняя ip адрес подключения

В файле server.py указать "secret_key" и "server_port". Хотя можно оставить и по умолчанию

Запустить скрипт командой: c:\Python38\python c:\modem\server.py

Где: 

"c:\Python38\python" - это путь к python,

"c:\modem\server.py" - это путь к скрипту.

Для перезагрузки модема (смены ip адрес) перейти по адресу:

http://127.0.0.1:8080/secreturl/192.168.1.1/

Где:

"8080" - это порт, который вы указали в переменной "server_port",

"secreturl" - это секретный ключ, который вы указали в переменной "secret_key",

"192.168.1.1" - это ip модема, который перезагружаем

Скрипт подходит для мобильных прокси, настроенных по этой инструкции [https://nevep.ru/26-mobilnye-proksi-svoimi-rukami](https://nevep.ru/26-mobilnye-proksi-svoimi-rukami)

Также возмжна удаленная перезагружка модемов, для этого нужно настроить port forwarding для вашего роутера
## Rendermap - визуализируй карта своего сайта

Зависимости
```
Для работы приложения необходима версия языка Python 3.7 и выше 
```
requirements.txt
```
aiohttp==3.6.2
async-timeout==3.0.1
attrs==19.3.0
chardet==3.0.4
idna==2.9
multidict==4.7.5
pydot==1.4.1
pyparsing==2.4.6
yarl==1.4.2
```
Установка python package
```
python setup.py install
```
Настройка
```
На файле app.py изменить main_url на свой сайт 
```
Запуск приложения
```
python app.py
```
Результат будет доступно на текущий директории 
```
graph.png
```
Дополнительная информация:
```
# https://docs.python.org/3/howto/logging.html
на sitemap/__init__.py можно настроить логирование
logging.basicConfig(level=logging.DEBUG)

```

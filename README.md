# read me please

1. install docker & selenoid

- open https://aerokube.com/cm/latest/
- download resource & exec commands
- ./cm selenoid start --vnc
- ./cm selenoid start

2. выполнить команду

- docker build -t sintina1 -f Dockerfile .
- docker run -it --network selenoid sintina1 > ./mylogs.txt 2>&1

3. запустить скрипт

- pytest /путь до файла/test_collection.py --way_to_execute=selenoid
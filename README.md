# read me please

1. install docker & selenoid

- open https://github.com/aerokube/cm/releases/latest and download suitable for your system asset (section Assets).
  For example, if you're using Linux - your choose is cm_linux_amd64.
- download resource & exec commands
- ./cm selenoid start --vnc
- ./cm selenoid start

2. execute following commands

- docker build -t sintina1 -f Dockerfile .
- docker run -it --network selenoid sintina1 > ./mylogs.txt 2>&1

3. run your script using command, e.g. you have script test_collection.py:

- pytest /path yo your file/test_collection.py --way_to_execute=selenoid
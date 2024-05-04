@ECHO off
curl https://www.python.org/ftp/python/3.12.3/python-3.12.3.exe >> pythoninstall.exe
pythoninstall.exe /quiet
python -m pip install pip --user

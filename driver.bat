@echo off  
:Again  
echo 自动签到中！！！
python ./qiandao.py 
timeout /t 14400
goto Again 

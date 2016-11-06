@Echo off
cd ../
:goto

set /P devUsername="Username: "
set GAME_SERVER=68.119.63.201:6667

set TOONTOWN_LOGIN_PLAYTOKEN=%devUsername%
dependencies\panda\python\ppython __main__.py
pause
goto :goto

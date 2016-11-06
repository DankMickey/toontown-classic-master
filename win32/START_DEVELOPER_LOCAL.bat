@Echo off
cd ../
:goto

set /P devUsername="Username: "
set GAME_SERVER=127.0.0.1:6667

set TOONTOWN_LOGIN_PLAYTOKEN=%devUsername%
set WANT_DEV_INJECTOR=False
dependencies\panda\python\ppython __main__.py
pause
goto :goto

@Echo off
cd ../config/astron
:goto
astrond.exe --pretty --loglevel info astrond.yml
pause
goto :goto

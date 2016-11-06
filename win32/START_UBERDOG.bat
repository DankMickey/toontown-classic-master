@Echo off
cd ../
:goto
dependencies\panda\python\ppython -m otp.uberdog.UDStart
pause
goto :goto
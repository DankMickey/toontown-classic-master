@echo off
cd ../

:goto
dependencies\panda\python\ppython -m otp.ai.AIStart
pause
goto :goto
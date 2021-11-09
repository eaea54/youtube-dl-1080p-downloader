@echo off
For /F "tokens=1 delims= " %%i IN ('wmic product get name') do (if %%i==Python (set a=abc))
if not %a% ==abc (
python-3.7.9-amd64.exe
)

cd ./Scripts/
CALL activate
cd ..
python program.py
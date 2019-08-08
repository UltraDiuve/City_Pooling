REM Delete prd\ folder and content
rd /s /q .\prd\

REM Copy the content of docs\build\ to a brand new prd\ folder
robocopy .\docs\build\ .\prd\ /E

REM Force adding of prd\ folder to git index
REM (prd\ folder is ignore in the .gitignore file)
REM git rm -r --cached prd/
git add --force prd/
git status

pause
REM Get last version of code
git pull

REM Delete prd\ folder and content
rd /s /q .\prd\

REM Copy the content of docs\build\ to a brand new prd\ folder
robocopy .\docs\build\ .\prd\ /E

REM Force adding of prd\ folder to git index
git add --force prd/

REM Commit that addition
git commit -m "Automated deployment of prd"

REM Push this commit to remote repository
git push origin master
git status
echo off

echo Replacing prd/ folder content
echo.

REM Delete prd\ folder and content
rd /s /q .\prd\

REM Copy the content of docs\build\ to a brand new prd\ folder
robocopy .\docs\build\ .\prd\ /E

REM Unstage all changes
echo.
echo Unstaging all changes
echo.
git reset

REM Force adding of prd\ folder to git index
echo.
echo Adding prd/ folder to git index 
echo.
git add --force prd/

REM Commit that addition
echo.
echo Committing changes
echo.
git commit -m "Automated deployment of prd"

REM Push this commit to remote repository
echo.
echo Pushing to remote repository
echo.
git push origin master
git status
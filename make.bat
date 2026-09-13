@echo off
if "%1"=="html" sphinx-build -b html docs _build\html
if "%1"=="linkcheck" sphinx-build -b linkcheck docs _build\linkcheck
if "%1"=="release" python tools\build_release.py
if "%1"=="clean" rmdir /s /q _build 2>nul & rmdir /s /q release 2>nul

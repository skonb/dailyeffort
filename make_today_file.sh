#!/usr/local/bin/fish
set today (date '+%Y-%m-%d')
#python
touch {$today}.py
rm today.py
ln -s  {$today}.py today.py
code today.py
#C++
touch {$today}.c
rm today.c
ln -s  {$today}.cpp today.c
code today.c

#!/usr/local/bin/fish
set today (date '+%Y-%m-%d')
#python
touch {$today}.py
rm today.py
ln -s  {$today}.py today.py
code today.py
#C++
touch {$today}.cpp
rm today.coo
ln -s  {$today}.cpp today.cpp
code today.cpp

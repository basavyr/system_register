#!/usr/bin/env python
from app import app
from app import mega

if __name__ == '__main__':
    x = app.SayHi()
    y = mega.Reverse_Mega()
    print(f'{x}')
    print(f'{y}')

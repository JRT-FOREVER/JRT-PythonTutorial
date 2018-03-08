#!/usr/bin/env python3
#-*- coding: utf-8 -*-


items = ["right", "top", "right", "bottom", "top"]

typeMap = {
        "right": 0,
        "top": 1,
        "bottom": 2
        }

for item in items:
    print(item)

for item in items:
    print(typeMap[item])

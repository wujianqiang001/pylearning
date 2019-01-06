#!/usr/bin/env python
# coding=utf-8
module = []
with open("../configs/module.txt") as f:
    for line in f:
        if not line.startswith("#"):
            module.append(line.strip())

m = " or ".join(module)
print(m)
# -*- coding: utf-8 -*-
# Python 3

import os


def ensureDir(path):
    d = os.path.dirname(path)
    if not (os.path.exists(d)):
        os.makedirs(d)

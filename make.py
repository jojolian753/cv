#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Makefile for Sphinx documentation, adapted to python
"""


import os
from cloud_sptheme.make_helper import SphinxMaker

if __name__ == "__main__":
    SphinxMaker.BUILD = "../build"
#    SphinxMaker.SPHINXBUILD = "sphinx-build"
    SphinxMaker.PAPER = "a4"
#    SphinxMaker.SERVEHTML_PORT = 8000

    SphinxMaker.execute(root_dir=os.path.join(__file__,os.pardir))



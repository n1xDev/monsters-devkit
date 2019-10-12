# pylint: skip-file
# -*- coding: utf-8 -*-

import os, json
import consts

def getAllSubjs():
  allSubjsFile = open(consts.requiredFiles[0], "r")
  allSubjs = json.loads(allSubjsFile.read())
  return allSubjs
# pylint: skip-file
# -*- coding: utf-8 -*-

import os, json
import consts, service

def getAllSubjs():
  return service.getObjFromJsonFile(consts.requiredFiles["processedSubjectsWithPolygons"])

def getSubjsPopulation():
  return service.getObjFromJsonFile(consts.requiredFiles["processedPopulation"])

def getSubjsEducation():
  return service.getObjFromJsonFile(consts.requiredFiles["processedEducation"])
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

def getSubjsCapitals():
  return service.getObjFromJsonFile(consts.requiredFiles["processedCapitals"])

def getSubjsElections():
  return service.getObjFromJsonFile(consts.requiredFiles["processedElections"])

def getSubjsInternet():
  return service.getObjFromJsonFile(consts.requiredFiles["processedInternet"])

def getSubjsSalaries():
  return service.getObjFromJsonFile(consts.requiredFiles["processedSalaries"])
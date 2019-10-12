# pylint: skip-file
# -*- coding: utf-8 -*-

import schemas
import helpers

# Methods for getting all info
def subjects(subjects):
  allSubjects = [] # [schemas.subject(), schemas.subject()]
  for oneSubj in subjects:
    newSubj = schemas.subject()
    newSubj["name"] = helpers.getUniversalSubjName(oneSubj["name"])
    newSubj["isoName"] = oneSubj["iso"]
    newSubj["localName"] = helpers.convertLatinToCyrillic(oneSubj["name"])
    newSubj["polygons"] = oneSubj["polygons"]
    allSubjects.append(newSubj)
  return allSubjects

def subjsWithPopulation(processedSubjs, populationData):
  for index, val in enumerate(processedSubjs):
    for subIndex, subVal in enumerate(populationData):
      print(helpers.stringsSimilarity(val["name"], subVal["name"]))
      if helpers.stringsSimilarity(val["name"], subVal["name"]) > 0.009:
        print("OK: " + val["name"] + "/" + subVal["name"] + "")
        processedSubjs[index]["population"] = subVal["populationCount"]
  return processedSubjs



def subjsWithEducation(processedSubjs, education):
  pass
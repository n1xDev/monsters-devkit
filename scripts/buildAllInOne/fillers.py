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

def subjsWithPopulation(processedSubjs, population):
  for index, val in range(len(processedSubjs)):
    print(processedSubjs[index]["name"])

def subjsWithEducation(processedSubjs, education):
  pass
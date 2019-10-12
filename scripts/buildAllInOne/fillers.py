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
      # print(helpers.stringsSimilarity(val["name"], subVal["name"]))
      if helpers.stringsSimilarity(val["name"], subVal["name"]) > 0.97:
        # print("OK: " + val["name"] + "/" + subVal["name"] + "")
        processedSubjs[index]["population"] = subVal["populationCount"]
  return processedSubjs

def subjsWithEducation(processedSubjs, educationData):
  for index, val in enumerate(processedSubjs):
    for subIndex, subVal in enumerate(educationData):
      # print(helpers.stringsSimilarity(val["name"], subVal["name"]))
      if helpers.stringsSimilarity(val["name"], subVal["name"]) > 0.97:
        processedSubjs[index]["education"] = (subVal["stateUniversStudsCount"]*100)/processedSubjs[index]["population"]
  return processedSubjs

def subjsWithCapitals(processedSubjs, capitalsData):
  for index, val in enumerate(processedSubjs):
    for subIndex, subVal in enumerate(capitalsData):
      # print(helpers.stringsSimilarity(val["name"], subVal["name"]))
      if helpers.stringsSimilarity(val["name"], subVal["name"]) > 0.97:
        processedSubjs[index]["capitalCityName"] = subVal["capitalCityName"]
  return processedSubjs

def subjsWithElections(processedSubjs, electionsData):
  for index, val in enumerate(processedSubjs):
    for subIndex, subVal in enumerate(electionsData):
      # print(helpers.stringsSimilarity(val["name"], subVal["name"]))
      if helpers.stringsSimilarity(val["name"], subVal["name"]) > 0.97:
        election = schemas.election()
        election["votes"] = subVal["bulletinsCount"]
        election["votersPercentage"] = (0 if processedSubjs[index]["population"] == 0 else (subVal["bulletinsCount"]*100)/processedSubjs[index]["population"])
        election["candidates"] = subVal["candidates"]
        processedSubjs[index]["elections"].append(election)
  return processedSubjs

def subjsWithInternet(processedSubjs, internetData):
  for index, val in enumerate(processedSubjs):
    for subIndex, subVal in enumerate(internetData):
      # print(helpers.stringsSimilarity(val["name"], subVal["name"]))
      if helpers.stringsSimilarity(val["name"], subVal["name"]) > 0.97:
        processedSubjs[index]["internet"] = subVal["penetrationPercentage"]
  return processedSubjs

def subjsWithSalaries(processedSubjs, salariesData):
  for index, val in enumerate(processedSubjs):
    for subIndex, subVal in enumerate(salariesData):
      # print(helpers.stringsSimilarity(val["name"], subVal["name"]))
      if helpers.stringsSimilarity(val["name"], subVal["name"]) > 0.97:
        processedSubjs[index]["salary"] = subVal["averageSalary"]
  return processedSubjs
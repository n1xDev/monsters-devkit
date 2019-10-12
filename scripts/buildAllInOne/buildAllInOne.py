# pylint: skip-file
# -*- coding: utf-8 -*-
"""
# Build unified country subjects file with all data
"""
import json
import consts
import helpers
import schemas
import service
import fillers
import getters

def main():
  # Stage 0: checking all
  print("[i] Checking for required files...")
  service.checkForRequiredFiles(consts.requiredFiles)
  print("[i] All required files are found!")
  print("[i] STAGE 0: OK!")

  # Stage 1: get all subjects
  allSubjs = getters.getAllSubjs()
  allFilledSubjs = fillers.subjects(allSubjs)
  # print(*allFilledSubjs, sep='\n\n')
  # print("\n[i] Russian subjects count: " + str(len(allFilledSubjs)))
  print("[i] STAGE 1: OK!")

  # Stage 2: get all additional information(e.g.: population, internet, education) about subjects
  processedPopulation = getters.getSubjsPopulation()
  processedEducation = getters.getSubjsEducation()
  processedCapitals = getters.getSubjsCapitals()
  processedElections = getters.getSubjsElections()
  processedInternet = getters.getSubjsInternet()
  processedSalaries = getters.getSubjsSalaries()
  print("[i] STAGE 2: OK!")

  # Stage 3: fill all subjects(population, internet, education)
  allFilledSubjs = fillers.subjsWithPopulation(allFilledSubjs, processedPopulation)
  allFilledSubjs = fillers.subjsWithEducation(allFilledSubjs, processedEducation)
  allFilledSubjs = fillers.subjsWithCapitals(allFilledSubjs, processedCapitals)
  allFilledSubjs = fillers.subjsWithElections(allFilledSubjs, processedElections)
  allFilledSubjs = fillers.subjsWithInternet(allFilledSubjs, processedInternet)
  allFilledSubjs = fillers.subjsWithSalaries(allFilledSubjs, processedSalaries)
  print("[i] STAGE 3: OK!")

  # Stage 4: save all
  processedAllFile = open(consts.outputFilesPaths["processedAll"], "w", encoding='utf8')
  processedAllFile.write(json.dumps(allFilledSubjs, ensure_ascii=False))
  processedAllFile.close()
  print("[i] STAGE 4: OK!")

  print("[i] All done!!!")


main()
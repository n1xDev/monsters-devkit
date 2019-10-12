# pylint: skip-file
# -*- coding: utf-8 -*-
"""
# Build unified country subjects file with all data
"""
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

  # Stage 1: get all subjects
  allSubjs = getters.getAllSubjs()
  allFilledSubjs = fillers.subjects(allSubjs)
  print(*allFilledSubjs, sep='\n\n')
  print("\n[i] Russian subjects count: " + str(len(allFilledSubjs)))

  # Stage 2: get all additional information(e.g.: population, internet, education) about subjects
  processedPopulation = getters.getSubjsPopulation()

  # Stage 3: fill all subjects(population, internet, education)


main()
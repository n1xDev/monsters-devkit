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

  # Stage 1: get only all subjects
  allSubjs = getters.getAllSubjs()
  allFilledSubjs = fillers.subjects(allSubjs)
  print(allFilledSubjs)

main()
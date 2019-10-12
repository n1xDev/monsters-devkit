# pylint: skip-file
# -*- coding: utf-8 -*-

import schemas
import helpers

# Methods for getting all info
def subjects(subjects):
  allSubjects = [] # [schemas.subject(), schemas.subject()]
  for oneSubj in subjects:
    newSubj = schemas.subject()
    newSubj["name"] = helpers.getUniversalSubjName(newSubj["name"])
    newSubj["localName"] = helpers.convertLatinToCyrillic(oneSubj["name"])
    allSubjects.append(newSubj)

  return allSubjects
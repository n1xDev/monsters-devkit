import os, json, codecs

# Service methods
def criticalExit(reasonMsg):
  # TODO: Log this problem to file
  exit(reasonMsg)

def checkForRequiredFiles(requiredFilesList):
  for key in requiredFilesList:
    if not os.path.isfile(requiredFilesList[key]):
      criticalExit("[!] checkForRequiredFiles() " + requiredFilesList[key] + " is not found!!!")
    else:
      if os.path.getsize(requiredFilesList[key]) < 8:
        criticalExit("[!] checkForRequiredFiles() " + requiredFilesList[key] + " is almost empty!!!")

def getObjFromJsonFile(filePath):
  jsonFile = codecs.open(filePath, "r", "utf_8_sig")
  obj = json.loads(jsonFile.read())
  return obj
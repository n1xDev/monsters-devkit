import os, json

# Service methods
def criticalExit(reasonMsg):
  # TODO: Log this problem to file
  exit(reasonMsg)

def checkForRequiredFiles(requiredFilesList):
  for oneRequiredFile in requiredFilesList:
    if not os.path.isfile(oneRequiredFile):
      criticalExit("[!] checkForRequiredFiles() " + oneRequiredFile + " is not found!!!")
    else:
      if os.path.getsize(oneRequiredFile) < 8:
        criticalExit("[!] checkForRequiredFiles() " + oneRequiredFile + " is almost empty!!!")
import json, codecs

srcRawFilePath = "C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\rawData\\salary\\salariesCreditsOther.csv"
outputFilePath = "C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\processedData\\processedSalaries.json"

allSubjsData = []
srcRawFile = codecs.open(srcRawFilePath, "r", "utf_8_sig")
srcRawFileContentLines = srcRawFile.readlines()

def isSubjAlreadyExists(subjName):
  for oneSubjData in allSubjsData:
    if oneSubjData["name"] == subjName:
      return True
  return False

for oneContentLine in srcRawFileContentLines:
  if "Средняя зарплата" not in oneContentLine:
    continue
  if "Россия" in oneContentLine:
    continue
  
  splittedLine = oneContentLine.split(",")
  if "2018-10" in oneContentLine:
    if not isSubjAlreadyExists(splittedLine[1]):
      allSubjsData.append({
        "name": splittedLine[1],
        "date": splittedLine[2],
        "averageSalary": int(splittedLine[3])
      })
  else:
    if "2018-11" in oneContentLine or "2018-03" in oneContentLine or "2018-12" in oneContentLine:
      if not isSubjAlreadyExists(splittedLine[1]):
        allSubjsData.append({
          "name": splittedLine[1],
          "date": splittedLine[2],
          "averageSalary": int(splittedLine[3])
        })

#print(*allSubjsData, sep="\n\n")
allSubjsDataJsonStr = json.dumps(allSubjsData, ensure_ascii=False)
outputFile = open(outputFilePath, "w", encoding='utf8')
outputFile.write(str(allSubjsDataJsonStr))
outputFile.close()

print("All done!")
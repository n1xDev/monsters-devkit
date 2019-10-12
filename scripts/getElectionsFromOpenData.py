import json, codecs

srcRawFilePath = "C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\rawData\\elections\\elections.json"
outputFilePath = "C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\processedData\\processedElections.json"

allSubjsData = []
srcRawFile = codecs.open(srcRawFilePath, "r", "utf_8_sig")
srcRawFileContent = srcRawFile.read()
elections = json.loads(srcRawFileContent)["election"]["district"]

for oneElection in elections:
  candidates = []
  bulletinsCount = 0
  for oneResultLine in oneElection["result"]:
    if "Число действительных избирательных бюллетеней" in oneResultLine["name"]:
      bulletinsCount = oneResultLine["quantity"]
    if "quantity_percent" in oneResultLine:
      candidates.append(oneResultLine)
  # if len(candidates) != 8:
  #   exit("Incorrect candidates count!")
  allSubjsData.append({
    "name": oneElection["name"],
    "bulletinsCount": int(bulletinsCount),
    "candidates": candidates
  })

#print(*allSubjsData, sep="\n\n")
allSubjsDataJsonStr = json.dumps(allSubjsData, ensure_ascii=False)
outputFile = open(outputFilePath, "w", encoding='utf8')
outputFile.write(str(allSubjsDataJsonStr))
outputFile.close()

print("All done!")
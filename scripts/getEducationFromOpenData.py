import json, codecs

"""
Raw file structure:
field name,english description,russian description,format
"countstudentgos","Quantity of students in state educational organizations (OKEI)","Количество студентов, обучающихся в государственных вузах и в филиалах, человек (согласно классификатору ОКЕИ)","integer"
"countstudentnegos","Quantity of students in private educational organizations (OKEI)","Количество студентов, обучающихся в негосударственных вузах и в филиалах, человек (согласно классификатору ОКЕИ)","integer"
"countteachergos","Quantity of teachers in state educational organizations (OKEI)","Численность профессорско- преподавательского состава в государственных вузах и в филиалах, человек (согласно классификатору ОКЕИ)","integer"
"countteachernegos","Quantity of teachers in private educational organizations (OKEI)","Численность профессорско- преподавательского состава в негосударственных вузах и в филиалах, человек (согласно классификатору ОКЕИ)","integer"
"obrgos","Quantity of state higher educational organizations (OKEI)","Число государственных образовательных учреждений высшего образования Российской Федерации и филиалов, единиц (согласно классификатору ОКЕИ)","integer"
"obrnegos","Quantity of private higher educational organizations (OKEI)","Число негосударственных образовательных учреждений высшего образования Российской Федерации и филиалов, единиц (согласно классификатору ОКЕИ)","integer"
"subject","Subject of the Russian Federation (SSRF)","Субъект Российской Федерации (согласно справочнику ССРФ)","region"
"""
srcRawFilePath = "C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\rawData\\education\\education.csv"
outputFilePath = "C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\processedData\\processedEducation.json"

allSubjsData = []
srcRawFile = codecs.open(srcRawFilePath, "r", "utf_8_sig")
srcRawFileContentLines = srcRawFile.readlines()
for oneContentLine in srcRawFileContentLines:
  if "subject" in oneContentLine:
    continue
  splittedLine = oneContentLine.split(",")
  for key in range(len(splittedLine)):
    if splittedLine[key].replace('"', '').replace('\n', '') == '' or splittedLine[key].replace('"', '').replace('\n', '') == ' ':
      if key != 6:
        splittedLine[key] = '0'
  allSubjsData.append({
    "name": splittedLine[6].replace('"', '').replace('\n', ''),
    "stateUniversStudsCount": int(splittedLine[0].replace('"', '')),
    "privateUniversStudsCount": int(splittedLine[1].replace('"', '')),
    "stateUniversProfessorCount": int(splittedLine[2].replace('"', '')),
    "privateUniversProfessorCount": int(splittedLine[3].replace('"', '')),
    "stateUniversCount": int(splittedLine[4].replace('"', '')),
    "privateUniversCount": int(splittedLine[5].replace('"', ''))
  })

#print(*allSubjsData, sep="\n\n")
allSubjsDataJsonStr = json.dumps(allSubjsData, ensure_ascii=False)
outputFile = open(outputFilePath, "w", encoding='utf8')
outputFile.write(str(allSubjsDataJsonStr))
outputFile.close()

print("All done!")
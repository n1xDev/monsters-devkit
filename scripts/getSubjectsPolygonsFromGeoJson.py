# Warning: GeoJson need to be prepared by frontend logic

import json

gjSrcFilePath = "C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\raw-data\\subjects\\subjectsGeoJson.json"
gjSrcFile = open(gjSrcFilePath, "r")
gjData = json.loads(gjSrcFile.read())

allSubjectsObj = {}
allSubjectsArr = []
stupidMoments = []
for oneFeature in gjData["features"]:
  if oneFeature["properties"]["NAME_1"] not in allSubjectsObj:
    allSubjectsObj[oneFeature["properties"]["NAME_1"]] = {
      "name": oneFeature["properties"]["NAME_1"],
      "hasc": oneFeature["properties"]["HASC_1"],
      "iso": oneFeature["properties"]["ISO_2"],
      "internet": 0.5,
      "education": 0.5,
      "polygons": []
    }
  
  for oneCoordinateArr in oneFeature["geometry"]["coordinates"]:
    allSubjectsObj[oneFeature["properties"]["NAME_1"]]["polygons"].append(oneCoordinateArr)

  # print("=============================")
  # print(str(oneFeature["properties"]["NAME_1"]))
  # print(str(len(oneFeature["geometry"]["coordinates"])))
  # print(str(len(oneFeature["geometry"]["coordinates"][0])))
  # if len(oneFeature["geometry"]["coordinates"]) > 1:
  #   stupidMoments.append({
  #     "Name": oneFeature["properties"]["NAME_1"],
  #     "Count": len(oneFeature["geometry"]["coordinates"]),
  #     "Data": oneFeature["geometry"]["coordinates"]
  #   })
  # print("=============================")
#print(stupidMoments)

for key in allSubjectsObj:
  allSubjectsArr.append(allSubjectsObj[key])

allSubjectsArrJsonStr = json.dumps(allSubjectsArr)
allSubjectsFile = open("C:\\dev\\contests\\hackathons\\111019_nastachku_gamedev\\monsters-devkit\\processed-data\\processedSubjectsWithPolygons.json", "w")
allSubjectsFile.write(allSubjectsArrJsonStr)

print("All done!")
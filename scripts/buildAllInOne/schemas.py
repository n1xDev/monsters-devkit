# Schemas
def subject():
  schema = {
    "name": "",
    "isoName": "",
    "localName": "",
    "polygons": [],
    "population": 0,
    "salary": 0,
    "internet": 0.0,
    "education": 0.0,
    "massMedia": 0.0,
    "elections": [
      # electionSchema()
    ],
    "meetings": [
      # meetingSchema()
    ]
  }
  return schema

def election():
  schema = {
    "votes": 0, # Votes count in this subject
    "votersPercentage": 0 # Percentage of Voters
  }
  return schema

def meeting():
  schema = {
    "city": "",
    "startedAt": 0, # Meeting start time
    "endAt": 0, # Meeting end time
    "isAgreed": False,
    "isContinues": False,
    "protestersCount": 0, # Number of meetings participants
    "effectPercentage": 0 # Influence
  }
  return schema
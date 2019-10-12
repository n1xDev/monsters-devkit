import re

# Help methods
def isSubjNameSame(firstSubjName, secondSubjName):
  return True

def getUniversalSubjName(currName):
  return ""

def isTextContainsCyrillic(text):
  return bool(re.search('[а-яА-Я]', text))

def isTextContainsLatin(text):
  return bool(re.search('[a-zA-Z]', text))

def convertCyrillicToLatin(text):
  if not isTextContainsCyrillic(text):
    return text
  symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
  tr = dict( [ (ord(a), ord(b)) for (a, b) in zip(*symbols) ] )
  return text.translate(tr)

def convertLatinToCyrillic(text):
  if not isTextContainsLatin(text):
    return text
  symbols = (u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA", u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
  tr = dict( [ (ord(a), ord(b)) for (a, b) in zip(*symbols) ] )
  return text.translate(tr)
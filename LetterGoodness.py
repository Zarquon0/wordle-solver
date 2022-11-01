def letterGoodinate(wordList):
  letterDict = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
  } 
  for word in wordList:
    for i in range(0,len(word)):
      letterDict[word[i]]+=1
  t=chr(98)
  for i in range(97,97+len(letterDict)-1):
    ii = chr(i)
    if letterDict[ii]>=letterDict[t]:
      t = ii
    else:
      t = t
  a = letterDict[t]
  for term in letterDict:
    letterDict[term] /= a
  return letterDict

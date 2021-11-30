text = input("Ievadi tekstu: ")
if text.count("e")>0:
  text = text.replace("e", " ")
  text = text.upper()
  print("Teksts: ", text)
else:
  d = "TEKSTS NESATUR VAJADZĪGO BURTU."
  print(d)
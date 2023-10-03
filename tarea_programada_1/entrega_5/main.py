import analyzer

if __name__ == "__main__":
  output = []
  output = analyzer.analyze("vpn-logs-2020-modified-abb-revMM.txt")
  for i in range(len(output)):
    print(output[i])
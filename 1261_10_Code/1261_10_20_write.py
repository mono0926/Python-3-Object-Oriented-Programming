contents = "an oft-repeated cliché"
file = open("filename", "w", encoding="ascii", errors="replace")
file.write(contents)
file.close()

import libcsv

options = libcsv.openTable("./testcsvfile.csv")
print(options)

print(libcsv.writeTable("./username.csv", options))

options = libcsv.openTable("./username.csv")
print(options)

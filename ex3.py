import zipfile
import sys
import re

print sys.argv
with zipfile.ZipFile(sys.argv[1], "r") as postalzip:
    filelist = postalzip.namelist()
    with postalzip.open(filelist[0], "r") as csvfile:
        alllines = csvfile.readlines()
# 3 setup
dic_by_zips = {}
for l in alllines:
    l = l.strip()
    zip_code = l.split(",")[0]
    dic_by_zips[zip_code] = l

# 3
print dic_by_zips['"6830031"']

# 4
for i in range(9):
    key = '"' + str(i) * 7 + '"'
    if key in dic_by_zips:
        print dic_by_zips[key]
    else:
        print key + " 0 record."
# 5 indexing
print [ dic_by_zips[key] for key in dic_by_zips.keys() if key[-4:-1] == "128"]
# 5 regular expression
print [ dic_by_zips[key] for key in dic_by_zips.keys() if re.search('128"$',key) ]

# 6,7  setup
dic_by_towns = {}

for l in alllines:
    l = l.strip()
    values = l.split(",")
    key = values[4] + values[5] + values[6]
    dic_by_towns[key] = l

## 6. find method
print [ dic_by_towns[key] for key in dic_by_towns.keys() if key.find("SHIGA KEN") >= 0 and key.find("KUSATSU SHI") >= 0 ]

## 6. regular expression
##print [ dic_by_towns[key] for key in dic_by_towns.keys() if re.search("SHIGA KEN.*KUSATSU SHI", key) ]

results = [ dic_by_towns[key] for key in dic_by_towns.keys() if key.find("FUJIMI") >= 0 ]
print len( [ l for l in results if l.find("SHIZUOKA KEN") >= 0 ] )
print len( [ l for l in results if l.find("SHIZUOKA KEN") == -1] )
print len( results )

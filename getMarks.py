import requests
import re
import csv

# converts marks to grade points 
def point(a):
	if (a < 50):
		return 0 if a < 40 else int((a - 5) / 10 + 1)
	return min(int(a / 10 + 1), 10)

allMarks = []
rangeEnd = 198
url = 'http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php'

for itr in range(1, rangeEnd):
  usn = '1cr15cs' + ('0' * (3 - len(str(itr)))) + str(itr)
  values = { 'lns' : usn }
  r = requests.post(url, data = values)
  htm = r.text
  
  # checks if student appeared for 5 sememster exams and then extracts name and marks
  if (re.search(r'Semester : 5', htm)):
    name = re.search(r"Student Name.*\n.*:</b>(.*)</td>", htm)
    marks = re.findall(r'Cell">([\w]*)</div>', htm)
    
    sub, lab = 0, 0
    for j, i in enumerate(range(5, 41, 5)):
      if j < 6:
        sub += point(int(marks[i]))
      else:
        lab += point(int(marks[i]))
    gpa = ((sub * 4.0) + (lab * 2.0)) / 28.0
    allMarks.append(tuple((usn, name.group(1).strip(), str(gpa))))

# sorts list by gpa in decending order
allMarks.sort(key = lambda x : x[2], reverse = True)

with open('CSEmarks.csv', 'wb') as filePtr:
  csvWriter = csv.writer(filePtr)
  for i in range(len(allMarks)):
    csvWriter.writerows([allMarks[i]])

# Syntax changes for Python 3
# with open('CSEmarks.csv', 'w', newline = '') as filePtr:

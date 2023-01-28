import os
import re

INDEX = 'index.html'

if os.path.exists(INDEX):
    os.remove(INDEX)

with open(INDEX, 'a') as outStream:
    outStream.write("<!DOCTYPE html>\n")
    outStream.write("<html>\n")
    outStream.write("<head>\n")
    outStream.write('<link rel="stylesheet" href="style.css">\n')
    outStream.write("</head>\n")
    outStream.write("<body>\n")
    outStream.write("<pre>\n")

    outStream.write(f'<h2>Useful Resources</h2>\n')
    outStream.write(f"<a href='https://www.w3schools.com/python'>W3 Schools Python Tutorial</a>\n")
    outStream.write(f"<a href='https://www.w3schools.com/python/python_quiz.asp'>W3 Schools Python Quiz</a>\n")
    outStream.write(f"<a href='https://www.w3schools.com/python/python_exercises.asp'>W3 Schools Python Exercises</a>\n")
    outStream.write(f"<a href='https://docs.python.org/3.11'>Python 3.11.1 documentation</a>\n")

    outStream.write(f'<div>&nbsp;</div>\n')
    outStream.write(f'<h2>Exercises</h2>\n')

    for root, dirs, files in os.walk('.'):
        print(f"{root}:{dirs}:{files}")

        if re.search('^\\.\\\\[0-9][0-9]', root) is not None:

            dirName = root.removeprefix('.\\').replace("_", " ")

            outStream.write(f'<h3>{dirName}</h3>\n')

            for file in files:
                filePath = os.path.join(root, file)

                print(filePath)

                outStream.write(f"<a href='{filePath}'>{file.replace('.html', '')}</a>\n")

    outStream.write("</body>\n")
    outStream.write("</html>\n")



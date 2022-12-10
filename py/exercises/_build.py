import os
import re

INDEX = 'index.html'

if os.path.exists(INDEX):
    os.remove(INDEX)

with open(INDEX, 'a') as outStream:
    for root, dirs, files in os.walk('.'):
        # print(f"{root}:{dirs}:{files}")

        if re.search('[0-9][0-9]$', root) is not None:

            dirName = root.removeprefix('.\\')

            outStream.write(f'<h3>{dirName}</h3>\n')

            for file in files:
                filePath = os.path.join(root, file)
                print(filePath)

                outStream.write(f"<div><a href='{filePath}'>{file.replace('.html', '')}</a></div>\n")



import os

file_path = r'D:\myownproject\python_study\os\获得路径和文件名.py'
(filepath,tempfilename) = os.path.split(file_path)
(filename,extension) = os.path.splitext(tempfilename)

print(filepath)
print(tempfilename)
print(extension[1:])

"""
output:
D:\myownproject\python_study\os
获得路径和文件名.py
.py
"""
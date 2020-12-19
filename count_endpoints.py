import glob
import os
import re

file_path = glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/APIs/*/**/client.py', recursive=True)
count = 0

for file in file_path:
    with open(file, 'r') as f:
        for line in f:
            if "  def " in line:
                # print(re.findall("def (.*)\(", line)[0].upper())  # Print all APIs
                count += 1
        f.close()

print(f'{"=" * 25}\n  Total endpoints = {count} \n{"=" * 25}')

"""
====================================================================
Linux/UNIX command
1) cd PRICE/APIs
2) find -mindepth 2 -name 'client.py' | xargs grep " return " | wc -l
3) find -mindepth 2 -name 'client.py' | xargs grep "def " | grep -o -P '(?<=def).*(?=\()'
====================================================================
"""

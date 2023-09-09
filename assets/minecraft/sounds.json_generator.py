"""
sounds.json generator
---------------------
Paste the full file path into the program input, and the sounds.json file
will be generated for you!
"""

import os
import sys

print("=================================")
print("sounds.json generator by Bentroen")
print("=================================\n")

if sys.version_info[0] < 3:
    raise Exception("This script requires Python 3.")

while True:
    path = input("Please enter path to 'sounds' folder: ")
    if not os.path.isdir(path):
        print("ERROR: Invalid path name provided.\n")
        continue
    else:
        if not os.path.basename(path).strip() == "sounds":
            print("ERROR: The provided path does not point to a 'sounds' folder.\n")
            continue
        else:
            break

FILE_COUNT = 0
sounds = []

for directory, subdirs, files in os.walk(path):
    for f in files:
        FILE_COUNT += 1
        if f[-4:] == ".ogg":
            # Replace the \ in file path with . (e.g., minecart\base > minecart.base)
            file_name = os.path.join(directory[(len(directory)-len(path)-1)*-1:], f[:-4]).replace("\\", ".")
            sounds.append(file_name)
        if FILE_COUNT >= 1500:
            raise Exception("File count exceeded safe limit.")

json_path = os.path.join(os.path.split(path)[0], "sounds.json")
json = open(json_path, 'w', encoding='utf-8')
json.write("{")

LAST_PREFIX = ""
FIRST_EVENT = True

for i,f in enumerate(sounds):
    print(f"Processing file {i+1}/{len(sounds)}: {f}")
    prefix = f

    if not LAST_PREFIX == prefix:
        # If first file, exclude the closing brackets, else include
        if not FIRST_EVENT:
            json.write('\n\t\t]')
            json.write('\n\t},')
        FIRST_EVENT = False
        # Sound name (e.g., minecart.base)
        json.write(f'\n\t"{prefix}\": {{')
        json.write('\n\t\t"sounds": [')
    else:
        json.write(',')
    # Sound file path. Replace the . with / (e.g., minecart.base > minecart/base)
    json.write(f'\n\t\t\t"{f.replace(".", "/")}"')
    LAST_PREFIX = prefix

# Close last sound file
json.write('\n\t\t]')
json.write('\n\t}')
json.write('\n}')
json.close()

print(f"\n{len(sounds)} files generated.")
os.system("pause")

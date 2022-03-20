import os
import re


path = "./sounds"

file_count = 0
sounds = []

for dir, subdirs, files in os.walk(path):
  print(dir, files)
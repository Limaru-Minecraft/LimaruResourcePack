import os

path = input('Path to .wav files: ')

# list and remove
dirlist = [i for i in os.listdir(path) if i.startswith('0')]
dirlist.sort()

# Create a tree of all files
new_names = []
for f in range(1, len(dirlist)+1, 2):
  filename = dirlist[f]
  station_name = filename.split("_")[2].split("に到着")[0]
  new_names.append("次_"+station_name)
  new_names.append("今_"+station_name)

for f in range(len(dirlist)):
  os.system('ffmpeg -i {0}/{1} -acodec libvorbis -filter_complex "[0:a][0:a]amerge=inputs=2[a]" -map "[a]" {0}/{2}.ogg'.format(path, dirlist[f], new_names[f]))

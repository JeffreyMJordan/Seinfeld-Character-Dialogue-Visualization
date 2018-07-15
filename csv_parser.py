import csv 
import json
# This program parses ./seinfeld-chronicles/scripts.csv into a JSON array of objects representing each episode 
# Each episode object has keys for each character mapped to the number of lines they've spoken 
episode_obj = {}
main_characters = {'ELAINE': True, 'JERRY': True, 'GEORGE': True, 'KRAMER': True, 'NEWMAN': True}
arr = []
episode_list = {}
with open('./seinfeld-chronicles/scripts.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    for row in spamreader:
      episode = row[4]
      word_count = len(row[2].split(" "))
      character = row[1]
      if not episode_list.get(episode):
        episode_list[episode] = True
        arr.append(episode_obj)
        episode_obj = {'TITLE': episode}
        for name in main_characters.keys():
          episode_obj[name] = 0
      if(main_characters.get(character)):
        episode_obj[character] += word_count
     

with open('data.json', 'w') as outfile:
    json.dump(arr[2:], outfile)
      
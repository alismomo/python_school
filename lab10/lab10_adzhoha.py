##Word count based on a txt file, and exception handling. Alisa Dzhoha. This program takes an input from the user, which is supposed to be a txt file. 
# If the file exists, then the program counts the frequency with which the word appeared in the file.Otherwise, it will tell the user that an error occurred. 
# 11/01/2025
from pathlib import Path

#The file name is kafka_metamorphosis.txt
def main():
  file_name = input('Please enter file name: ')
  file_path = Path.cwd() / 'lab10' / file_name
  try:
    contents = open(file_path, 'r')
  except(TypeError, FileNotFoundError, FileExistsError) as e:
    print(f'Sorry, an error occured: {e}')
    return
  else:
    freq_data = wordFreq(contents)
    printOut(freq_data)
  contents.close()

def wordFreq(contents):
  freq = {}
  line = contents.readline()
  punctChars = ('.', ',', '[', ']', '|', ':', ';', '\"', '\'', '?', '!', '*', '-', '(', ')',
    '“', '”', '‘', '•', '-', '—', '…', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '$', '#', '%')
  while line:
    for c in punctChars:
      line = line.replace(c, '')
    
    words = line.split()

    for word in words:
      tmp = word.lower()
      freq[tmp] = freq.get(tmp, 0) + 1

    line = contents.readline()
  return freq

def printOut(freq_data):
  for word, count in sorted(freq_data.items()):
    print(f'{word} :: {count} \n')


if __name__ == "__main__":
    main()
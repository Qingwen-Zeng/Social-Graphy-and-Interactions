import os

# Path to the directory containing singer text files (update this path as needed)
directory_path = 'wiki_pages'

# Extracting file names from the directory (without extensions)
files_in_directory = [os.path.splitext(file)[0] for file in os.listdir(directory_path)]

# Reading the uploaded 'genres.txt' to extract singer names
with open('genres.txt', 'r', encoding='utf-8') as f:
    genres_data = f.read()

# Extracting singer names from the 'genres.txt' file
singer_names_in_genres = [line.split(":")[0].strip('{"} ') for line in genres_data.split("\n") if line]

# Finding singers that are in 'genres.txt' but not in the directory
missing_singers = [singer for singer in singer_names_in_genres if singer not in files_in_directory]

print(missing_singers)

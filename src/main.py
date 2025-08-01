import os
import json
import shutil

dir_name = os.path.dirname(__file__)
in_path = os.path.join(dir_name, "in")
out_path = os.path.join(dir_name, "out")

font_name_file = os.path.join(dir_name, "font-names.json")

fonts = []

# If input and output dirs don't exist, please create them
if not os.path.exists(in_path):
    os.makedirs(in_path)

if not os.path.exists(out_path):
    os.makedirs(out_path)

# Read the contents of the json file with font names
with open(font_name_file) as names_file:
    contents = json.loads(names_file.read())
    fonts = contents["fonts"]

# Create the new files with the fonts
for font_file in os.listdir(in_path):
    out_font_path = os.path.join(out_path, font_file.replace(".ttf", ""))
    out_font_file_path = os.path.join(out_font_path, font_file)
    in_font_file_path = os.path.join(in_path, font_file)

    # Delete contents if already ran with font
    if os.path.exists(out_font_path):
        shutil.rmtree(out_font_path)
    os.makedirs(out_font_path)

    for font in fonts:
        shutil.copy(in_font_file_path, out_font_path)
        os.rename(out_font_file_path, os.path.join(out_font_path, font))
# Source - https://stackoverflow.com/a/3207973
# Posted by pycruft, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-12, License - CC BY-SA 4.0

from os import listdir
from os.path import isfile, join

icon_path = "images/item_icons"

file_list = [join(icon_path, f) for f in listdir(icon_path) if isfile(join(icon_path, f))]

#jumble them up

from random import shuffle

shuffle(file_list)

# Now to write the text to a external file...

final_txt = f"[\"{"\",\"".join(file_list)}\"];"

final_txt = final_txt.replace("\\", "/")

with open("tools/images_names.txt", "w") as txt_file:
    txt_file.write(final_txt)
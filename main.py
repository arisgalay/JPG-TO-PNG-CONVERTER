from pathlib import Path, PurePath
from PIL import Image

p = Path('.')
my_folder = p / 'JPG'
out_folder = p / 'PNG'

if not Path(out_folder).exists():
    Path(out_folder).mkdir()

for filename in my_folder.iterdir():
    img = Image.open(filename)
    clean_name = PurePath(filename).name
    img.thumbnail((400, 400))
    img.save(f'{out_folder}/{clean_name[:-4]}.png', 'png')
    print(f'{clean_name[:-4]}.png : Completed')

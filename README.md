# VISOR
This repository is to visualize VISOR dataset by having the JSON files from VISOR website: (https://epic-kitchens.github.io/VISOR)


## How to use
The visualization script vis.py could be used with the following arguments:

`input_directory`: a path to JSON files you want to visualizse there
`output_directory`: a path where the output masks/overlay would be generated.
`is_overlay`: this flag determain if you want to generate masks (is_overlay=False) only or overlaid images (is_overlay=True). Default is False.
`images_root_directory` (optional): a path where VISOR images are in case you want to visualize the output as overlaid images.
`output_resolution`: output resolution of the generated masks/overlaid images. Default is Full HD (1920x1080)

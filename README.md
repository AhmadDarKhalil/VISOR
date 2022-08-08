# VISOR
This repository is to visualize VISOR dataset (both sparse and dense) by having the JSON files from VISOR website: (https://epic-kitchens.github.io/VISOR)


## How to use
Open `demo.py` script and edit the paths with yout local paths. `demo.py` script will call `folder_of_jsons_to_masks` function from vis.py the function support has those arguments:

`input_directory`: a path to JSON files you want to visualizse.<br />
`output_directory`: a path where the output masks/overlay would be generated.<br />
`is_overlay` (optional): this flag determain if you want to generate masks (is_overlay=False) only or overlaid images (is_overlay=True). Default is False.<br />
`images_root_directory` (optional): a path where VISOR images are in case you want to visualize the output as overlaid images.<br />
`output_resolution` (optional): output resolution of the generated masks/overlaid images. Default is Full HD (1920x1080)<br />
`generate_video` (optional): whthear you want to create videos from the output images. Default is True

After identifying all arguments, just run `python demo.py` and you should get the visualizations in your `output_directory`.

You'll also get a `data_mapping.csv` file in the `output_directory`, this file maps each colour in the PNG images into the object name.


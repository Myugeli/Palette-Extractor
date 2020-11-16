# Palette-Extractor
This program will make a palette image from an input image, and then save it. 

To use compiled executable: Make sure you have both RAR volumes, Part1 and Part2, then extract with WinRAR.

Algorithm used is: Resize picture to [user specified, default 50x50, unless input is smaller] -> Convert to 0-255 RGB space -> 
Round each pixel colour value to nearest [user specified, default 35] -> Pull all unique colour values and put them in a list -> 
Check each colour value in that list for distance in RGB space from each other, removing ones that are closer than [user specified, default 110] -> 
Finally, generate palette image with the resulting list of colours.

Instructions: 
Step 1: Enter target image filepath. Click 'Set Target' to make sure you have the right one. Please make sure the application and the input image are in the same folder.
Step 2: Enter resize value. The larger this is, the more colours there will be in the palette, but it will take more time to process.
Step 3: Enter rounding value. This controls colour variation. The larger this is, the less colours there will be in the palette.
Step 4: Enter tuning value. This controls how close together the palette colours will be. The larger this is, the less colours there will be in the palette.
Step 5: Click 'Preview' to preview to palette. The number of colours in it will also be displayed.
Step 6: Enter palette filename and click 'Save Palette'. The palette will be saved to the folder the application is in.

#!/usr/bin/env python

import os

# Please write your screenshot dir with full path. Later, I'll improve this.
screenshot_dir   = "/home/anggiramadyansyah/Gambar/Screenshoot"
os.chdir(screenshot_dir)
ss_dir           = os.getcwd()
list_file        = os.popen("ls -p | grep -v /").read().split("\n")[:-1]
original_file    = list_file[-1]
target           = list(original_file)
target.insert(-4, 'X')
target_file      = ''.join(target)
color_profile    = "/usr/share/color/icc/colord/sRGB.icc"
color_fg         = "#ffffff"
color_bg         = "#212B30"
border_size      = "2"
background_color = "white"
background_size  = "15"
shadow_size      = "50x10+0+10"
font             = "Iosevka"
font_size        = "11"
color_fg         = "#ffffff"
color_bg         = "#212B30"
author_position  = ["NorthEast", "+60+16"]
author           = "Shooter: @" + \
                   os.popen("echo $USER").read().rstrip("\n")

os.system(f"""
convert {original_file} -bordercolor '{color_bg}' -border {border_size} \
{target_file}

convert {target_file} \\( +clone -background black \
-shadow {shadow_size} \\) +swap -background none \
-layers merge +repage {target_file}; \

convert {target_file} -bordercolor {background_color} \
-border {background_size} {target_file}

echo -n " {author} " | convert {target_file} \
-gravity {author_position[0]} -pointsize {font_size} -fill '{color_fg}' \
-undercolor '{color_bg}' -font {font} \
-annotate {author_position[1]} @- {target_file}

convert {target_file} -gravity South -chop 0x{int(background_size)/2} \
{target_file}

convert {target_file} -gravity North -background {background_color} \
-splice 0x{int(background_size)/2} {target_file}

convert {target_file} -profile {color_profile} {target_file}
""")

if os.system("which optipng > /dev/null 2>&1"):
    os.system(f"optipng {target_file}")
    print("OPTIPNG DONE!")

print(f"""SS_DIR: {ss_dir}
SOURCE: {original_file}
TARGET: {target_file}
FRAMING SUCCESS!""")

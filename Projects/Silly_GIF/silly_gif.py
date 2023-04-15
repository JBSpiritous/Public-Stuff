import os
from moviepy.editor import *

# Set up font and message
font_path = "Caveat-Bold.ttf"
font_size = 50
font_color = "white"
message = "You are amazingly silly"

# Set up background color and size
bg_color = "black"
width, height = 500, 500

# Set up duration and number of repetitions
duration = 30
n_repetitions = duration // 3

# Set up path to ImageMagick convert binary
imagemagick_path = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe"
ffmpeg_binary = r"C:\ffmpeg\bin\ffmpeg.exe"

# Create the text clip
text_clip = TextClip(message, fontsize=font_size, font=font_path, color=font_color)

# Set the duration of the text clip
text_clip = text_clip.set_duration(duration)

# Animate the text clip
animation = (text_clip.set_position("center")
                       .fadein(2)
                       .fadeout(2))

for i in range(n_repetitions):
    animation = animation.to_ImageClip(1).set_duration(1)
    animation.write_videofile(filename="temp.mp4", fps=15, codec="libx264", ffmpeg_params=["-pix_fmt", "yuv420p", "-preset", "medium", "-b:v", "1000k", "-b:a", "192k"])
    animation = VideoFileClip("temp.mp4", ffmpeg_binary=ffmpeg_binary)

# Create the background clip
bg_clip = ColorClip(size=(width, height), color=bg_color)

# Combine the animation and background clips
final_clip = CompositeVideoClip([bg_clip, animation])

# Set the path to where the GIF will be saved
gif_path = os.path.join(r"C:\Code-Repository\VS Code Projects\Pratice Code Project\Test Projects\Silly_GIF", "you-are-amazingly-silly.gif")

# Write the GIF file
final_clip.write_gif(gif_path, fps=15, program=imagemagick_path, opt="optimizeplus")

# Print the path of the saved GIF
print("GIF saved at:", gif_path)


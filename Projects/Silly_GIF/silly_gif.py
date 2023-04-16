"""
This module is used to create a GIF file from a text message.
"""
import os
from moviepy.editor import (TextClip, CompositeVideoClip, ColorClip,
                            ImageClip, ImageSequenceClip)

# Set up font and message
FONT_PATH = "Caveat-Bold.ttf"
FONT_SIZE = 50
FONT_COLOR = "white"
MESSAGE = "You are amazingly silly!"

# Set up background color and size
BG_COLOR = "black"
WIDTH, HEIGHT = 500, 500

# Set up duration and number of repetitions
DURATION = 30
N_REPETITIONS = DURATION // 3

# Set up path to ImageMagick convert binary
IMAGEMAGICK_PATH = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe"

# Create the text clip
TEXT_CLIP = TextClip(MESSAGE, fontsize=FONT_SIZE, font=FONT_PATH, color=FONT_COLOR)

# Set the duration of the text clip
TEXT_CLIP = TEXT_CLIP.set_duration(DURATION)

# Animate the text clip
ANIMATION_CLIP = TEXT_CLIP.set_position("center").fadein(2).fadeout(2)

# Create the directory for the image files
IMAGE_DIR = os.path.join(os.getcwd(), "images")
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# Generate the image files for the animation
for i, t in enumerate(ANIMATION_CLIP.iter_frames(fps=15, with_times=True)):
    img_path = os.path.join(IMAGE_DIR, f"frame_{i:04d}.png")
    ImageClip(t).save_frame(img_path)

# Check if the image sequence directory exists
if os.path.exists(IMAGE_DIR):
    # Create the image sequence clip from the generated image files
    ANIMATION_CLIP = ImageSequenceClip(os.path.join(IMAGE_DIR, "frame_%04d.png"), fps=15)

    # Repeat the animation and add each repetition to the video file
    ANIMATION_CLIP = ANIMATION_CLIP.set_duration(ANIMATION_CLIP.duration * N_REPETITIONS)

    # Create the background clip
    bg_clip = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR)

    # Combine the animation and background clips
    FINAL_CLIP = CompositeVideoClip([bg_clip, ANIMATION_CLIP])

    # Set the path to where the GIF will be saved
    GIF_PATH = os.path.join(os.getcwd(), "you-are-amazingly-silly.gif")

    # Write the GIF file
    FINAL_CLIP.write_gif(GIF_PATH, fps=15, program=IMAGEMAGICK_PATH, opt="optimizeplus")

    # Print the path of the saved GIF
    print("GIF saved at:", GIF_PATH)

    # Delete the image files
    for f in os.listdir(IMAGE_DIR):
        os.remove(os.path.join(IMAGE_DIR, f))
    os.rmdir(IMAGE_DIR)
else:
    print(f"Error: {IMAGE_DIR} directory does not exist")

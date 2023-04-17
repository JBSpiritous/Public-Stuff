from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Define the font and size to use for the text
font_path = "C:/Code-Repository/VS Code Projects/Public-Stuff/Projects/New_Imagine_Print/Pacifico/Pacifico-Regular.ttf" # Change this to your font path
font_size = 44
font = ImageFont.truetype(font_path, int(font_size*1.1))

# Define the text to use for the image
text = "You are awesome!"

# Define the dimensions of the background image
bg_width, bg_height = 600, 400

# Get the background image from the URL
bg_url = "https://qph.cf2.quoracdn.net/main-qimg-d335a2075ccca716ded363c3837f5fc9.webp"
bg = Image.open(BytesIO(requests.get(bg_url).content)).convert("RGBA")

# Create the text image and draw the text on it
text_img = Image.new("RGBA", (bg_width, bg_height), (255, 255, 255, 0))
draw = ImageDraw.Draw(text_img)
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
x, y = (bg_width - text_width) // 2, (bg_height - text_height) // 2
draw.text((x, y), text, font=font, fill=(255, 215, 0, 255))

# Paste the text image on top of the background image
bg.paste(text_img, (0, 0), text_img)

# Save the new image with the text overlaid
bg.save("C:/Code-Repository/VS Code Projects/Public-Stuff/Projects/New_Imagine_Print/photo/awesome.png") # Change this to your save path

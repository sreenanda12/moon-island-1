# Check color variations in the bottom 30% of assets/moonlit_backwaters_hero.png
from PIL import Image
import numpy as np

with Image.open('assets/moonlit_backwaters_hero.png') as img:
    pixels = np.array(img.convert('RGB'))
    h, w, _ = pixels.shape
    bottom = pixels[int(h*0.7):, :, :]
    
    # Check max and min brightness in the bottom part
    brightness = np.mean(bottom, axis=2)
    min_b = np.min(brightness)
    max_b = np.max(brightness)
    print("Bottom 30% brightness range: min =", min_b, ", max =", max_b)
    
    # Find how many pixels are bright (moonlit water highlights)
    bright_water = brightness > 120
    print("Number of bright water reflection pixels:", np.sum(bright_water))

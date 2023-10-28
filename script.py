
import os 
directory = "portfolio"
for i in os.listdir(directory):
    filename = i - ".svg"
    os.system(f"ffmpeg -i portfolio/{i} {filename}.webp")

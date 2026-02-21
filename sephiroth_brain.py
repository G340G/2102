from scraper import *
from sound_design import *
from director import *
from moviepy.editor import *
import os, json

def generate():
    keyword = get_keyword()
    text = scrape_text(keyword)
    scrape_image(keyword)
    generate_noise()
    style = choose_style()

    clip = ImageClip("generator/temp.jpg").set_duration(5)
    audio = AudioFileClip("generator/audio.wav")
    clip = clip.set_audio(audio)

    output_path = f"output/{keyword}.mp4"
    clip.write_videofile(output_path, fps=24)

    with open("manifest.json","w") as f:
        json.dump({"latest": output_path}, f)

if __name__ == "__main__":
    generate()from scraper import *
from sound_design import *
from director import *
from moviepy.editor import *
import os, json

def generate():
    keyword = get_keyword()
    text = scrape_text(keyword)
    scrape_image(keyword)
    generate_noise()
    style = choose_style()

    clip = ImageClip("generator/temp.jpg").set_duration(5)
    audio = AudioFileClip("generator/audio.wav")
    clip = clip.set_audio(audio)

    output_path = f"output/{keyword}.mp4"
    clip.write_videofile(output_path, fps=24)

    with open("manifest.json","w") as f:
        json.dump({"latest": output_path}, f)

if __name__ == "__main__":
    generate()

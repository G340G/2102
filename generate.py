import os
import json
from moviepy.editor import *
from director import *
from scraper import *
from sound import *
from analog import *

os.makedirs("output", exist_ok=True)

def main():

    print("Initializing Director Brain...")

    keyword = build_master_keyword()
    mode = choose_mode()

    print("Theme:", keyword)
    print("Mode:", mode)

    # SCRAPE
    text = scrape_text(keyword)
    scrape_image(keyword)

    # ANALOG EFFECT
    vhs_corrupt()

    # AUDIO
    generate_tts(f"{mode}. {text}")
    generate_noise()

    # LOAD MEDIA
    image_clip = ImageClip("corrupted.jpg").set_duration(6)
    voice = AudioFileClip("voice.wav")
    noise = AudioFileClip("noise.wav").volumex(0.5)

    final_audio = CompositeAudioClip([voice, noise])
    image_clip = image_clip.set_audio(final_audio)

    # SUBLIMINAL FRAME
    subliminal = ColorClip((640,480),(255,0,0)).set_duration(0.05)
    subliminal = subliminal.set_audio(noise.subclip(0,0.05))

    final = concatenate_videoclips([image_clip, subliminal])

    output_path = "output/SEPHIROTH_SIGNAL.mp4"

    final.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    print("Signal Generated:", output_path)

if __name__ == "__main__":
    main()


import os
import subprocess
from PIL import Image, ImageDraw

WIDTH = 1920
HEIGHT = 1080
FPS = 24

def create_scene(text, output_file, duration=5):
    image = Image.new("RGB", (WIDTH, HEIGHT), "#101827")
    draw = ImageDraw.Draw(image)

    draw.rectangle(
        (0, 0, WIDTH, 12),
        fill="#D4A843"
    )

    draw.text(
        (100, 450),
        text,
        fill="white",
        stroke_width=1
    )

    image.save(output_file)

    print("Scene created:", output_file)
    return output_file


def render_video(scenes, output_file="documentary.mp4"):

    if not scenes:
        raise ValueError("No scenes provided")

    inputs = []

    for index, scene in enumerate(scenes):
        filename = f"scene_{index}.png"

        create_scene(
            scene["text"],
            filename,
            scene.get("duration", 5)
        )

        inputs.extend([
            "-loop", "1",
            "-t", str(scene.get("duration", 5)),
            "-i", filename
        ])

    command = ["ffmpeg", "-y"] + inputs

    filters = []

    for i in range(len(scenes)):
        filters.append(
            f"[{i}:v]scale={WIDTH}:{HEIGHT},"
            f"setsar=1,setpts=PTS-STARTPTS[v{i}]"
        )

    concat = "".join(
        f"[v{i}]" for i in range(len(scenes))
    )

    filters.append(
        f"{concat}concat=n={len(scenes)}:v=1:a=0[out]"
    )

    command += [
        "-filter_complex", ";".join(filters),
        "-map", "[out]",
        "-r", str(FPS),
        "-pix_fmt", "yuv420p",
        output_file
    ]

    subprocess.run(command, check=True)

    print("Documentary rendered:", output_file)

    return output_file
  

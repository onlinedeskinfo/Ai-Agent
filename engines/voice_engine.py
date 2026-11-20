
# AI Documentary Voice Engine

import os
import asyncio
import edge_tts


async def generate_voice(text, output_file="narration.mp3"):

    voice = "hi-IN-MadhurNeural"

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(output_file)

    return output_file


def create_narration(script):

    output_file = "narration.mp3"

    asyncio.run(
        generate_voice(script, output_file)
    )

    print("Voice generated successfully!")

    return output_file
  


# AI Documentary Audio Engine

from pydub import AudioSegment


def mix_audio(
    narration_file,
    music_file,
    output_file="final_audio.mp3"
):

    narration = AudioSegment.from_file(
        narration_file
    )

    music = AudioSegment.from_file(
        music_file
    )

    # Background music volume
    music = music - 22

    # Match music duration with narration
    music = music[:len(narration)]

    # Combine voice and background music
    final_audio = narration.overlay(music)

    # Export final audio
    final_audio.export(
        output_file,
        format="mp3",
        bitrate="192k"
    )

    print("Audio mixing completed!")

    return output_file
  

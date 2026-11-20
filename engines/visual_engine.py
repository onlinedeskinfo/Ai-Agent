
# AI Documentary Visual Engine

def create_visual_prompts(scenes):

    visual_prompts = []

    for index, scene in enumerate(scenes, start=1):

        prompt = f"""
Create a professional 2D animated
historical documentary scene.

Scene Number: {index}

Scene Description:
{scene}

Visual Requirements:
- High quality 2D animation
- Historical accuracy
- Detailed backgrounds
- Consistent characters
- Cinematic lighting
- Smooth character movement
- Professional camera movements
- 16:9 widescreen composition
- 1080p visual quality

Animation Style:
Premium educational documentary.

Avoid:
- Modern objects in historical scenes
- Inconsistent character designs
- Distorted faces
- Random visual elements
"""

        visual_prompts.append(prompt)

    return visual_prompts
  

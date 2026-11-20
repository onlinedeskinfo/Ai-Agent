def create_script(topic, research, duration=5):

    words_per_minute = 125
    target_words = duration * words_per_minute

    prompt = f"""
    Create a professional 2D documentary script.

    Topic: {topic}

    Research:
    {research}

    Language: Hinglish (Hindi + English)
    Visual Style: 2D Animation
    Duration: {duration} minutes
    Target Words: {target_words}

    Include:
    1. Powerful opening hook
    2. Historical background
    3. Important events in timeline
    4. Scene-by-scene narration
    5. Visual descriptions for every scene
    6. Camera movement instructions
    7. Strong ending

    Make the documentary engaging and factual.
    """

    return prompt

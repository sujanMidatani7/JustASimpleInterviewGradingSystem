from gtts import gTTS

def text_to_speech(text):
    """
    This function converts text to speech using Google Text-to-Speech API.

    Args:
        text (str): The text to convert to speech.

    Returns:
        str: The name of the output file.
    """
    tts = gTTS(text)
    tts.save("output.mp3")

    return "output.mp3"

import speech_recognition as sr

def takeCommand(audio):
    """
    This function takes an audio file as input and returns the recognized speech as text.
    
    Parameters:
    audio (str): The path to the audio file.
    
    Returns:
    str: The recognized speech as text.
    """
   
    # Initialize a Recognizer object
    r = sr.Recognizer()
    
    # Open the audio file and record the audio data
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)

    try:
        # Use the recognize_google method to recognize the speech from the audio data
        query = r.recognize_google(audio_data, language="en-in")
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print(f"Error occurred: {e}")

    return "Some error occurred."

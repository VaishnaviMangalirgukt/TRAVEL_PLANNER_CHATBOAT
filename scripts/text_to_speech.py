import pyttsx3

def speak_output(text):
    """Converts text into speech and plays it."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust speed
    engine.setProperty("volume", 1.0)  # Set volume
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    sample_text = "Hello! This is a Travel Planner Chatbot response."
    speak_output(sample_text)
import pyttsx3

def list_available_voices():
    """Lists available voices in the system."""
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} ({voice.languages}) - ID: {voice.id}")

def speak_output(text, voice_type="default"):
    """Converts text into speech and plays it."""
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)  # Adjust speed
        engine.setProperty("volume", 1.0)  # Set volume

        # Get available voices
        voices = engine.getProperty("voices")

        # Set voice type
        if voice_type == "male":
            engine.setProperty("voice", voices[0].id)  # Usually male
        elif voice_type == "female" and len(voices) > 1:
            engine.setProperty("voice", voices[1].id)  # Usually female
        # Default system voice otherwise

        engine.say(text)
        engine.runAndWait()
    
    except Exception as e:
        print(f"Error in TTS: {e}")

# Run the script for testing
if __name__ == "__main__":
    print("Available voices:")
    list_available_voices()
    
    sample_text = "Hello! This is a Travel Planner Chatbot response."
    speak_output(sample_text, voice_type="female")  # Change to "male" if needed

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    print("Say something:")
    
    # Capture the audio
    audio_data = recognizer.listen(source)

    try:
        # Convert the speech to text
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        print("You said: " + text)

    except sr.UnknownValueError:
        # Error if speech is unintelligible
        print("Google Speech Recognition could not understand the audio.")
    
    except sr.RequestError:
        # Error if there's an issue with the request
        print("Could not request results from Google Speech Recognition service.")

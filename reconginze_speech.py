import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Capturegit  audio from the microphone
with sr.Microphone() as source:
    print("Listening...")
    try:
        audio = r.listen(source, timeout=5)  # Record audio for up to 5 seconds
        print("Audio captured successfully.")
    except sr.WaitTimeoutError:
        print("No speech detected. Exiting...")
        exit()

# Convert the audio to text
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand your audio.")
except sr.RequestError as e:
    print(f"Sorry, there was an error with the speech recognition service: {e}")

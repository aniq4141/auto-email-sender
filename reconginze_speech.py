import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Listening...")
    try:
        audio = r.listen(source)
        print("Listening...")
    except Exception as e:
        print(e)
    print("hello")

# Convert the audio to text
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand your audio.")
except sr.RequestError as e:
    print(f"Sorry, there was an error with the speech recognition service: {e}")
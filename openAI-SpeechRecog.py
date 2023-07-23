import openai
import speech_recognition as sr
import pyttsx3

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main program loop
while True:
    user_input = listen()

    # Generate a response from the AI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        echo=True
    )

    # Extract and print the AI's reply
    ai_reply = response.choices[0].text.strip()
    print("ChatGPT: " + ai_reply)
    speak(ai_reply)

    # Terminate the loop if the user says goodbye
    if 'goodbye' in user_input.lower():
        break

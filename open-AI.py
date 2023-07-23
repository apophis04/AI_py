import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Main program loop
while True:
    user_input = input("You: ")

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

    # Terminate the loop if the user says goodbye
    if 'goodbye' in user_input.lower():
        break

import openai

# Initialize the API client
openai.api_key = "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"

# Set the engine and model for the chatbot
engine = "text-davinci-003"

while True:
    # Get input/question from the user
    user_input = input("What is your question for OpenAI DaVinci003 model? ")

    # Get the response from GPT-3
    # From chatGPT API documentation https://platform.openai.com/docs/api-reference/introduction
    response = openai.Completion.create(
        engine=engine,
        prompt=user_input,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the response
    generated_text = response["choices"][0]["text"]

    # Print the generated text
    print(generated_text)

    # prompt user input and handle exit conditions
    user_input = input("Would you like to continue asking questions? (y/n): ")

    if user_input == "n":
        print()
        print("Deuces!")
        break

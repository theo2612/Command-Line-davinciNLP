import openai

# Initialize the API client
openai.api_key = "insert-api-key-here"

# Get input/question from the user
UserQForChatGPT = input("What is your question for ChatGPT? ")

# Get the response from GPT-3
# From chatGPT API documentation https://platform.openai.com/docs/api-reference/introduction
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=UserQForChatGPT,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract the generated text from the response
generated_text = response["choices"][0]["text"]

# Print the generated text
print(generated_text)

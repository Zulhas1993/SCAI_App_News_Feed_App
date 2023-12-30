import openai

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

def ask_gpt3(question):
    # Define the prompt by specifying that you want to ask a question
    prompt = f"I have a question: {question}"

    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=150  # Adjust based on the desired length of the response
    )

    # Extract the generated response from the API result
    answer = response.choices[0].text.strip()

    return answer

# Example usage
user_question = input("Ask a question: ")
response = ask_gpt3(user_question)
print("GPT-3 Response:", response)


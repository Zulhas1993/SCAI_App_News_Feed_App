from flask import Flask, render_template, request
import openai
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

def ask_gpt3(question):
    # Define the prompt by specifying that you want to ask a question
    prompt = f"I have a question: {question}"

    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    # Extract the generated response from the API result
    answer = response.choices[0].text.strip()

    return answer

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        user_question = request.form['question']
        response = ask_gpt3(user_question)
    return render_template('templates/questionapp.html', response=response)


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

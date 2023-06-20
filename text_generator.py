import openai
from openai_key import API_KEY

openai.api_key = API_KEY
model_engine = "text-davinci-003"

prompt = "Edgy humor text about bad youtube content"

print("The Text Has Been Generated Successfully!")
def generate_text():
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=96,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the generated text
    generated_text = completions.choices[0].text
    return generated_text
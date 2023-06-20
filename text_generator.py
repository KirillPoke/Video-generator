import openai
from openai_key import API_KEY

openai.api_key = API_KEY
model_engine = "text-davinci-003"#"text-ada-001"

prompt = "Write ridiculing story about reddit, exagerating the situation and making fun of it."
prompt_with_meta = f"Write about the following topic: {prompt}. Write in short sentences separated by . Write about 5 complete sentences."
print("The Text Has Been Generated Successfully!")
def generate_text():
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_with_meta,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the generated text
    generated_text = completions.choices[0].text
    return generated_text
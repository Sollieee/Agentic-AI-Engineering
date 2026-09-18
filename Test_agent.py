from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env into the environment
client = OpenAI()  # now picks up OPENAI_API_KEY
question  = "What are three important factors a farmer should consider before planting maize? Answer clearly using plain text only."

response = client.responses.create(
    model="gpt-5.6-sol",
    input=question 
    )

print(response.output_text)

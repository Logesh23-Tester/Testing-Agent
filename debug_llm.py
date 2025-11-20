import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()

model_name = os.getenv("MODEL", "gemini/gemini-1.5-pro-latest")
api_key = os.getenv("GOOGLE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

print(f"Testing model: {model_name}")

try:
    if "gpt" in model_name.lower():
        print("Using OpenAI...")
        llm = ChatOpenAI(
            model=model_name,
            verbose=True,
            temperature=0.5,
            api_key=openai_api_key
        )
    else:
        print("Using Google Gemini...")
        if model_name.startswith("gemini/"):
            model_name = model_name.replace("gemini/", "")
        print(f"Adjusted model name: {model_name}")
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            verbose=True,
            temperature=0.5,
            google_api_key=api_key
        )

    response = llm.invoke("Hello, are you working?")
    print("Success! Response:")
    print(response.content)

except Exception as e:
    print("Error occurred:")
    print(e)

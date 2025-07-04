from ai import call_gpt

# GPT4O model

def main():
    response = call_gpt("What are you? ")
    print(response)

# "I am an artificial intelligence language model created by OpenAI, designed to assist with a wide range of inquiries and provide information on various topics"

if __name__ == "__main__":
    main()
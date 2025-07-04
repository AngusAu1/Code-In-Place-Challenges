from ai import call_gpt

"""
Write a program that will tell the user 
the captial city of a country
"""

def main():
    country = input("Country: ")
    print("Thinking...")
    capital = call_gpt(f"What is the capital city of {country}")
    print(capital)
    

# "I am an artificial intelligence language model created by OpenAI, designed to assist with a wide range of inquiries and provide information on various topics"

if __name__ == "__main__":
    main()
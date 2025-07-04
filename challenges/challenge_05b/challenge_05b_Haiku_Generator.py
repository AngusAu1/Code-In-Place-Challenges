# import the ai module - call_gpt
from ai import call_gpt

def main():
    # defined name and topic for user input
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    print("Creating your haiku...")

    # response is the statement that with those valuables which will used for call_gpt()
    response = f"using your {name} and the topic: {topic} to turn into a haiku"

    # use the call_gpt() for input the statement into it
    response = call_gpt(response)
    print(response)

    # testing to call the input function and put it into call_gpt()
    """
    response = input("Please input your prompt: ")
    response = call_gpt(response)
    print(response)
    """

if __name__ == "__main__":
    main()
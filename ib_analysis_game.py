import random
import textwrap

# Define text types and sample prompts for various difficulties
text_types = {
    'Advertisement': [
        "A sleek and minimalistic print ad for a new smartphone, highlighting its eco-friendly production.",
        "A loud, colourful commercial showcasing a cleaning product that removes tough stains in seconds."
    ],
    'Blog Post': [
        "An influencer's reflective post about sustainable fashion choices.",
        "A personal journal entry recounting a cross-country road trip adventure."
    ],
    'Speech': [
        "A politician's campaign speech focused on education reform.",
        "A motivational talk encouraging resilience during setbacks."
    ],
    'News Report': [
        "A factual report about a recent scientific discovery and its potential impact on health.",
        "An investigative article exploring the rise of urban farming."
    ],
    'Cartoon': [
        "A single-panel comic illustrating the irony of online privacy in the age of social media.",
        "A satirical graphic highlighting consumerism during holiday sales."
    ]
}

difficulties = {
    'Easy': "Identify the target audience and primary purpose of this text. Discuss one persuasive technique used.",
    'Medium': "Analyze how the structure and tone contribute to the text's effectiveness. Identify hidden implications.",
    'Hard': "Examine subtle stylistic devices and intertextual references. Reflect on cultural or ideological messages that might not be evident at first glance."
}

def choose_text_type():
    return random.choice(list(text_types.keys()))

def choose_prompt(text_type):
    return random.choice(text_types[text_type])

def choose_difficulty():
    return random.choice(list(difficulties.keys()))

def display_challenge():
    text_type = choose_text_type()
    prompt = choose_prompt(text_type)
    difficulty = choose_difficulty()

    print("\n--- New Challenge ---")
    print(f"Text Type: {text_type}")
    print("Sample Text / Scenario:")
    print(textwrap.fill(prompt, width=80))
    print("\nChallenge Level: ", difficulty)
    print(difficulties[difficulty])
    input("\nYour response: ")  # Pause for player response
    print("\nReflection Tips:")
    print("- Did you consider the text's context and potential biases?")
    print("- Can you think of alternative interpretations that challenge the obvious?")
    print("- How do visual elements (if any) interact with the written content?\n")


def game_loop():
    print("Welcome to the IB Text Analysis Game!")
    while True:
        display_challenge()
        cont = input("Press Enter to continue or type 'quit' to exit: ")
        if cont.lower().strip() == 'quit':
            print("Thanks for playing! Keep analyzing beyond the surface!")
            break

if __name__ == "__main__":
    game_loop()

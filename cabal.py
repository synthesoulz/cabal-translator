import openai

openai.api_key = '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'

dictionary = {
    "words": {
        "Believer (colloquial)": "rud'minuox",
        "Believer (formal)": "rudsceleratus",
        "Blessed (formal)": "pestis cruento",
        "Blood (formal)": "cruo",
        "Blood brother (formal)": "crunatus",
        "Blood heaven (formal)": "pretiacruento",
        "Bloodhungry (formal)": "cruentu",
        "Bloodshed (colloquial)": "cruensseasrjit",
        "Bloodthirsty (colloquial)": "cruonit",
        "Chaos (formal)": "shaantitus",
        "Curse (formal)": "cruento pestis",
        "Dark (formal)": "domus",
        "Death (colloquial)": "marana",
        "Drink (colloquial)": "bibox",
        "Eat (colloquial)": "vorox",
        "Ecstasy/enlightenment (formal)": "cruento paashaeximus",
        "Enemies (formal)": "Shatruex",
        "Foreigner (formal)": "infirmux",
        "Fresh (colloquial)": "crudux",
        "Gun (colloquial)": "vigra",
        "Hate (colloquial)": "invisux",
        "Hate (formal)": "invisuu",
        "Heaven (formal)": "maravita",
        "Home (formal)": "domus-bhaava",
        "Light (formal)": "acerbus-shatruex",
        "Living dead (formal)": "pretaanluxis",
        "Love (colloquial)": "odiosux",
        "Love (formal)": "odiosuu",
        "Massacre (colloquial)": "cruo-stragaraNa",
        "Massacre (formal)": "prayaNavita",
        "Order (formal)": "vilomaxus",
        "Pray (colloquial)": "profanx",
        "Pray (formal)": "profanuxes",
        "Shit (colloquial)": "exim’ha",
        "Spirit (colloquial)": "tuulenux",
        "Spirit (formal)": "praaNsilenux",
        "To be (colloquial)": "esco",
        "To be (formal)": "bhuuesco",
        "To become (colloquial)": "desco",
        "To become (formal)": "bhuudesco",
        "To do, inflict upon (colloquial)": "hatanoceo",
        "To do, to inflict upon (formal)": "hatanoceo",
        "To have, possess (colloquial)": "gero",
        "To have, possess (formal)": "geropayati",
        "To make bloody (colloquial)": "cruonita",
        "To make dark (formal)": "infuscomus",
        "Unbeliever/Humanity (colloquial)": "malax",
        "Unbeliever/Humanity (formal)": "caecux",
        "Unquenchable (formal)": "quodpipax",
        "Weakling (colloquial)": "pallex",
        "Wisdom (formal)": "durbentia",
        "World (formal)": "lokemundux",
        "Kill (colloquial)": "neco",
        "Kill (formal)": "occido",
        "Kill (alternate formal)": "interficio",
        "Raw (colloquial)": "crudusux",
        "Raw (formal)": "crudusuu",
        "Bloody (colloquial)": "cruentusux",
        "Bloody (formal)": "cruentusuu",
        "Gore (colloquial)": "cruorux",
        "Gore (formal)": "cruoruu",
        "Hateful (colloquial)": "odiosusux",
        "Hateful (formal)": "odiosusuu",
        "Hated (colloquial)": "invisusux",
        "Hated (formal)": "invisusuu",
        "Prayer (colloquial)": "profanxux",
        "Prayer (formal)": "profanxuu",
        "Destroy (colloquial)": "interficioxx",
        "Destroy (formal)": "interficioxxx",
        "Spiritual (colloquial)": "tuulenuxux",
        "Spiritual (formal)": "tuulenuxuu"


    },
    "phrases": {
        "apigami": "_________",
        "bhuudesco invisuu": "To become hate (formal)",
        "bhuuesco marana": "To be death",
        "crudux cruo": "Fresh blood",
        "cruento paashaeximus": "Ecstasy / Enlightenment (formal)",
        "cruento pestis shatruex": "Curse enemies (formal)",
        "cruo crunatus durbe": "Blood blood brother wise (formal?)",
        "cruo lokemundux": "Blood world (formal)",
        "cruo stragarana malaxos": "Massacre ___________",
        "geroxe cruo": "To have _________ blood",
        "En marana domus nava crunatus": "__ death home blood brother",
        "caecux infirmux": "Unbeliever foreigner (formal)",
        "malax \"say ti\"": "Unbeliever / humanity _________",
        "maranax pallex": "Death to the weakling (colloquial)",
        "maranax malax": "Death to the unbeliever",
        "maranax infirmux": "Death to the outsider",
        "pallex \"ti\"": "Weakling _____",
        "Geroxe bibox malax": "________ drink unbeliever / humanity",
        "pestis Cruento": "Blessed (formal)",
        "pestis cruento vilomaxus pretiacruento": "Blessed order blood heaven (formal)",
        "pretaanluxis cruonit": "Living dead bloodthirsty",
        "pretiacruento": "Blood heaven",
        "stragarana": "Massacre?",
        "vorox esco marana": "Eat to be death (colloquial)",
        "vilomaxus": "Order (formal)",
        "\"Pro\" stragarana malaxos": "Said as a Cultist chant by Brian Goble"
    }
}

def generate_prompt(dictionary, text):
    prompt = "Translate the following English text to the **Cultist Language**, " \
             "a derivative of **Latin, French, and Sanskrit** with two forms - **FORMAL and colloquial**. " \
             "It is **SHARP, CRASS, TERRIFYING** and meant to **UNNERVE** non-cult members. " \
             "The Cultist Language **AMALGAMATES ELEMENTS FROM LATIN AND ITALIAN**, " \
             "often **CHANGING** the -us ending to -ux as well as other linguistic transformations. " \
             "For example, Latin 'crudus' means 'raw', 'cruentus' is 'bloody', and 'cruor' is 'blood' or 'gore', " \
             "while Italian 'crudus' becomes 'crudusux' in the Cultist Language. " \
             "This blending of Latin and Italian vocabulary adds an **ADDITIONAL LAYER OF COMPLEXITY** " \
             "and enhances the **SINISTER AURA** of the Cultist Language. " \
             "Some of the words' meanings appear to be **ALTERED SIGNIFICANTLY OR MOCKINGLY INVERTED**. " \
             "This intentional inversion is a powerful linguistic tool that evokes an **UNSETTLING AND EERIE ATMOSPHERE**, " \
             "twisting the familiar meanings of words. By altering Latin and Italian vocabulary and inverting their meanings, " \
             "the Cultist Language takes on an **OTHERWORLDLY AND MALEVOLENT CHARACTER**. " \
             "The intentional inversion of positive concepts like 'love' becoming 'hateful' or 'blessed' " \
             "being transformed into 'curse' can create a **SENSE OF DREAD AND DISCOMFORT** in the listener. " \
             "This inversion serves to **UNNERVE NON-CULT MEMBERS** and reinforces the **MYSTERIOUS AND FOREBODING NATURE** " \
             "of the Cultist Language. It gives the impression of a language that **DEFIES CONVENTIONAL NORMS AND MORALITY**, " \
             "instilling **FEAR AND INTRIGUE** in those who encounter it. " \
             "Overall, the importance of amalgamating Latin and Italian elements and inverting their meanings " \
             "lies in its ability to enhance the **DARK AND SINISTER NATURE** of the Cultist Language, " \
             "contributing to its intended purpose of being sharp, crass, and terrifying. " \
             "Now, using the provided dictionary, translate the following text:"

    for category, translations in dictionary.items():
        for english, translation in translations.items():
            prompt += f'- "{english}" is "{translation}" in Cultist ({category}).\n'

    prompt += f'\nTranslate: "{text}"'

    return prompt



def translate_english_to_cultist(dictionary, text):
    prompt = generate_prompt(dictionary, text)

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.3,
      max_tokens=150
    )

    return response.choices[0].text.strip()

def explain_word_formation(word):
    # A call to OpenAI's GPT-3 model to generate an explanation for the formation of the word.
    prompt = f"Explain the possible linguistic origins and formation of the word '{word}' in a hypothetical language derived from Latin, French, Italian and Sanskrit."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].text.strip()


if __name__ == "__main__":
    print("English to Cultist translation service is now running.")
    print("Enter the text you want to translate, or type 'EXIT' to quit.")

    most_recent_translation = None

    while True:
        user_input = input("\nEnter your text: ")

        if user_input.strip().upper() == "EXIT":
            print("Exiting the translator. Goodbye!")
            break
        elif user_input.strip().lower() == "explain":
            if most_recent_translation:
                explanation = explain_word_formation(most_recent_translation)
                print(explanation)
            else:
                print("No recent translation to explain.")
        else:
            most_recent_translation = translate_english_to_cultist(dictionary, user_input)
            print(f'Translated text: {most_recent_translation}')

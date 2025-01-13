import asyncio
from googletrans import Translator

async def translate_text():
    """
    Asynchronous text translation software using Google Translate.
    """
    # Initialize the translator
    translator = Translator()

    # Display supported language options
    print("Welcome to the Translation Software!")
    print("Enter the text you want to translate.")
    print("For example: 'Hello, how are you?'")
    
    # Input the text to be translated
    text_to_translate = input("\nEnter text: ").strip()

    # Input the source and target languages
    print("\nSupported Language Codes:")
    print("English: en, Yoruba: yo, Hausa: ha, Igbo: ig, French: fr, Spanish: es, etc.")
    source_lang = input("Enter source language code (e.g., 'en' for English): ").strip()
    target_lang = input("Enter target language code (e.g., 'yo' for Yoruba): ").strip()

    # Handle empty inputs
    if not text_to_translate or not source_lang or not target_lang:
        print("Error: All fields are required. Please try again.")
        return

    try:
        # Perform the translation asynchronously
        translated = await translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        print("\nOriginal Text: ", text_to_translate)
        print("Translated Text: ", translated.text)

    except Exception as e:
        print(f"An error occurred during translation: {e}")

if __name__ == "__main__":
    # Run the asynchronous translation function
    asyncio.run(translate_text())

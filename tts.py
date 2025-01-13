# Import the required libraries
from gtts import gTTS
import os

def text_to_speech():
    """
    A Text-to-Speech converter with added support for African languages like Yoruba, Hausa, 
    and placeholder handling for unsupported languages like Igbo.
    """
    # Display a welcome message and supported languages
    print("Welcome to the Text-to-Speech Converter!")
    print("Supported Languages:")
    print("1. English (en)")
    print("2. Spanish (es)")
    print("3. French (fr)")
    print("4. German (de)")
    print("5. Italian (it)")
    print("6. Yoruba (yo)")
    print("7. Hausa (ha)")
    print("8. Igbo (ig) - Not yet supported but included for demonstration.\n")
    print("Enter the language code corresponding to your desired language (e.g., 'en' for English).")

    # Prompt the user to select a language
    language = input("Language Code: ").strip()  # Read and trim the input

    # Define a list of supported language codes
    supported_languages = {
        'en': "English",
        'es': "Spanish",
        'fr': "French",
        'de': "German",
        'it': "Italian",
        'yo': "Yoruba",
        'ha': "Hausa",
    }

    # Handle unsupported languages like Igbo
    if language == 'ig':
        print("Sorry, Igbo is not supported at the moment.")
        return  # Exit the function if the user selects an unsupported language

    # Validate if the entered language code is supported
    if language not in supported_languages:
        print(f"Error: '{language}' is not a supported language. Please try again.")
        return  # Exit the function if the language is invalid

    # Prompt the user to input the text for conversion
    text = input(f"Enter the text you want to convert to speech in {supported_languages[language]}: ").strip()

    # Check if the user provided any text
    if not text:
        print("Error: No text entered. Please try again.")
        return  # Exit the function if no text is provided

    try:
        # Use gTTS to convert the text into speech
        # 'lang' specifies the language for conversion
        tts = gTTS(text=text, lang=language)

        # Save the generated speech to an output file
        output_file = f"output_{language}.mp3"
        tts.save(output_file)
        print(f"\nSpeech successfully generated and saved as '{output_file}'.")

        # Ask the user if they want to play the generated speech
        play_choice = input("Do you want to play the generated speech? (yes/no): ").strip().lower()

        # Check the user's choice and play the file if they opt to
        if play_choice == 'yes':
            if os.name == 'nt':  # For Windows systems
                os.system(f'start {output_file}')
            elif os.name == 'posix':  # For macOS and Linux systems
                if 'darwin' in os.uname().sysname.lower():  # macOS
                    os.system(f'open {output_file}')
                else:  # Linux
                    os.system(f'xdg-open {output_file}')
    except Exception as e:
        # Handle any exceptions that occur during text-to-speech conversion
        print(f"An error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    # Call the text_to_speech function to start the program
    text_to_speech()

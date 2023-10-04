# Import required libraries
import re

# Define a function to translate English to Hinglish
def translate_to_hinglish(text):
    # Define a dictionary of English to Hinglish translations
    translation_dict = {
        "Definitely": "ज़रूर",
        "share": "शेयर",
        "feedback": "फ़ीडबैक",
        "comment section": "कमेंट सेक्शन",
        "So even if it's a big video,": "तो चाहे ये एक बड़ा वीडियो हो,",
        "I will clearly mention all the products.": "मैं साफ-साफ सब प्रोडक्ट्स का मेंशन कर दूँगा।",
        "I was waiting for my bag.": "मैं अपनी बैग का इंतजार कर रहा था।",
    }

    # Use regular expressions to find and replace English words with Hinglish
    for key, value in translation_dict.items():
        text = re.sub(r'\b' + key + r'\b', value, text)

    return text

# Example usage:
english_text = "Definitely share your feedback in the comment section. I was waiting for my bag."
hinglish_text = translate_to_hinglish(english_text)
print(hinglish_text)

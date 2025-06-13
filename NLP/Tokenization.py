from nltk.tokenize import word_tokenize

text = ("India’s monsoon season has officially begun, bringing much-needed rainfall to southern states. "
        "Apple has unveiled iOS 19 with major AI-powered features during its WWDC 2025 event. "
        "Delhi recorded its highest temperature of the year at 47.2°C, prompting a red heatwave alert.")

tokens = word_tokenize(text)
print(tokens)

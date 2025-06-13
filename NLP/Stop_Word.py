# Stop-word Removal Example
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

text = ("India’s monsoon season has officially begun, bringing much-needed rainfall to southern states. "
        "Apple has unveiled iOS 19 with major AI-powered features during its WWDC 2025 event. "
        "Delhi recorded its highest temperature of the year at 47.2°C, prompting a red heatwave alert.")

tokens = word_tokenize(text)
stops = set(stopwords.words('english'))
filtered = [word for word in tokens if word.lower() not in stops and word.isalpha()]
print("After stop-word removal:", filtered)

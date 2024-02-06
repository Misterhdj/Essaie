import nltk
from nltk.corpus import gutenberg
from collections import Counter

# Chargement du texte français
nltk.download('punkt')
nltk.download('stopwords')
sentences = gutenberg.sents('french.txt')

# Tokenization et mise en minuscules
words = [word.lower() for sentence in sentences for word in sentence]

# Filtrage des mots vides (stop words)
stopwords = set(nltk.corpus.stopwords.words('french'))
words = [word for word in words if word.isalpha() and word not in stopwords]

# Comptage des occurrences des mots
word_freq = Counter(words)

# Récupération des 5000 mots les plus courants
most_common_words = [word for word, _ in word_freq.most_common(5000)]

# Écriture des mots dans un fichier texte
with open("5000_mots_courants_francais.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(most_common_words))

print("Fichier créé avec succès : 5000_mots_courants_francais.txt")

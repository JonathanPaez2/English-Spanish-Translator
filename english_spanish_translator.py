class Dictionary:
  def __init__(self):
    self.entries = {}

  def add(self, english, spanish):
    self.entries[english] = spanish

  def translate(self, word):
    if word in self.entries:
      return self.entries[word]
    else:
      return None

def translate_words():
  dictionary = Dictionary()

  while True:
    action = input("Would you like to [a]dd a word, [t]ranslate a word, or [q]uit? ")
    if action == "q":
      break
    elif action == "a":
      english = input("Enter the English word: ")
      spanish = input("Enter the Spanish translation: ")
      dictionary.add(english, spanish)
    elif action == "t":
      word = input("Enter a word to translate: ")
      translation = dictionary.translate(word)
      if translation is not None:
        print(f"{word} translates to {translation}.")
      else:
        print(f"{word} could not be found in the dictionary.")
    else:
      print("Invalid action. Please try again.")

translate_words()

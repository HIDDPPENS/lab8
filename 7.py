import os

class SentenceError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class LexicographicalIterator:
    def __init__(self, sentence_obj):
        self._sorted_words = sorted(sentence_obj.words)
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._sorted_words):
            word = self._sorted_words[self._index]
            self._index += 1
            return word
        else:
            raise StopIteration
class Sentence:
    def __init__(self, content=""):
        if isinstance(content, str):
            self.words = content.split()
        elif isinstance(content, list):
            self.words = list(content)
        else:
            self.words = []
    def __len__(self):
        return len(self.words)
    def __getitem__(self, index):
        return self.words[index]
    def __setitem__(self, index, value):
        if not isinstance(value, str):
            raise SentenceError(
                f"Помилка присвоєння: слово має бути рядковим літералом (str), передано {type(value).__name__}.")
        self.words[index] = value
    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(self.words + other.words)
        elif isinstance(other, str):
            return Sentence(self.words + [other])
        else:
            raise SentenceError(
                f"Помилка додавання (+): правий операнд має бути класом Sentence або str, отримано {type(other).__name__}.")
    def __sub__(self, other):
        if isinstance(other, Sentence):
            words_to_remove = set(other.words)
            return Sentence([w for w in self.words if w not in words_to_remove])
        elif isinstance(other, str):
            return Sentence([w for w in self.words if w != other])
        else:
            raise SentenceError(
                f"Помилка віднімання (-): правий операнд має бути класом Sentence або str, отримано {type(other).__name__}.")
    def __contains__(self, item):
        return item in self.words
    def __str__(self):
        return " ".join(self.words)
    def __iter__(self):
        return LexicographicalIterator(self)
def process_text(filename, replacements, words_to_delete):
    if not os.path.exists(filename):
        print(f"Файл {filename} не знайдено.")
        return 0
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    sentence = Sentence(text)
    for i in range(len(sentence)):
        clean_word = sentence[i].strip(".,!?;:\"'()")
        if clean_word in replacements:
            sentence[i] = sentence[i].replace(clean_word, replacements[clean_word])
    for word in words_to_delete:
        sentence = sentence - word
    print(sentence)
    return len(sentence)
if __name__ == "__main__":
    test_filename = "test_text.txt"
    with open(test_filename, "w", encoding="utf-8") as f:
        f.write("Це дуже старий текст. Він містить погані слова та зайвий сміття.")
    replace_dict = {"старий": "новий", "погані": "гарні"}
    delete_list = ["зайвий", "сміття.", "дуже", "та"]
    final_word_count = process_text(test_filename, replace_dict, delete_list)
    print(f"Загальна кількість слів після коригування: {final_word_count}\n")
    if os.path.exists(test_filename):
        os.remove(test_filename)
    text_for_iterator = "яблуко ананас банан груша"
    sentence_iter = Sentence(text_for_iterator)
    for word in sentence_iter:
        print(word)
    print("\n")
    s1 = Sentence("Це тестове речення")
    try:
        s1[1] = 123
    except SentenceError as e:
        print(e)
    try:
        s2 = s1 + ['новий', 'список']
    except SentenceError as e:
        print(e)
    try:
        s3 = s1 - 45.6
    except SentenceError as e:
        print(e)
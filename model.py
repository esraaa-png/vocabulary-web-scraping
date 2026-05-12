class Example:
    def __init__(self, text, translation):
        self.text = text
        self.translation = translation

    def toDict(self):
        return self.__dict__


class Meaning:
    def __init__(self, meaning):
        self.meaning = meaning
        self.examples = []

    def addExample(self, example):
        self.examples.append(example.toDict())

    def toDict(self):
        return {
            "meaning": self.meaning,
            "examples": self.examples
        }


class Block:
    def __init__(self, type_):
        self.type = type_
        self.meanings = []

    def addMeaning(self, meaning):
        self.meanings.append(meaning.toDict())

    def toDict(self):
        return {
            "type": self.type,
            "meanings": self.meanings
        }


class Vocabulary:
    def __init__(self, word, image_api, image, audio_api, audio, spelling):
        self.word = word
        self.image_api = image_api
        self.image = image
        self.audio_api = audio_api
        self.audio = audio
        self.spelling = spelling
        self.translation = []

    def addTranslation(self, block):
        self.translation.append(block.toDict())

    def toObj(self):
        return self.__dict__
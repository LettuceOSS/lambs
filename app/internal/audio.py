import re

class AudioGeneration():
    def __init__(
        self,
        text: str,
        id: str,
        folder: str
    ):
        """
        Audio generation initialization

        Parameters
        ----------
        text: str
            Text on which audio will be generated.
        id: str
            Unique text identifier.
        folder: str
            Absolute or relative folder's path where the audio files will be saved.
        """
        self.text = text
        self.id = id
        self.folder = folder

    def __split_text(
        self,
        exceptions: list[str] = [" ", "\'"]
    ):
        """
        Dividing a text using punctuation (non-alphanumeric chars minus custom exceptions)

        Parameters
        ----------
        exceptions: list[str]
            Char exceptions while splitting. Default values: [" ", "'"].

        Returns
        -------
        sentences: list[str]
            List containing sentences from the original text.
        """
        # Splitting text by using any Unicode non-alphanumeric chars
        sentences = []
        start = 0
        for i in range(len(self.text)):
            if (not self.text[i].isalnum() and self.text[i] not in exceptions) or i == len(self.text) - 1:
                sentences.append(self.text[start:i+1])
                start = i + 1
        return sentences

        

    def __tts(
        self,
        texts: list[str]
    ):
        """
        Generate an audio file for each text

        Parameters
        ----------
        texts: list[str]
        """
        pass

    def __concat_files(
        self
    ):
        """
        Concatenate every audios from the same text.
        """
        pass

    def generation(
        self
    ):
        self.__split_text()

if __name__ == "__main__":
    test = AudioGeneration(
        text="Ceci, enfin ce qu'il en reste, est une phrase! Je serais heureux que ça fonctionne.",
        id="testid",
        folder="."
    )
    test.generation()
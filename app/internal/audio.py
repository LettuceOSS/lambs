import re
import pandas as pd
from gtts import gTTS
from zipfile import ZipFile
import subprocess
import os

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
            Text on which audio will be generated
        id: str
            Unique text identifier
        folder: str
            Absolute or relative folder's path where the audio files will be saved
        """
        self.text = text
        self.id = id
        self.folder = folder
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def __split_text(
        self,
        exceptions: list[str] = [" ", "\'"]
    ):
        """
        Dividing a text using punctuation (non-alphanumeric chars minus custom exceptions)

        Parameters
        ----------
        exceptions: list[str]
            Char exceptions while splitting. Default values: [" ", "'"]

        Returns
        -------
        sentences: list[str]
            List containing sentences from the original text
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
        texts: list[str],
        lang: str = "fr"
    ):
        """
        Generate an audio file for each text

        Parameters
        ----------
        texts: list[str]
            List containing sentences for TTS
        lang: str
            IETF language tag

        Returns
        -------
        audios: Pandas DataFrame
            DataFrame containing sentences and corresponding audio
        """
        # Creating Pandas DataFrame
        columns = ["sentence", "audio_abs_path"]
        audios = pd.DataFrame(
            columns=columns
        )
        # Generating TTS for each sentence
        for i in range(len(texts)):
            # Generating TTS and saving it
            tts = gTTS(
                text=texts[i],
                lang=lang
            )
            folder_abs_path = os.path.abspath(
                path=self.folder
            )
            filename = self.id + "_" + str(i) + ".mp3"
            audio_abs_path = os.path.join(
                folder_abs_path,
                filename
            )
            tts.save(audio_abs_path)
            # Adding sentence and file path to DataFrame
            row = [
                texts[i],
                audio_abs_path
            ]
            audios.loc[len(audios)] = row
        return audios

    def __concat_files(
        self,
        audios: pd.DataFrame
    ):
        """
        Concatenate every audios from the same text

        Parameters
        ----------
        audios: pd.DataFrame
            DataFrame containing sentences and corresponding audio

        Returns
        -------
        audio_path: str
            Path to the concatenated audio
        """
        # Getting folder absolute path
        folder_abs_path = os.path.abspath(
            path=self.folder
        )
        # Creating filename and file path
        filename = str(self.id) + '.txt'
        file_path = os.path.join(
            folder_abs_path,
            filename
        )
        # Generating text file containing audios paths
        with open(file_path, 'w') as file:
            file.write("# " + filename + "\n")
            for index, row in audios.iterrows():
                file.write("file '{}'\n".format(row["audio_abs_path"]))
        # Concatenate all files in one
        complete_audio_name = str(self.id) + ".mp3"
        complete_audio_path = os.path.join(
            folder_abs_path,
            complete_audio_name
        )
        run = subprocess.run(
            args=["ffmpeg", "-f", "concat", "-safe", "0", "-i", str(file_path), "-c", "copy", str(complete_audio_path)]
        )
        # Checking if everything went well
        if run.returncode != 0:
            raise Exception("Audio generation failed")

    def __zipping(
        self
    ):
        """
        Zip all the files related to the text

        Returns
        -------
        files_zipped: str
            Absolute path the the zipped files
        """
        # Getting folder absolute path
        folder_abs_path = os.path.abspath(
            path=self.folder
        )
        # Getting files for the current text
        files = os.listdir(
            path=folder_abs_path
        )
        current_text_files = [os.path.join(folder_abs_path, file) for file in files if file.startswith(str(self.id))]
        # Zipping these files
        zip_path = os.path.join(folder_abs_path, str(self.id) + ".zip")
        with ZipFile(zip_path, 'w') as zip_object:
            for file in current_text_files:
                zip_object.write(
                    filename=file,
                    arcname=os.path.basename(file)
                )
        # Removing not zipped files
        for file in current_text_files:
            os.remove(file)
        return zip_path

    def generation(
        self
    ):
        """
        Generates all audios for the current text

        Returns
        -------
        zip_file_path: str
            Absolute path to the audios archive
        """
        # Splitting text into sentences
        sentences = self.__split_text()
        # TTS for each sentence
        df = self.__tts(sentences)
        # Creating audio file with all sentences
        self.__concat_files(df)
        # Zipping all files related to the current text
        zip_file_path = self.__zipping()
        return zip_file_path

if __name__ == "__main__":
    test = AudioGeneration(
        text="Ceci, enfin ce qu'il en reste, est une phrase! Je serais heureux que ça fonctionne.",
        id="testid",
        folder="fake"
    )
    test.generation()
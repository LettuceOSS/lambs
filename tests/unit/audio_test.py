from app.internal.audio import AudioGeneration
from zipfile import ZipFile
import pytest

test_folder = "test"
text_1_path = "../../data/input_1.txt"
text_2_path = "../../data/input_2.txt"

def test_audio_generation_1():
    """
    Testing audio generation
    """
    # Getting test data
    with open(text_1_path) as f:
        contents = f.readlines()
    text = " ".join(contents)
    # Generating audios
    test = AudioGeneration(
        text=text,
        id="1",
        folder=test_folder
    )
    zip_path = test.generation()
    # Verifying number of files
    with ZipFile(zip_path) as archive:
        count = len(archive.infolist())
    assert count == 6

def test_audio_generation_2():
    """
    Testing audio generation
    """
    # Getting test data
    with open(text_2_path) as f:
        contents = f.readlines()
    text = " ".join(contents)
    # Generating audios
    test = AudioGeneration(
        text=text,
        id="2",
        folder=test_folder
    )
    zip_path = test.generation()
    # Verifying number of files
    with ZipFile(zip_path) as archive:
        count = len(archive.infolist())
    assert count == 4


if __name__ == "__main__":
	pytest.main()
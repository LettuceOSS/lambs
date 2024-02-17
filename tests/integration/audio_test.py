import requests
from zipfile import ZipFile
import pytest

api_url = "http://localhost:80"
text_1_path = "../../data/input_1.txt"


def test_get_audio_route():
    """
    Testing API REST for creating and getting audio
    """
    # Getting test data
    with open(text_1_path) as f:
        contents = f.readlines()
    text = " ".join(contents)
    # Posting our text
    resp_1 = requests.post(
        url=api_url + "/audio/generate",
        json={
             "text": text
        }
    )
    assert resp_1.status_code == 200
    assert ("audio_id" in resp_1.json())
    # Getting generated file /audio/
    resp_2 = requests.get(
        url=api_url + "/audio/" + resp_1.json()["audio_id"]
    )
    file_path = resp_1.json()["audio_id"] + ".zip"
    open(file_path, "wb").write(resp_2.content)
    # Verifying number of files
    with ZipFile(file_path) as archive:
        count = len(archive.infolist())
    assert resp_2.status_code == 200
    assert count == 6


if __name__ == "__main__":
    pytest.main()

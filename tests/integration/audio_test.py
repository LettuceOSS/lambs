import requests
import json
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
    resp = requests.post(
        url=api_url + "/audio/generate",
        json={
             "text": text
        }
    )
    assert resp.status_code == 200
    assert ("audio_id" in resp.json()) == True

if __name__ == "__main__":
	pytest.main()
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from internal.audio import AudioGeneration
import hashlib
import os


# Global variables
AUDIO_FOLDER = "generated"


# Data Text Model
class DataText(BaseModel):
    text: str


app = FastAPI()


@app.post("/audio/generate")
def audio_generation(data: DataText):
    """
    Generate audio from the given text

    Parameters
    ----------
    data: DataText
        Body of the request containing required text

    Returns
    -------
    uid:
        UID of the generated archive
    """
    # ID Generation
    uid_gen = hashlib.sha256()
    uid_gen.update(data.text.encode())
    uid = uid_gen.hexdigest()
    # Audio Generation
    audio = AudioGeneration(
        text=data.text,
        id=uid,
        folder=AUDIO_FOLDER
    )
    audio.generation()
    # Return archive path
    return {"audio_id": uid}


@app.get("/audio/{audio_id}")
def audio_file(audio_id: str):
    """
    Get an archive containing audios

    Parameters
    ----------
    audio_id: str
        Unique identifier of the archive

    Returns
    -------
    file: FileResponse
        Archive containing audios
    """
    # Getting folder absolute path
    folder_abs_path = os.path.abspath(
        path=AUDIO_FOLDER
    )
    # Getting archive absolute path
    archive_abs_path = os.path.join(
        folder_abs_path,
        audio_id + ".zip"
    )
    # Returning archive
    return FileResponse(
        path=archive_abs_path
    )

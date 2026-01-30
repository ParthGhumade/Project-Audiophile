from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import subprocess
import uuid
import os
import shutil

shutil.copy("/etc/secrets/cookies.txt", "/tmp/cookies.txt")


app = FastAPI()

@app.get("/health")
def check_heath():
    return {"status":"ok"}

def clear_downloads():
    folder = "downloads"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")


@app.get("/url")
def get_url(url: str,name: str):

    clear_downloads()

   command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "m4a",
        "--no-playlist",
        "-o", file_path,
        url
    ],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        raise HTTPException(
            status_code=400,
            detail=result.stderr
        )

    
    return FileResponse(
        path=f"downloads/{name}.m4a",
        media_type="audio/mp4",
        filename=f"{name}.m4a"
    )









from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import subprocess
import uuid


app = FastAPI()

@app.get("/health")
def check_heath():
    return {"status":"ok"}

@app.get("/url")
def get_url(url: str,name: str):

    file_id=str(uuid.uuid4())
    file_path=f"downloads/{file_id}.m4a"

    result=subprocess.run(
    ["./yt-dlp", "--extractor-args","youtube:player_client=web_embedded","-f","bestaudio[ext=m4a]","-o", file_path, "--print","after_move:filepath", url],
        capture_output=True,
        text=True,
        check=True
    )

    return FileResponse(
        path=file_path,
        media_type="audio/mp4",
        filename=f"{name}.m4a"
    )

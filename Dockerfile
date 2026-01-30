FROM python:3.11-slim 
# os + python ver

RUN apt-get update && apt-get install -y ffmpeg curl ca-certificates && rm -rf /var/lib/apt/lists/*
# system binaries

RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && chmod a+rx /usr/local/bin/yt-dlp  
# yt-dlp binary

WORKDIR /app    
# set a permanant root dir

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# python dependancies

COPY main.py .
COPY downloads ./downloads
#copied the code from dir to dockerfile

EXPOSE 10000

CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","10000" ]

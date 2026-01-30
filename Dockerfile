FROM python:3.11-slim

# System deps + Node.js LTS
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates ffmpeg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# yt-dlp
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp \
    -o /usr/local/bin/yt-dlp && chmod +x /usr/local/bin/yt-dlp

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
RUN mkdir -p downloads && chmod 777 downloads

EXPOSE 10000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:10000/health || exit 1

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","10000"]

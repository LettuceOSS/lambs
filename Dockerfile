FROM python:3.10.13-slim
# Installing FFmpeg
SHELL ["/bin/bash", "-c"]
RUN apt update &&\
    apt install ffmpeg -y
# Copying files
WORKDIR /lambs
COPY . .
# Importing and activating Python environment
RUN python -m venv venv &&\
    source venv/bin/activate &&\
    pip install -r requirements.txt
WORKDIR /lambs/app
RUN chmod 777 run.sh
ENTRYPOINT [ "./run.sh" ]
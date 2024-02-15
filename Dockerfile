FROM continuumio/miniconda3:23.10.0-1
# Installing FFmpeg
SHELL ["/bin/bash", "--login", "-c"]
RUN apt update &&\
    apt install ffmpeg -y
# Copying files
COPY . .
# Importing and activating Python environment
RUN conda init bash &&\
    conda env create -f environment.yml
WORKDIR /app
RUN chmod 777 run.sh
ENTRYPOINT [ "./run.sh" ]
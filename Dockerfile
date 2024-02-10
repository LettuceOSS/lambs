FROM continuumio/miniconda3:23.10.0-1
# Copying files
COPY . .
# Installing, importing and activating env
SHELL ["/bin/bash", "--login", "-c"]
RUN apt update &&\
    apt install ffmpeg -y
RUN conda init bash &&\
    conda env create -f environment.yml
RUN conda activate lambs
# Lettuce Lambs
## Description

Convert text into audio using a Rest API.

## Installation

Build the container's image:

```console
docker build -t lambs:mvp .
```

Run the container based on this image:
```console
docker run --name lambs -p 8080:80 lambs:mvp
```

## Usage example

Send the text:
```console
curl -d '{"text":"Ceci est une phrase test"}' -H "Content-Type: application/json" -X POST http://localhost:8080/audio/generate
```

It returns the audio id in JSON:
```text
{"audio_id":"814b8d19d8b6946820c67869a82afba07f205a542685ae5b4eb9352c0fb30665"}
```

Get the audio with the audio id:
```console
curl -X GET http://localhost:8080/audio/814b8d19d8b6946820c67869a82afba07f205a542685ae5b4eb9352c0fb30665 -o output.zip
```

## Documentation

Go to http://localhost:8080/docs.

## Roadmap

- [ ] Switching from Conda to PIP
- [ ] Create a Continuous Delivery (CD) pipeline
- [ ] Option to get only concatenated audio
- [ ] Adding code coverage to Continuous Integration (CI) pipeline
- [ ] Adding option to save audios in S3
- [ ] Add authentification system
# Lambs

Command line to export the environment
```
conda env export --no-builds | grep -v "^prefix: " > environment.yml
```

Create docker image
```
docker build -t lambs:test .
```

Run docker container
```
docker run --name lambs --rm -p 8080:80 lambs:test
```

conda activate lambs
cd ../tests
pytest
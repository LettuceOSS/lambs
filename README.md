# Lambs

Command line to export the environment
```
conda env export --no-builds | grep -v "^prefix: " > environment.yml
```
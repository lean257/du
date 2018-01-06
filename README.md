### This is a script built to reimplement the disk usage (du) command in python

### Commands included:

Get number of blocks allocated on disk of current directory, similar to du . 

```
./du.py .
./du.py -a .
```

Get file size in KB, MB, GB

```
./du.py -k .
./du.py -m .
./du.py -g .
```

Get apparent size of files, similar to du --apparent_size in linux

```
./du.py -e .
```

### Run tests

```
python dutest.py

```

### WIP
1. ability to list only files with specific criteria like du -*
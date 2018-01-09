### This is a script built to reimplement a subset the disk usage (du) command in python

### Set up

```
chmod +x ./du.py
```

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

For help

```
./du.py -h
```

### Run tests

```
python dutest.py
```

### WIP
1. ability to list only files with specific criteria like du -*
2. sort file by size
3. accomodate 2 files
4. du --max-depth=1
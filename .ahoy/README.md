# PyDKAN Ahoy setup

## Installation

+ Install docker (See https://docs.docker.com/engine/installation/)
+ Install ahoy (See https://github.com/devinci-code/ahoy#installation)
+ Run the following:

```
$ ahoy docker build
```

## Usage

### Prompt into a container with the dev environment

```
ahoy api prompt
```

### Prompt into an ipython console:

```
ahoy api python
```

### Run a script

```
ahoy api python examples/list_nodes.py
```

### Run the testsuite

````
ahoy api tests
````

### Rebuild the image

From time to time you'll need to rebuild the docker image. For instance, if you add a requirement to the requirements.txt file and you'll need it installed. Yoy can do that by:

```
ahoy docker build --no-cache
```

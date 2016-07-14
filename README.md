# PyDKAN

This is a python client to interface with the [dkan_dataset_rest_api](https://github.com/NuCivic/dkan_dataset/tree/7.x-1.x/modules/dkan_dataset_rest_api) web service.

## Installation

### As a Library

```bash
# To install the latest of the latest
$ pip install git+git://github.com/NuCivic/pydkan.git@master#egg=pydkan
# To install a release
$ pip install git+git://github.com/NuCivic/pydkan.git@0.3#egg=pydkan
```

### For development with docker and ahoy

+ Install docker
+ Install ahoy (See https://github.com/devinci-code/ahoy#installation)
+ Run the following:

```
$ ahoy docker build
```

That's it.

## Usage

### As a library

Check the examples folder, there are snippets for pretty much everything you can do with this library.

### Docker + Ahoy setup

#### Prompt into a container with the dev environment

```
ahoy api prompt
```

#### Prompt into an ipython console:

```
ahoy api python
```

#### Run a script

```
ahoy api python examples/list_nodes.py
```

#### Run the testsuite

````
ahoy api tests
````

#### Rebuild the image

From time to time you'll need to rebuild the docker image. For instance, if you add a requirement to the requirements.txt file and you'll need it installed. Yoy can do that by:

```
ahoy docker build --no-cache
```

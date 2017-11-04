# NLP with Python for Facebook Mining
## Introduction
In this review I present a non-exhaustive list tools for analyzing a text corpus using Python. I will use state-of-the-art NLP techniques to mine Facebook user's text from their posts. 

## Requirements (tools and libs)
* The code uses __python3__, it can be easily backported to python2 if needed, but that's up to you.
* This notebook can be easily viewed here in GitHub or [nbviewer](https://nbviewer.jupyter.org/). The preferred way to run the code is to clone the repository and install [__Jupyter__](https://jupyter.org/). However If you want to be able to recompute some parts without using your own jupyter, you can try the awesome [Binder](https://mybinder.org/) (currently in beta), although it won't work for extra modules such as NLPs libs.
(Optional: Install the [__Spyder IDE__](https://github.com/spyder-ide/spyder) which provides IPython integration).
* NLP libraries: mainly only [__spaCy__](https://spacy.io/) and [__gensim__](https://radimrehurek.com/gensim/). In the future maybe try Stanford's [__CoreNLP__](https://stanfordnlp.github.io/CoreNLP/). I will avoid using mainstream [__NLTK__](www.nltk.org) in this starting phase.* Standard Python scientific stack is needed. You can install it through the [conda](https://conda.io/) package manager, through your package manager distribution, or using __pip__, Python's own package manager.

Modules used utilize [__Pandas__](http://pandas.pydata.org/) for data analysis and naive visualization, [__scikit-learn__](http://scikit-learn.org/) for comparative machine learning.

## Datasets
As a team member, I'm proud to say that the datasets are the result of a collective effort of the [__Facebook Tracking Exposed__](https://facebook.tracking.exposed/) project and can be easily retrieved from the GitHub [repo](https://github.com/tracking-exposed/experiments-data/).
If you are thinking to go beyond testing the generously provided models, and you want to learn how to make bots to crawl Facebook  yourself and build your own datasets, refer to the main fbtrex project [backend](https://github.com/tracking-exposed/facebook) (UPDATE: I'm currently working on fbtrex guide for wannabe researchers).
At the moment fbtrex allows one to crawl public posts from single users thus exposing Facebook's filter bubble. To have a more comprehensive analysis it's useful to compare these bubbles not only between themselves, but also with all the posts of a public page. This feature is not currently implemented (we are trying) although the posts of a single page can be retrieved via Facebook's own Graph API (you will actually need a developer token to do this).

## Setting up
While working with NLP it's often convenient to work with __virtual environments__. Some of the tools provided are frequently upgraded with new functionalities, while others are subject to model and architecture changes. Having different toolchains allows one to compare the different modules and find the best tools fit for the nlp tasks. 
If you already know what is right for your job you can install everything in the global Python without using virtual enviroments, but remember that Python provides native sandbox creation and management thus allowing to keep a clean global environment while still having a bleeding edge development branch in production.

### Virtual Environment
Python 3.3+ comes with a module called [__venv__](https://docs.python.org/3/library/venv.html). For applications that require an older version of Python, [virtualenv](https://virtualenv.pypa.io/en/stable/) is to be used.
```
#Create a nlp virtual environment for efficient sandboxing
python -m venv nlp
```
Running this command creates a nlp directory in this nb directory and places a pyvenv.cfg file in it with a home key pointing to the Python installation from which the command was run. It also creates a bin subdirectory containing a copy of the python binary. It also creates an (initially empty) lib/pythonX.Y/site-packages subdirectory, where pip installed modules will end up.
```
#Activate nlp venv
source nlp/bin/activate
```
__Note__: You don't specifically need to activate an environment; activation just prepends the virtual environment's binary directory to your path, so that "python" invokes the virtual environment's Python interpreter and you can run installed scripts without having to use their full path. However, all scripts installed in a virtual environment should be runnable without activating it, and run with the virtual environment's Python automatically.

__Note2__: If you are using Spyder IDE, remember to change Python interpreter's path: *Tools -> Preferences -> Python interpreter-> ~/nlp/bin/python3*

### Install core deps
Most of these tools can be installed globally via your linux distribution's package manager. If you are working with the nlp virtual environment as suggested, you can now use pip to install the modules. 
```
#Install minimal scientific python stack
pip install pandas && pip install scikit-learn
```
__Note__: If you already have installed some package via pip you can upgrade to latest version with "pip install -U ModelName"

### Install NLP modules
Let's begin our journey using only __spaCy__ for data analysis. Later on we will also use gensim to provided unsupervised training for our model. 

I suggest to try the [__alpha__](http://alpha.spacy.io/) version, which is provided via the [__spacy-nightly__](https://pypi.python.org/pypi/spacy-nightly) module. Basic and API documentation can be found in the alpha spaCy [subdomain](https://alpha.spacy.io/usage/). For the soon-legacy documentation refer to [main domain](https://spacy.io/docs/usage/).
```
#Install the alpha spacy2.0 instead of 1.9
pip install spacy-nightly
```
Once installed, we can move on to download the available spaCy [language __models__](https://alpha.spacy.io/models/). You can also build your own [models](https://alpha.spacy.io/api/#nn-models) using spaCy's integrated machine learning library [__Thinc__](https://github.com/explosion/thinc). 

I reckon that the provided models work fine for my purposes although I'd prefer having better integration with different languages such as Spanish and Italian; if you have time to spare please contribute to [language support](https://spacy.io/docs/usage/adding-languages).
```
#Download core English model
spacy download en_core_web_sm
#Download Spanish model
spacy download es_core_web_sm
```

### Jupyter
To really appreciate this work you will have to try it out yourself. The Jupyter project provides an IPython console in which you can run code on your machine. If you are in a virtual env you will have to rebuild the IPython kernel after you installed all the core deps and modules:
```
#Activate nlp venv
source nlp/bin/activate
#Create new customized kernel
python -m ipykernel install --user --name=nlp
```
To use this kernel launch Jupyter in the traditional way: *jupyter-notebook nlp*. A new local webpage will open in your browser. From the navigation bar pick *Kernel -> Change Kernel -> nlp*.  

## Contribute
There are many ways of contributing to NLP analysis on Facebook! You can help the fbtrex project to build new datasets and write a notebook about it. If you speak a different language than English, please consider improving SpaCy's language support. 

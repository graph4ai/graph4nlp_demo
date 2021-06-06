# Deep Learning on Graphs for Natural Language Processing Demo


The repository contains code examples for [DLG4NLP](https://dlg4nlp.github.io) tutorials at [NAACL 2021](https://2021.naacl.org). 

Slides can be downloaded from [NAACL 2021 version](). 


## Get Started

You will need to install our [graph4nlp library](https://github.com/graph4ai/graph4nlp) in order to run the demo code. Please follow the following environment setup instructinos. Please also refer to the *graph4nlp* repository page for more details on how to use the library.


### Environment setup

1. Create virtual environment
```
conda create --name graph4nlp python=3.7
conda activate graph4nlp
```

2. Install [graph4nlp](https://github.com/graph4ai/graph4nlp) library
- Clone the github repo
```
git clone -b stable https://github.com/graph4ai/graph4nlp.git
cd graph4nlp
```
- Then run `./configure` (or `./configure.bat` if you are using Windows 10) to config your installation. The configuration program will ask you to specify your CUDA version. If you do not have a GPU, please choose 'cpu'.
```
./configure
```
- Finally, install the package
```
python setup.py install
```

3. Set up StanfordCoreNLP (for static graph construction only, unnecessary for this demo because preprocessed data is provided)
- Download [StanfordCoreNLP](https://stanfordnlp.github.io/CoreNLP/)
- Go to the root folder and start the server
```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```


### Start Jupyter notebook and run the demo

After complete the above steps, you can start the jupyter notebook server to run the demo:
```
cd graph4nlp_demo/NAACL2021_demo
jupyter notebook
```


## Additional Resources:

* [DLG4NLP survey]()
* [DLG4NLP literature repo](https://github.com/graph4ai/graph4nlp_literature)

<!-- ### Citation: -->


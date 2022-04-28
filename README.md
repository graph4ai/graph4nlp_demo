# Deep Learning on Graphs for Natural Language Processing Demo


The repository contains code examples for [DLG4NLP](https://dlg4nlp.github.io) tutorials at [NAACL 2021](https://2021.naacl.org), [SIGIR 2021](https://sigir.org/sigir2021/), [KDD 2021](https://www.kdd.org/kdd2021/), [IJCAI 2021](http://ijcai-21.org), [AAAI 2022](https://aaai.org/Conferences/AAAI-22/) and [TheWebConf 2022](https://www2022.thewebconf.org/conference-schedule/).

Slides can be downloaded from [here](https://dlg4nlp.github.io/tutorials.html).


## Get Started

You will need to install our [graph4nlp library](https://github.com/graph4ai/graph4nlp) in order to run the demo code. Please follow the following environment setup instructions. Please also refer to the [*graph4nlp* repository page](https://github.com/graph4ai/graph4nlp#readme) for more details on how to use the library.


### Environment setup

1. Create virtual environment
```
conda create --name graph4nlp python=3.8
conda activate graph4nlp
```

2. Install [graph4nlp](https://github.com/graph4ai/graph4nlp) library
- Clone the github repo
```
git clone -b [branch_version] https://github.com/graph4ai/graph4nlp.git
cd graph4nlp
```
Please choose the branch version corresponding to the demo version as shown in the table below.

| demo version | library branch version |  
| ---- | ---- |  
| DLG4NLP@ICLR 2022 | v0.5.5 |
| TheWebConf 2022 | v0.5.5 |
| AAAI 2022 | v0.5.5 |  
| CLIQ-ai 2021 | stable_nov2021b |  
| IJCAI 2021 | stable_202108 |  
| KDD 2021 | stable_202108 |  
| SIGIR 2021 | stable |  
| NAACL 2021 | stable |  


- Then run `./configure` (or `./configure.bat` if you are using Windows 10) to config your installation. The configuration program will ask you to specify your CUDA version. If you do not have a GPU, please choose 'cpu'.
```
./configure
```
- Finally, install the package
```
python setup.py install
```
3. Install other packages
```
pip install torchtext
pip install notebook
```

4. Set up StanfordCoreNLP (for static graph construction only, unnecessary for this demo because preprocessed data is provided)
- Download [StanfordCoreNLP](https://stanfordnlp.github.io/CoreNLP/)
- Go to the root folder and start the server
```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```


### Start Jupyter notebook and run the demo

After complete the above steps, you can start the jupyter notebook server to run the demo:
```
cd graph4nlp_demo/XYZ
jupyter notebook
```
Note that you will need to change `XYZ` to the specific folder name.

## Additional Resources:

* [Graph4NLP library](https://github.com/graph4ai/graph4nlp)
* [DLG4NLP website](https://dlg4nlp.github.io/index.html)
* [DLG4NLP survey](https://arxiv.org/pdf/2106.06090)
* [DLG4NLP literature repo](https://github.com/graph4ai/graph4nlp_literature)

<!-- ### Citation: -->


# Process Mining - 6.Semester



## Introduction to Alpha Miner

The α-algorithm or α-miner is an algorithm used in process mining, aimed at reconstructing causality from a set of sequences of events. It was first put forward by van der Aalst, Weijters and Măruşter. The goal of Alpha miner is to convert the event log into a workflow-net based on the relations between various activities in the event log. An event log is a multi-set of traces, and a trace is a sequence of activity names. 
Link: **https://en.wikipedia.org/wiki/Alpha_algorithm**

## Connect to the Lehrer Server

## Webservice display

## Technologies

- [ ] Python 3.10
- [ ] Flask
- [ ] Bootstrap 4
- [ ] Javascript
- [ ] css
- [ ] Graphviz
- [ ] Minidom

## project Structure
process-mining 

│   handle_xes.py <br />
│   alphaminer.py <br />
│   alphaminer_tests.py <br />
│   main.py <br />
│   README.md  <br />
│   requirements.txt<br />
│   <br />
└───static <br />
│   │   backgroud.jpeg<br />
│   │   munich.png<br />
│   │   somefile.png<br />
│   │   ...<br />
│   <br />
└───templates <br />
│   │   contact.html <br />
│   │   about.html <br />
│   │   index.html <br />
│   <br />
└───upload _folder <br />
│   <br />
└───datasets <br />
│   │   L1.xes <br />
│   │   L2.xes <br />
│   │   L3.xes <br />
│   │   ... <br />


## Installation
**PIP3 install packages, e.g Flask**
```
pip3 install flask
```
**virtual environment**
```
python3 -m venv tutorial-env
source tutorial-env/bin/activate
```
**requirements.txt**
```
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```

## Contact

email address: chunqing.hao@tum.de





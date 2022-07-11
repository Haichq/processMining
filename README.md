# Process Mining - 6.Semester



## Introduction to Alpha Miner

The α-algorithm or α-miner is an algorithm used in process mining, aimed at reconstructing causality from a set of sequences of events. It was first put forward by van der Aalst, Weijters and Măruşter.[1] The goal of Alpha miner is to convert the event log into a workflow-net based on the relations between various activities in the event log. An event log is a multi-set of traces, and a trace is a sequence of activity names. 
Link: **https://en.wikipedia.org/wiki/Alpha_algorithm**

## Connect to the Lehrer Server

- [ ] **Connect to lehre server via ssh:**
```
ssh ge35tuy@lehre.bpm.in.tum.de
```
- [ ] **Passphrase for key:**
```
rwVYNEH4BEPIkEBnLvNn8QHD_DEmJp0gm
```
- [ ] **into the folder**
```
ls
```
```
cd pm_internship
```
- [ ] **clone gitlab project:**
```
git clone https://gitlab.lrz.de/00000000014A5ED1/process-mining-6.semester.git
```
- [ ] **Then you should execute the commands as following:**
```
python3 -m venv tutorial-env
source tutorial-env/bin/activate
ls
cd process-mining-6.semester
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
pip3 install flask
pip3 install graphviz
pip3 install numpy
pip3 install pydot
```
- [ ] **provide environment variable:**
```
export FLASK_APP=main
```
- [ ] **run the project:**
```
flask run --host=:: --port=9012
```
- [ ] **access the webapp url:**
```
https://lehre.bpm.in.tum.de/ports/9012/index
```
- [ ] **quit the app:**
```
CTRL+C
```
## Webservice display

If you want to upload a new xes file, you need to go back to the page which its url **https://lehre.bpm.in.tum.de/ports/9012/index** is.

You should always get back to the page first, if you want to use another fuctionalities, such as **About** and **Contact Me**.

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

email address: hai.chunqing@gmail.com





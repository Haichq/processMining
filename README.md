# Process Mining - 6.Semester



## Introduction about Alpha Miner

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

- [ ] **clone gitlab project:**
```
git clone https://gitlab.lrz.de/00000000014A5ED1/process-mining-6.semester.git
```
- [ ] **Then you should execute the commands as following:**
```
ls
cd pm_internship
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
- [ ] **access the url:**
```
https://lehre.bpm.in.tum.de/ports/9012/index
```
- [ ] **quit the app:**
```
CTRL+C
```

## Technologies

- [ ] Python 3.10
- [ ] Flask
- [ ] Bootstrap 4
- [ ] Javascript
- [ ] css
- [ ] Graphviz
- [ ] Minidom


## Installation
**Flask**
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
## Webservice display

If you want to upload a new xes file, you need to go back to the page which its url ** https://lehre.bpm.in.tum.de/ports/9012/index ** is.

You should always get back to the page first, if you want to use another fuctionalities, such as **About** and **Contact Me**.

## project Structure
process-mining 

│   handle_xes.py

│   handle_xes_test.py

│   alphaminer.py

│   alphaminer_tests.py
│   main.py
│   README.md  
│   requirements.txt
│
└───static
│   │   backgroud.jpeg
│   │   munich.png
│   │   somefile.png
│   │   ...
│
└───templates 
│   │   contact.html
│   │   about.html
│   │   index.html
│  
└───upload _folder
│   │   L1.xes
│   │   L2.xes
│   │   L3.xes
│   │   ...
│ 
└───datasets
│   │   L1.xes
│   │   L2.xes
│   │   L3.xes
│   │   ...


# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!).  Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

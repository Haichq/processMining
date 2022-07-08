import os
# from bs4 import BeautifulSoup
from xml.dom.minidom import parse


# dom1 = parse('datasets/billinstances.xes')

# traces = dom1.getElementsByTagName("trace")
# L = []
# for trace in traces:
#  event_list = []
#  events = trace.getElementsByTagName("event")
#  for event in events:
#   event_list.append(event.childNodes[5].attributes["value"].value)

#  L.append(event_list)
# print(L)

#
dom1 = parse('datasets/L1.xes')

traces = dom1.getElementsByTagName("trace")
L = []
for trace in traces:
    event_list = []
    events = trace.getElementsByTagName("event")
    for event in events:
        for n in event.childNodes:
            try:
                if n.attributes['key'].value == "concept:name":
                    event_list.append(n.attributes["value"].value)
            except:
                pass

    L.append(event_list)
print(L)
print("handle_xes")

def handle_test(filename):
    dom1 = parse(filename)

    traces = dom1.getElementsByTagName("trace")
    L = []
    for trace in traces:
        event_list = []
        events = trace.getElementsByTagName("event")
        for event in events:
            for n in event.childNodes:
                try:
                    if n.attributes['key'].value == "concept:name":
                        event_list.append(n.attributes["value"].value)
                except:
                    pass


        L.append(event_list)
    print(L)
    print("handle_test")
    return L
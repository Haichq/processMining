import os
from xml.dom.minidom import parse

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
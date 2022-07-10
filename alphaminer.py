from __future__ import annotations
import json
from logging import setLoggerClass
from pdb import pm
from typing import Any, Tuple, Union
from graphviz.backend.mixins import View
from graphviz.dot import comment, node
from numpy.lib.index_tricks import diag_indices
import pm4py
import os
from graphviz import Digraph
from handle_xes import handle_test
import pydot

#frozenset : order-irrelevant
#powerset at the beginning is an empty set
def powerset(TL: set[str]) -> set[frozenset[str]]:
    powerset: set[frozenset[str]] = {frozenset()}
    #find subsets from an empty set to other subsets which length is from 1 to N 
    for set_len in range(1, len(TL) + 1):
        # Find the set with set_len - 1 elements from the entire powerset
        for s in {s for s in powerset if len(s) == set_len - 1}:
            #Elements in TL, but not in S
            for t in TL - s: 
                # add each appropriate element to s, 
                # then we cen get a new set with lengeh set_len,
                # then we put the new set into the entire powerset. 
                powerset.add(s.union({t}))
    return powerset


# L = ["abcd", "acbd"]
#Step 1
def test_data(L):
    TL = {t for sig in L for t in sig}
    print("TL = " )
    print(TL)

    #Assuming that the default from the start to the end is “#”
    mat = {(t1, t2): "#" for t1 in TL for t2 in TL}
    for sig in L:
        for a, b in zip(sig[:-1], sig[1:]): 
            # e.g. L = [<a,b,c,d>,<a,c,b,d>]
            #--> ab,bc, cd, ac,cb,bd
            if mat[(a, b)] == "#":
                if a == b:         
                    mat[(a, b)] = "#"  # token
                    # L7
                    #mat[(a, b)] = "|"
                else:
                    mat[(a, b)] = ">"
                    mat[(b, a)] = "<"
            elif mat[(a, b)] == "<":
                mat[(a, b)] = "|"
                mat[(b, a)] = "|"

    TI = {sig[0] for sig in L}
    # print(TI)
    TO = {sig[-1] for sig in L}
    # print(TO)

    XL = {
        (A, B)
        for A in powerset(TL)
        for B in powerset(TL)
        if len(A) != 0
        and len(B) != 0
        and all(mat[(a, b)] == ">" for a in A for b in B)
        and all(mat[(a1, a2)] == "#" for a1 in A for a2 in A)
        and all(mat[(b1, b2)] == "#" for b1 in B for b2 in B)
    }

    YL = {
        (A, B)
        for (A, B) in XL
        
        #There is no case of being included, AB will stay and will not be replaced
        #by (A_,B_)

        if not any(
            A.issubset(A_) and B.issubset(B_) and (A is not A_ or B is not B_)
            for (A_, B_) in XL
        )
    }

    PL = {(A, B) for (A, B) in YL}
    PL.update({"iL", "oL"})

    FL = {(a, (A, B)) for (A, B) in YL for a in A}
    FL.update({((A, B), b) for (A, B) in YL for b in B})
    FL.update({("iL", t) for t in TI}.union({(t, "oL") for t in TO}))


    def toSet(A: Any) -> Any:
        #if A is a frozenset, then -> set, 
        # else A 
        return set(A) if isinstance(A, frozenset) else A


    # print("XL = ")
    for A, B in XL:
        print("\t", (toSet(A), toSet(B)))
        

    # print("YL = ")
    for A, B in YL:
        print("\t", (toSet(A), toSet(B)))


    return TI, TO, TL, YL,XL

i = 0
def circle_nodes():
    global i 
    i +=1
    return str(i)

def generate_graph(TI, TO, TL, YL, XL):
     #Petri Net
    #set with first and last elements 
    s_TITO = TI|TO
    #set without first and last element 
    s_NoTITO = TL - s_TITO

    g = Digraph(comment='petri-net',format='png')
    #iL node
    g.node('iL',shape = 'circle') 
    #first element
    for first in TI:
        g.node(name = first,shape = 'square') 
    #the middle part
    for s_no in s_NoTITO:
        g.node(name = s_no,shape='square')
    #last element
    for last in TO:
        g.node(name = last,shape = 'square')
    #OL node
    g.node('oL',shape = 'doublecircle')

    for set_pairs in YL:
        (set_first,set_second) = set_pairs
        name1 = circle_nodes()
        g.node(name=name1,label='',shape = 'circle') 

        for set_name in set_second:
            g.edge(tail_name=name1,head_name=set_name)
        for set_name in set_first:
            g.edge(tail_name=set_name,head_name= name1)

    g.edges(('iL', first) for first in TI)
    g.edges((last,'oL') for last in TO)

    # g.view()
    g.save("xes.dot", directory="static")
    (graph,) = pydot.graph_from_dot_file('./static/xes.dot')
    graph.write_png('./static/somefile.png')
    return "somefile.png"

if __name__ == '__main__':
    # test_data(L)
    ll = handle_test()
    test_data(ll)
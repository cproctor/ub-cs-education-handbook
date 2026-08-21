---
title: UB Teach track
---

## UB Teach Track

```{.graphviz caption="The UB Teach Track"}
digraph G {
  rank="max"
  rankdir="LR"
  bgcolor="transparent"
  graph [fontname="Helvetica", nodesep=0.35]
  node [fontname="Helvetica", fontsize=11, shape="box", style="rounded,filled", penwidth=0, margin="0.18,0.1"]
  edge [color="#9aa5b1", arrowsize=0.75, penwidth=1.3]

  undergrad [label="Undergraduate UB student\n majoring in CSE" width=3 fillcolor="#e8eef7" fontcolor="#1d3f6e"]
  ubteach [label="UB Teach" width=2.4 fillcolor="#1d5fa8" fontcolor="white"]
  initial [label="Initial coursework\n& residency" width=2.4 fillcolor="#1d5fa8" fontcolor="white"]
  professional [label="Professional coursework" width=2.4 fillcolor="#1d5fa8" fontcolor="white"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n Qualified to teach CS in NY" width=5 fillcolor="#1f7a4d" fontcolor="white"]

  undergrad -> ubteach -> initial -> professional -> pro_cert_outcome;

  subgraph programs {
    rank="same"
    ubteach
    initial
    professional
  }
}
```

UB Teach CS will be a combined bachelor's degree, EdM, initial, and professional certification, 
all completed in five years. The first three years are focused on CSE coursework; the last two years are 
focused on teacher preparation coursework. The final year of the program is a yearlong residency placement
in a school.

**The UB Teach Track in CS is not yet available**. Prospective students interested in UB Teach CS are 
invited to contact Dr. Chris Proctor ([chrisp@buffalo.edu](mailto:chrisp@buffalo.edu)) for the latest 
updates on the program. General information about UB Teach is available at the 
[UB Teach program website](http://ed.buffalo.edu/academics/ub-teach.html).

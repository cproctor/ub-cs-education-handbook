---
title: UB Teach track
---

## UB Teach Track

```{.graphviz}
digraph G {
  rank="max"
  rankdir="LR"

  undergrad [label="Undergraduate UB student\n majoring in CSE" shape="box"]
  ubteach [label="UB Teach"]
  initial [label="Initial coursework"]
  professional [label="Professional coursework"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n Qualified to teach CS in NY" shape="box"]

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
all completed in five years.

**The UB Teach Track in CS is not yet available**. Prospective students interested in UB Teach CS are 
invited to contact Dr. Chris Proctor ([chrisp@buffalo.edu](mailto:chrisp@buffalo.edu)) for the latest 
updates on the program. General information about UB Teach is available at the 
[UB Teach program website](http://ed.buffalo.edu/academics/ub-teach.html).

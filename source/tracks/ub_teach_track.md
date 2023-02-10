---
title: UB Teach track
---

## UB Teach Track

```{.graphviz caption="The UB Teach Track"}
digraph G {
  rank="max"
  rankdir="LR"

  undergrad [label="Undergraduate UB student\n majoring in CSE" shape="box"]
  ubteach [label="UB Teach"]
  initial [label="Initial coursework\n& residency"]
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
all completed in five years. The first three years are focused on CSE coursework; the last two years are 
focused on teacher preparation coursework. The final year of the program is a yearlong residency placement
in a school.

**The UB Teach Track in CS is not yet available**. Prospective students interested in UB Teach CS are 
invited to contact Dr. Chris Proctor ([chrisp@buffalo.edu](mailto:chrisp@buffalo.edu)) for the latest 
updates on the program. General information about UB Teach is available at the 
[UB Teach program website](http://ed.buffalo.edu/academics/ub-teach.html).

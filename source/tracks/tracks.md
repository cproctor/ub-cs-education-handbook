---
title: Tracks
---

# Tracks

The UB Computer Science Education Program offers several tracks designed to meet the 
needs of different students. If the diagram below has a path from where you are to where you 
want to be, we have a track for you.

```{.graphviz caption="All tracks of the CS Education Program"}
digraph G {
  rank="max"
  rankdir="LR"
  bgcolor="transparent"
  graph [fontname="Helvetica", nodesep=0.35, ransep=0.5]
  node [fontname="Helvetica", fontsize=11, shape="box", style="rounded,filled", penwidth=0, margin="0.18,0.1"]
  edge [color="#9aa5b1", arrowsize=0.75, penwidth=1.3]

  node [width=3, fillcolor="#e8eef7", fontcolor="#1d3f6e"]

  undergrad [label="Undergraduate UB student\n majoring in CSE"]
  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework"]
  init_cert [label="Teachers holding an initial\n or professional teaching\n certificate in any subject"]
  other_cert [label="Teachers holding a certificate,\nor preservice teachers,\nin another discipline"]

  node [width=2.4, fillcolor="#1d5fa8", fontcolor="white"]

  ubteach [label="UB Teach"]
  initial [label="Initial coursework\n& residency"]
  professional [label="Professional\ncoursework"]
  advanced_certificate [label="Advanced certificate\n coursework"]

  node [width=5, fillcolor="#1f7a4d", fontcolor="white"]

  init_cert_outcome [label="Certificate of Advanced Study\n Recommendation for NYS Initial Certificate in CS\n Qualified to teach CS in NY for 5 years"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n(or Additional Certificate in CS, if initial\ncertificate was in another subject)\n Qualified to teach CS in NY"]
  adv_cert_outcome [label="Certificate of Advanced Study\n Qualified to teach CS in NY"]

  undergrad -> ubteach -> initial;
  cse_majors -> initial -> init_cert_outcome;
  initial -> professional;
  init_cert -> professional -> pro_cert_outcome;
  other_cert -> advanced_certificate -> adv_cert_outcome;
  pro_cert_outcome -> adv_cert_outcome [style=invis];
  
  subgraph starts {
    rank="same"
    undergrad
    cse_majors
    init_cert
    other_cert
  }
  subgraph programs {
    rank="same"
    ubteach
    initial
    professional
    advanced_certificate
  }
  subgraph ends {
    rank="same"
    init_cert_outcome
    pro_cert_outcome
    adv_cert_outcome
  }
}
```

For those with an undergraduate major in computer science (or meeting coursework prerequisites), 
the [Initial Certificate Track](#initial-certificate-track) provides a Certificate of Advanced Study and 
a recommendation for a NYS Initial Certification in CS. This track requires 36 credit hours.
The Initial Certificate track requires 18 units of coursework, 
followed by a year-long residency in which teacher candidates are placed in classrooms 
under the supervision of a cooperating teacher. 

The [Professional Certificate Track](#professional-certificate-track) is available to teachers 
holding an initial or professional teaching certificate in any subject. Graduates earn an EdM degree 
and a recommendation for NYS Professional Certification in CS (or, for teachers whose initial 
certificate was in a different subject, an Additional Certification in CS). This track requires 
30 credit hours, and can be completed in one year of full-time study.

The [Initial/Professional Certificate Track](#initial-professional-certificate-track) 
combines initial and professional certification and requires fewer credit hours than completing 
the programs separately. This track requires 48 credit hours and is typically completed in two years of full-time
coursework. The second year is a residency in which teacher candidates are placed in classrooms
under the supervision of a cooperating teacher.

[UBTeach](#ub-teach-track) is a combined bachelor's degree, EdM, 
initial, and professional certification, completed in five years.
(UBTeach is not yet available for CS education.)

For teachers holding a certificate in another discipline, or for preservice teachers working toward 
certification in another discipline, the 
[Advanced Certificate Track for In-Service Teachers](#advanced-certificate-track-for-in-service-teachers) 
provides qualification to teach CS in New York public schools.  This track requires 15 credit hours, 
and is designed for working professionals to complete at their own pace.


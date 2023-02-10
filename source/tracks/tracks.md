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

  node [width=3]

  undergrad [label="Undergraduate UB student\n majoring in CSE" shape="box"]
  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework" shape="box"]
  init_cert [label="Teachers holding\n initial certificate in CS" shape="box"]
  other_cert [label="Teachers holding a certificate\n in another discipline" shape="box"]
  ubteach [label="UB Teach"]
  initial [label="Initial coursework"]
  professional [label="Professional coursework"]
  advanced_certificate [label="Advanced certificate\n coursework"]

  node [width=5]

  init_cert_outcome [label="Certificate of Advanced Study\n Recommendation for NYS Initial Certificate in CS\n Qualified to teach CS in NY for 5 years" shape="box"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n Qualified to teach CS in NY" shape="box"]
  adv_cert_outcome [label="Certificate of Advanced Study\n Qualified to teach CS in NY" shape="box"]
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
a recommendation for a NYS Initial Certification in CS. Coursework for the Initial certification takes 
about one year. The [Professional Certificate Track](#professional-certificate-track) 
requires an additional year of coursework. Graduates earn an EdM degree and recommendation for 
a NYS Professional Certification in CS.
The [Initial/Professional Certificate Track](#initial-professional-certificate-track) 
combines initial and professional certification and requires fewer credit hours than completing 
the programs separately. [UBTeach](#ub-teach-track) is a combined bachelor's degree, EdM, 
initial, and professional certification, completed in five years.

For teachers holding a certificate in another discipline, the 
[Advanced Certificate Track for In-Service Teachers](#advanced-certificate-track-for-in-service-teachers) provides qualification to teach CS in New York public schools. 

Because the CS teaching certificate is still fairly new, most teachers currently teaching CS in New York are
certified in other disciplines. Starting September 1, 2023, everyone teaching CS in New York will be 
required to hold a CS teaching certificate or a 
[CS Statement of Continuing Eligibility](http://www.highered.nysed.gov/tcert/certificate/computer-sci-soce.html) 
(SOCE) which is valid for ten years. If you have been teaching CS in New York with certification in another 
discipline, you should either enroll in the [Advanced Certificate Track](#advanced-certificate-track) or you should apply for the 
SOCE before September 1, 2023.


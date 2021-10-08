---
title: Initial/Professional Certificate Track
---

## Initial/Professional Certificate Track

```{.graphviz caption="The Initial/Professional Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"

  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework"]
  initial [label="Initial coursework" shape="box"]
  professional [label="Professional coursework" shape="box"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n Qualified to teach CS in NY"]

  cse_majors -> initial -> professional -> pro_cert_outcome;

  subgraph programs {
    rank="same"
    initial
    professional
  }
}
```

### Audience

The Initial/Professional Certificate Track combines the 
[Initial Certificate Track](#initial-certificate-track) and the 
[Professional Certificate Track](#professional-certificate-track), 
with fewer required credit hours than completing both tracks separately. Graduates earn an 
EdM dgree and 
an institutional recommendation for NYS Initial and Professional Certifications 
in CS, qualifying the holder to teach CS in New York schools.

### Admission requirements

The admission requirements for the Initial/Professional Certificate Track are the same 
as for the [Initial Certificate Track](#initial-certificate-track). 
Please see the [program web site](#TODO) for updates and details on application. 

- **An undergraduate degree** from an accredited institution
- **Content knowledge**:
  - Either an undergraduate major in CS or a related field, or 
  - 12 credit hours of CS satisfying the [content knowledge program outcomes](#cs-content-knowledge)
- **Test scores**[^1]: GRE or MAT scores from tests taken within five years
- **Contact information for two references**
- **Unofficial transcripts from all colleges attended**. (UB transcripts are automatically submitted for current UB students and alumni.)
- **Statement of education and career goals**

### Status

The details of the initial/professional track still need to be worked out.

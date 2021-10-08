---
title: Initial Certificate Track
---

## Initial Certificate Track

```{.graphviz}
digraph G {
  rank="max"
  rankdir="LR"
  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework"]
  initial [label="Initial coursework" shape="box"]
  init_cert_outcome [label="Certificate of Advanced Study\n Recommendation for NYS Initial Certificate in CS\n Qualified to teach CS in NY for 5 years"]
  cse_majors -> initial -> init_cert_outcome;
  
  subgraph programs {
    rank="same"
    initial
  }
  subgraph ends {
    rank="same"
    init_cert_outcome
  }
}
```

### Audience

The Initial Certificate Track is suitable for anyone with a content knowledge background in CS
who wishes to become a CS teacher. Graduates earn a Certificate of Advanced Study 
in Computer Science and an institutional recommendation for a NYS Initial Certification in CS, 
which qualifies the holder to teach CS in New York schools. 

### Admission requirements

Please see the [program web site](#TODO) for updates and details on application. 

- **An undergraduate degree** from an accredited institution
- **Content knowledge**:
  - Either an undergraduate major in CS or a related field, or 
  - 12 credit hours of CS satisfying the [content knowledge program outcomes](#cs-content-knowledge)
- **Test scores**[^1]: GRE or MAT scores from tests taken within five years
- **Contact information for two references**
- **Unofficial transcripts from all colleges attended**. (UB transcripts are automatically submitted for current UB students and alumni.)
- **Statement of education and career goals**

[^1]: Graduate Record Exam (GRE) or Miller Analogies Test (MAT) scores are required from tests taken within the last five years—including verbal, quantitative and writing sections. Please use institution code 2925 and department code 3101.  While GRE/MAT scores are not demonstrated to be predictive of student success in our program, by statutory regulation we are required to have a standardized admission test score on file as part of your application. 

### Status

The details of the initial certificate track still need to be worked out.

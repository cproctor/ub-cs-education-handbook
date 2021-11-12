---
title: Initial Certificate Track
---

## Initial Certificate Track

```{.graphviz caption="The Initial Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"
  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework" shape="box"]
  initial [label="Initial coursework"]
  init_cert_outcome [label="Certificate of Advanced Study\n Recommendation for NYS Initial Certificate in CS\n Qualified to teach CS in NY for 5 years" shape="box"]
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

### Learning outcomes

The Initial Certificate Track learning outcomes are aligned with the overarching 
[CS Education Program outcomes](#program-outcomes). Incoming students are expected to 
already have a strong content background in computer science.

 - PK1: Human development
 - PK2: Learning
 - PK3: Supporting students with disabilities
 - PK4: Language acquisition and literacy
 - PK5: Curriculum and instruction
 - PK6: Professional practice and obligations
 - PCK1: Computing as a literacy
 - PCK2: Supporting learner identities
 - PCK3: Shaping the learning environment
 - PCK4: Teaching with computational media
 - PCK5: Feedback and assessment

### Coursework

#### Fall Term 1 (15 credits)

| Course                                                                 | Credits |
|------------------------------------------------------------------------|---------|
| LAI 663: Sociocultural Dimensions of Learning and Human Development    | 3       |
| [LAI 611](#lai-611): Methods in Teaching Computer Science, Grades 1-12 | 3       |
| LAI 698: Instructional Strategies                                      | 3       |
| LAI 667: Field Experience                                              | 3       |
| LAI 574: Teaching the Exceptional Learner                              | 3       |

#### Spring Term 1 (15 credits)

| Course                                                                                          | Credits |
|-------------------------------------------------------------------------------------------------|---------|
| LAI 562: English Language Learners: Emergent Theory and Practices                               | 3       |
| LAI 552: Middle Childhood/ Adolescence Literacy Methods OR  LAI 551: Childhood Literacy Methods | 3       |
| LAI 668: Supervised Teaching I                                                                  | 3       |
| LAI 595: Supervised Teaching II                                                                 | 3       |
| LAI 674: Seminar in Teaching                                                                    | 3       |

The following diagram aligns Initial Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

```{.graphviz caption="Alignment of program and course outcomes"}
digraph G {
  rank="max"
  rankdir="LR"

  node [width=3.5]

  rank1 [style=invis]
  rank2 [style=invis]

  pk1 [label="PK1: Human development" shape="box"]
  pk2 [label="PK2: Learning" shape="box"]
  pk3 [label="PK3: Supporting students with disabilities" shape="box"]
  pk4 [label="PK4: Language acquisition and literacy" shape="box"]
  pk5 [label="PK5: Curriculum and instruction" shape="box"]
  pk6 [label="PK6: Professional practice and obligations" shape="box"]
  pck1 [label="PCK1: Computing as a literacy" shape="box"]
  pck2 [label="PCK2: Supporting learner identities" shape="box"]
  pck3 [label="PCK3: Shaping the learning environment" shape="box"]
  pck4 [label="PCK4: Teaching with computational media" shape="box"]
  pck5 [label="PCK5: Feedback and assessment" shape="box"]

  node [width=1]

  lai_574 [label="LAI 574" shape="box"]
  lai_663 [label="LAI 663" shape="box"]
  lai_562 [label="LAI 562" shape="box"]
  lai_698 [label="LAI 698" shape="box"]
  lai_552 [label="LAI 552" shape="box"]
  lai_611 [label="LAI 611" shape="box"]

  edge [arrowhead=none]

  pk1  -> lai_663;
  pk1  -> lai_562;
  pk1  -> lai_574;
  pk2  -> lai_663;
  pk2  -> lai_574;
  pk3  -> lai_611;
  pk3  -> lai_574;
  pk4  -> lai_562;
  pk4  -> lai_552;
  pk5  -> lai_611;
  pk5  -> lai_698;
  pk6  -> lai_698;
  pck1 -> lai_552;
  pck2 -> lai_663;
  pck2 -> lai_562;
  pck2 -> lai_552;
  pck3 -> lai_611;
  pck4 -> lai_611;
  pck5 -> lai_611;

  edge [style=invis];

  rank1 -> rank2;
  pk1 -> pk2 -> pk3 -> pk4 -> pk5 -> pk6 -> pck1 -> pck2 -> pck3 -> pck4 -> pck5;

  subgraph outcomes {
   rank="same"
    pk1
    pk2
    pk3
    pk4
    pk5
    pk6
    pck1
    pck2
    pck3
    pck4
    pck5
  }
}
```

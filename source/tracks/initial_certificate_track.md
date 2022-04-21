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

The table below aligns Initial Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

` @table:alignments:initial `{=comment}

| Learning outcome                           | LAI 552 | LAI 562 | LAI 574 | LAI 611 | LAI 663 | LAI 698 |
| ---------------------------------------    | ------- | ------- | ------- | ------- | ------- | ------- |
| PK1: Human development                     |         | X       | X       |         | X       |         |
| PK2: Learning                              |         |         | X       |         | X       |         |
| PK3: Supporting students with disabilities |         |         | X       | X       |         |         |
| PK4: Language acquisition and literacy     | X       | X       |         | X       |         |         |
| PK5: Curriculum and instruction            |         |         |         |         |         | X       |
| PK6: Professional practice and obligations |         |         |         |         |         | X       |
| PCK1: Computing as a literacy              | X       |         |         |         |         |         |
| PCK2: Supporting learner identities        | X       | X       |         |         | X       |         |
| PCK3: Shaping the learning environment     |         |         |         | X       |         |         |
| PCK4: Teaching with computational media    |         |         |         | X       |         |         |
| PCK5: Feedback and assessment              |         |         |         | X       |         |         |

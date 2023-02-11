---
title: Initial Certificate Track
---

## Initial Certificate Track

```{.graphviz caption="The Initial Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"
  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework" shape="box"]
  initial [label="Initial coursework\n& residency"]
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

Students may complete the first-year courses in any order and at any pace. 
However, the residency year is an integrated experience and courses must be taken as listed.

#### Fall Term 1 (6 credits)

| Course                                                                          | Credits |
| ------------------------------------------------------------------------------- | ------- |
| [LAI 605](#lai-605): Critical Computational Literacies                          | 3       |
| [LAI 676](#lai-676): The Pedagogy of Programming                                | 3       |
| [LAI 698](#lai-698): Instructional Strategies in Inclusive Classrooms           | 3       |

#### Spring Term 1 (6 credits)

| Course                                                                        | Credits |
| ----------------------------------------------------------------------------- | ------- |
| [LAI 562](#lai-562): English Language Learners: Emergent Theory and Practices | 3       |
| [LAI 574](#lai-574): Teaching the Exceptional Learner                         | 3       |
| [LAI 611](#lai-611): Methods in Teaching Computer Science, Grades 1-12        | 3       |

#### Fall Term 2: Residency (9 credits)

| Course                                                                 | Credits |
| ---------------------------------------------------------------------- | ------- |
| [LAI 668](#lai-668): Supervised Teaching I                             | 3       |
| [LAI 667](#lai-667): Field Experience                                  | 3       |
| [LAI 515](#lai-515): Action Research to Improve Teaching and Learning  | 3       |

#### Spring Term 2: Residency (9 credits)

| Course                                                                 | Credits |
| ---------------------------------------------------------------------- | ------- |
| [LAI 595](#lai-595): Supervised Teaching II                            | 3       |
| [LAI 674](#lai-674): Seminar in Teaching                               | 3       |
| [LAI 700](#lai-700): CS Education Capstone                             | 3       |

The table below aligns Initial Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

` @table:alignment:initial `{=comment}

| code   | 515   | 562   | 574   | 595   | 605   | 611   | 667   | 668   | 674   | 676   | 698   | 700   |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| PK1    |       | X     | X     |       |       |       |       |       |       |       |       |       |
| PK2    |       |       | X     |       |       |       |       |       |       |       |       |       |
| PK3    |       |       | X     |       |       | X     |       |       |       |       |       |       |
| PK4    |       | X     |       |       |       | X     |       |       |       |       |       |       |
| PK5    |       |       |       |       |       |       |       |       |       |       | X     |       |
| PK6    |       |       |       |       |       |       |       |       |       |       | X     |       |
| PCK1   |       |       |       |       | X     |       |       |       |       |       |       |       |
| PCK2   |       | X     |       |       | X     |       |       |       |       | X     |       |       |
| PCK3   | X     |       |       |       | X     | X     |       |       |       |       |       |       |
| PCK4   |       |       |       |       |       | X     |       |       |       | X     |       |       |
| PCK5   |       |       |       |       |       | X     |       |       |       | X     |       |       |

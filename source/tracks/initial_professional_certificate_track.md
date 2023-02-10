---
title: Initial/Professional Certificate Track
---

## Initial/Professional Certificate Track

```{.graphviz caption="The Initial/Professional Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"

  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework" shape="box"]
  initial [label="Initial coursework\n& residency"]
  professional [label="Professional coursework"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n Qualified to teach CS in NY" shape="box"]

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
with fewer required credit hours than completing both tracks separately 
(48 credit hours instead of 60). Graduates earn an EdM dgree and 
an institutional recommendation for NYS Initial and Professional Certifications 
in CS, qualifying the holder to teach CS in New York schools. This track generally requires 
one year of full-time coursework followed by a one-year residency placement in a school.

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

### Learning outcomes

The Initial/Professional Certificate Track learning outcomes are aligned with the overarching 
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
 - L1: Equity and opportunity
 - L2: Connected learning
 - L3: Interdisciplinary connections
 - L4: Design and research

### Coursework

#### Fall Term 1 (15 credits)

| Course                                                                          | Credits |
| ------------------------------------------------------------------------------- | ------- |
| [LAI 551](#lai-551): Childhood Literacy Methods*                                | 3       |
| [LAI 605](#lai-605): Critical Computational Literacies                          | 3       |
| [LAI 663](#lai-663): Sociocultural Dimensions of Learning and Human Development | 3       |
| [LAI 676](#lai-676): The Pedagogy of Programming                                | 3       |
| [LAI 698](#lai-698): Instructional Strategies                                   | 3       |

*Alternate: [LAI 552](#lai-552): Middle Childhood/Adolescence Literacy Methods

#### Spring Term 1 (15 credits)

| Course                                                                        | Credits |
| ----------------------------------------------------------------------------- | ------- |
| [LAI 562](#lai-562): English Language Learners: Emergent Theory and Practices | 3       |
| [LAI 573](#lai-573): Technology as a Social Practice                          | 3       |
| [LAI 574](#lai-574): Teaching the Exceptional Learner                         | 3       |
| [LAI 611](#lai-611): Methods in Teaching Computer Science, Grades 1-12        | 3       |
| [LAI 677](#lai-677): Survey of Topics in K12 Computer Science                 | 3       |

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

The following diagram aligns Initial/Professional Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

` @table:alignment:initial_professional `{=comment}

| code   | 515   | 551   | 562   | 573   | 574   | 595   | 605   | 611   | 663   | 667   | 668   | 674   | 676   | 677   | 698   | 700   |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| PK1    |       |       | X     |       | X     |       |       |       | X     |       |       |       |       |       |       |       |
| PK2    |       |       |       |       | X     |       |       |       | X     |       |       |       |       |       |       |       |
| PK3    |       |       |       |       | X     |       |       | X     |       |       |       |       |       |       |       |       |
| PK4    |       |       | X     |       |       |       |       | X     |       |       |       |       |       |       |       |       |
| PK5    |       |       |       |       |       |       |       |       |       |       |       |       |       |       | X     |       |
| PK6    |       |       |       |       |       |       |       |       |       |       |       |       |       |       | X     |       |
| PCK1   |       |       |       |       |       |       | X     |       |       |       |       |       |       |       |       |       |
| PCK2   |       |       | X     | X     |       |       | X     |       | X     |       |       |       | X     |       |       |       |
| PCK3   | X     |       |       |       |       |       | X     | X     |       |       |       |       |       |       |       |       |
| PCK4   |       |       |       |       |       |       |       | X     |       |       |       |       | X     |       |       |       |
| PCK5   |       |       |       |       |       |       |       | X     |       |       |       |       | X     |       |       |       |
| L1     |       |       |       |       |       |       | X     |       |       |       |       |       |       |       |       | X     |
| L2     | X     |       |       |       |       |       | X     |       |       |       |       |       | X     |       |       | X     |
| L3     |       |       |       |       |       |       |       |       |       |       |       |       |       | X     |       | X     |
| L4     | X     |       |       |       |       |       |       |       |       |       |       |       |       | X     |       | X     |

---
title: Initial/Professional Certificate Track
---

## Initial/Professional Certificate Track

```{.graphviz caption="The Initial/Professional Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"

  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework" shape="box"]
  initial [label="Initial coursework"]
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
with fewer required credit hours than completing both tracks separately. Graduates earn an 
EdM dgree and 
an institutional recommendation for NYS Initial and Professional Certifications 
in CS, qualifying the holder to teach CS in New York schools. This track generally requires 
two years of full-time coursework.

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

| Strand | Outcome                               |
| ------ | ------------------------------------- |
| PK     | Human development                     |
| PK     | Learning                              |
| PK     | Supporting students with disabilities |
| PK     | Language acquisition and literacy     |
| PK     | Curriculum and instruction            |
| PK     | Classroom use of technology           |
| PK     | Assessment                            |
| PK     | Education in society                  |
| PK     | Professional practice and obligations |
| PCK    | Computing as a literacy               |
| PCK    | Supporting learner identities         |
| PCK    | Shaping the learning environment      |
| PCK    | Teaching with computational media     |
| PCK    | Feedback and assessment               |
| L      | Equity and opportunity                |
| L      | Connected learning                    |
| L      | Interdisciplinary connections         |
| L      | Design and research                   |

### Coursework

#### Fall Term 1 (15 credits)

| Course                                                                 | Credits | New? |
| ---------------------------------------------------------------------- | ------- | ---- |
| [LAI 525](#lai-525): Critical Computational Literacies                 | 3       |      |
| [LAI 611](#lai-611): Methods in Teaching Computer Science, Grades 1-12 | 3       | X    |
| LAI 663: Sociocultural Dimensions of Learning and Human Development    | 3       |      |
| LAI 667: Field Experience                                              | 3       |      |
| LAI 698: Instructional Strategies                                      | 3       |      |

#### Spring Term 1 (15 credits)

| Course                                                                 | Credits | New? |
| ---------------------------------------------------------------------- | ------- | ---- |
| [LAI XXX](#lai-XXX): The Pedagogy of Programming                       | 3       | X    |
| LAI 562: English Language Learners: Emergent Theory and Practices      | 3       |      |
| LAI 668: Supervised Teaching I                                         | 3       |      |
| LAI 595: Supervised Teaching II                                        | 3       |      |
| LAI 674: Seminar in Teaching                                           | 3       |      |

#### Year 2 (18 credits)

| Course                                                                                        | Credits | New? |
| ----------------------------------------------------------------                              | ------- | ---- |
| [LAI YYY](#lai-YYY): Survey of Topics in K12 Computer Science                                 | 3       | X    |
| LAI 515 Action Research to Improve Teaching and Learning                                      | 3       |      |
| LAI 552: Middle Childhood/Adolescence Literacy Methods OR LAI 551: Childhood Literacy Methods | 3       |      |
| LAI 574: Teaching the Exceptional Learner                                                     | 3       |      |
| LAI 600 Curriculum Integration and Assessment                                                 | 3       |      |
| [LAI 700](#lai-700): CS Education Capstone                                                    | 3       | X    |

#### Alignment of program and course outcomes

The following table aligns Initial/Professional Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

##### Pedagogical Knowledge

| Strand | Outcome                               | LAI 611 | LAI 663 | LAI 698 | LAI 562 | LAI 552 | LAI 574 | LAI 600 |
| ------ | ------------------------------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| PK     | Human development                     |         | X       |         | X       |         | X       |         |
| PK     | Learning                              |         | X       |         |         |         | X       |         |
| PK     | Supporting students with disabilities | X       |         |         |         |         | X       |         |
| PK     | Language acquisition and literacy     |         |         |         | X       | X       |         |         |
| PK     | Curriculum and instruction            | X       |         | X       |         |         |         | X       |
| PK     | Classroom use of technology           | X       |         |         |         |         |         |         |
| PK     | Assessment                            | X       |         | X       |         |         |         | X       |
| PK     | Education in society                  |         |         |         | X       |         | X       |         |
| PK     | Professional practice and obligations |         |         | X       |         |         |         |         |

##### Pedagogical Content Knowledge and Leadership

| Strand | Outcome                               | LAI 525 | LAI 611 | LAI 663 | LAI XXX | LAI 562 | LAI YYY | LAI 515 | LAI 552 | LAI 600 | LAI 700 |
| ------ | ------------------------------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| PCK    | Computing as a literacy               | X       |         |         |         |         |         |         | X       |         |         |
| PCK    | Supporting learner identities         | X       |         | X       | X       | X       |         |         | X       |         |         |
| PCK    | Shaping the learning environment      | X       | X       |         |         |         |         |         |         |         |         |
| PCK    | Teaching with computational media     |         | X       |         | X       |         |         |         |         |         |         |
| PCK    | Feedback and assessment               |         | X       |         | X       |         |         |         |         | X       |         |
| L      | Equity and opportunity                | X       |         |         |         |         |         | X       |         |         | X       |
| L      | Connected learning                    |         |         |         | X       |         |         | X       |         |         |         |
| L      | Interdisciplinary connections         |         |         |         |         |         | X       |         |         |         | X       |
| L      | Design and research                   |         |         |         |         |         | X       | X       |         |         | X       |

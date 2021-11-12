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

| Course                                                                 | Credits |
| ---------------------------------------------------------------------- | ------- |
| [LAI 525](#lai-525): Critical Computational Literacies                 | 3       |
| [LAI 611](#lai-611): Methods in Teaching Computer Science, Grades 1-12 | 3       |
| LAI 663: Sociocultural Dimensions of Learning and Human Development    | 3       |
| LAI 667: Field Experience                                              | 3       |
| LAI 698: Instructional Strategies                                      | 3       |

#### Spring Term 1 (15 credits)

| Course                                                                 | Credits |
| ---------------------------------------------------------------------- | ------- |
| [LAI XXX](#lai-XXX): The Pedagogy of Programming                       | 3       |
| LAI 562: English Language Learners: Emergent Theory and Practices      | 3       |
| LAI 668: Supervised Teaching I                                         | 3       |
| LAI 595: Supervised Teaching II                                        | 3       |
| LAI 674: Seminar in Teaching                                           | 3       |

#### Year 2 (18 credits)

| Course                                                                                        | Credits |
| ----------------------------------------------------------------                              | ------- |
| [LAI YYY](#lai-YYY): Survey of Topics in K12 Computer Science                                 | 3       |
| LAI 515 Action Research to Improve Teaching and Learning                                      | 3       |
| LAI 552: Middle Childhood/Adolescence Literacy Methods OR LAI 551: Childhood Literacy Methods | 3       |
| LAI 574: Teaching the Exceptional Learner                                                     | 3       |
| LAI 600 Curriculum Integration and Assessment                                                 | 3       |
| [LAI 700](#lai-700): CS Education Capstone                                                    | 3       |

The following diagram aligns Initial/Professional Certificate Track learning outcomes with courses 
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
  l1 [label="L1: Equity and opportunity" shape="box"]
  l2 [label="L2: Connected learning" shape="box"]
  l3 [label="L3: Interdisciplinary connections" shape="box"]
  l4 [label="L4: Design and research" shape="box"]

  node [width=1]

  lai_xxx [label="LAI XXX" shape="box"]
  lai_yyy [label="LAI YYY" shape="box"]
  lai_525 [label="LAI 525" shape="box"]
  lai_574 [label="LAI 574" shape="box"]
  lai_663 [label="LAI 663" shape="box"]
  lai_562 [label="LAI 562" shape="box"]
  lai_698 [label="LAI 698" shape="box"]
  lai_552 [label="LAI 552" shape="box"]
  lai_611 [label="LAI 611" shape="box"]
  lai_515 [label="LAI 515" shape="box"]
  lai_700 [label="LAI 700" shape="box"]

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
  pck1 -> lai_525;
  pck1 -> lai_552;
  pck2 -> lai_525;
  pck2 -> lai_663;
  pck2 -> lai_xxx;
  pck2 -> lai_562;
  pck2 -> lai_552;
  pck3 -> lai_525;
  pck3 -> lai_611;
  pck4 -> lai_611;
  pck4 -> lai_xxx;
  pck5 -> lai_xxx;
  pck5 -> lai_611;
  l1   -> lai_525;
  l1   -> lai_515;
  l1   -> lai_700;
  l2   -> lai_xxx;
  l2   -> lai_515;
  l2   -> lai_525;
  l2   -> lai_700;
  l3   -> lai_yyy;
  l3   -> lai_700;
  l4   -> lai_yyy;
  l4   -> lai_515;
  l4   -> lai_700;

  edge [style=invis];

  rank1 -> rank2;
  pk1 -> pk2 -> pk3 -> pk4 -> pk5 -> pk6 -> pck1 -> pck2 -> pck3 -> pck4 -> pck5 -> l1 -> l2 -> l3 -> l4;

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
    l1
    l2
    l3
    l4
  }
}
```

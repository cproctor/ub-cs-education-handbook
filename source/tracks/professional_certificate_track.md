---
title: Professional Certificate Track
---

## Professional Certificate Track

```{.graphviz caption="The Professional Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"

  init_cert [label="Teachers holding\n initial certificate in CS" shape="box"]
  professional [label="Professional coursework"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n Qualified to teach CS in NY" shape="box"]

  init_cert -> professional -> pro_cert_outcome;
}
```

### Audience

The Professional Certificate Track is available to teachers holding initial certification in Computer Science wishing to earn professional certification. This track requires one year of full-time coursework.

### Admission requirements

- **Initial NY teacher certification** in Computer Science
- **Application essay** focused on vision for CS education
- **Recommendation letter** focused on preparation to succeed and potential for impact

### Learning outcomes

The Initial Certificate Track learning outcomes are aligned with the overarching 
[CS Education Program outcomes](#program-outcomes). Incoming students are expected to 
already have a strong content background in computer science as well as a strong background
in pedagogical knowledge. This track emphasizes the synthesis of content knowledge and pedagogical 
knowledge into CS pedagogical content knowledge and leadership. 

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

Coursework consists of 30 credits. Courses may be taken in any order and pace except for LAI 700, 
which should be taken in the final semester.

| Course                                                                   | Credits   | New?   |
| ------------------------------------------------------------------------ | --------- | ------ |
| [LAI XXX](#lai-XXX): The Pedagogy of Programming                         | 3         | X      |
| [LAI YYY](#lai-YYY): Survey of Topics in K12 Computer Science            | 3         | X      |
| LAI 515 Action Research to Improve Teaching and Learning                 | 3         |        |
| [LAI 525](#lai-525): Critical Computational Literacies                   | 3         |        |
| LAI 600 Curriculum Integration and Assessment                            | 3         |        |
| [LAI 700](#lai-700): CS Education Capstone                               | 3         | X      |
| Electives                                                                | 12        |        |

Students will choose from the following electives:

- [LAI 573](#lai-573): Technology as a Social Practice, recommended for elementary teachers.
- [LAI 508](#lai-508): Educational Uses of the Internet, recommended for secondary teachers.
- [LAI 686](#lai-686): Critical Computational Literacies Design Studio, recommended for 
  teachers interested in educational technology design.
- [DEE 520](#dee-520): Computing Education Research, recommended for teachers interested in 
  participating in research on computing education.
- Graduate-level CSE courses. Recommended for students with strong content background, especially 
  those interested in teaching Advanced Placement courses.
- Other LAI, LIS, or interdisciplinary courses with advisor approval.

#### Alignment of program and course outcomes

The following table aligns Professional Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

| Strand | Outcome                           | LAI XXX | LAI YYY | LAI 525 | LAI 700 |
| ------ | --------------------------------- | ------- | ------- | ------- | ------- |
| PCK    | Computing as a literacy           |         |         | X       |         |
| PCK    | Supporting learner identities     | X       |         | X       |         |
| PCK    | Shaping the learning environment  |         |         | X       |         |
| PCK    | Teaching with computational media | X       |         |         |         |
| PCK    | Feedback and assessment           | X       |         |         |         |
| L      | Equity and opportunity            |         |         | X       | X       |
| L      | Connected learning                | X       |         |         |         |
| L      | Interdisciplinary connections     |         | X       |         | X       |
| L      | Design and research               |         | X       |         | X       |

The following diagram aligns Initial/Professional Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

```{.graphviz caption="Alignment of program and course outcomes"}
digraph G {
  rank="max"
  rankdir="LR"

  node [width=3.5]

  rank1 [style=invis]
  rank2 [style=invis]

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
  lai_700 [label="LAI 700" shape="box"]

  edge [arrowhead=none]

  pck1 -> lai_525;
  pck2 -> lai_525;
  pck2 -> lai_xxx;
  pck3 -> lai_525;
  pck4 -> lai_xxx;
  pck5 -> lai_xxx;
  l1   -> lai_525;
  l1   -> lai_700;
  l2   -> lai_xxx;
  l3   -> lai_yyy;
  l3   -> lai_700;
  l4   -> lai_yyy;
  l4   -> lai_700;

  edge [style=invis];

  rank1 -> rank2;
  pck1 -> pck2 -> pck3 -> pck4 -> pck5 -> l1 -> l2 -> l3 -> l4;

  subgraph outcomes {
   rank="same"
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

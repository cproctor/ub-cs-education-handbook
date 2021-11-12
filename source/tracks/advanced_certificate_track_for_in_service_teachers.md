---
title: Advanced Certificate Track for In-Service Teachers
---

## Advanced Certificate Track for In-Service Teachers

```{.graphviz caption="The Advanced Certificate Track for In-Service Teachers"}
digraph G {
  rank="max"
  rankdir="LR"
  other_cert [label="Teachers holding a certificate\n in another discipline"]
  advanced_certificate [label="Advanced certificate\n coursework" shape="box"]
  adv_cert_outcome [label="Certificate of Advanced Study\n Qualified to teach CS in NY"]
  other_cert -> advanced_certificate -> adv_cert_outcome;
}
```
### Audience

The Advanced Certificate Track for In-Service Teachers is designed for New York teachers currently holding 
a teaching certificate in another discipline. 
This program builds on teachers’ expertise, experience, identities, and 
commitments to grow into a new subject area. There are no content knowledge 
prerequisites, however the program will require teachers to complete college-level 
CS coursework and will draw on existing pedagogical knowledge and 
pedagogical content knowledge in their current disciplines.

The Advanced Certificate Track for In-Service Teachers is designed to be completed remotely by working 
professionals at their own pace. 

### Admission requirements

- **Initial or Professional NY teacher certification** in any discipline
- **Teaching experience** (minimum one year recommended)
- **An ongoing context of practice** (classroom teaching, club) 
- **Application essay** focused on vision for CS education
- **Statement justifying preparation for CS coursework**
- **Recommendation letter** focused on preparation to succeed and potential for impact

### Learning outcomes

The Advanced Certificate Track for In-Service Teachers learning outcomes are aligned with the overarching 
[CS Education Program outcomes](#program-outcomes).
The Advanced Certificate Track for In-Service Teachers prioritizes CS content knowledge.
The Advanced Certificate Track for In-Service Teachers focuses on adapting teachers' 
existing pedagogical content knowledge to CS.

 - CK1: Impacts of computing                  
 - CK2: Computational thinking                
 - CK3: Networks and system design            
 - CK4: Cybersecurity                         
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

The Advanced Certificate consists of five courses and a total of 15 credit hours. 
Courses may be taken in any order and at any pace, except for the culminating capstone
course.

| Course                                                        | Credits | New? |
|---------------------------------------------------------------|---------|------|
| [LAI XXX](#lai-XXX): The Pedagogy of Programming              | 3       | X    |
| [LAI YYY](#lai-YYY): Survey of Topics in K12 Computer Science | 3       | X    |
| [LAI 525](#lai-525): Critical Computational Literacies        | 3       |      |
| [LAI 700](#lai-700): CS Education Capstone                    | 3       | X    |
| Elective (see below)                                          | 3       |      |

Students will choose one of the following electives:

- [LAI 573](#lai-573): Technology as a Social Practice, recommended for elementary teachers.
- [LAI 508](#lai-508): Educational Uses of the Internet, recommended for secondary teachers.
- [LAI 686](#lai-686): Critical Computational Literacies Design Studio, recommended for 
  teachers interested in educational technology design.
- [DEE 520](#dee-520): Computing Education Research, recommended for teachers interested in 
  participating in research on computing education.
- A graduate-level CSE course. Recommended for students with strong content background, especially 
  those interested in teaching Advanced Placement courses.

The following diagram aligns Initial/Professional Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

```{.graphviz caption="Alignment of program and course outcomes"}
digraph G {
  rank="max"
  rankdir="LR"

  node [width=3.5]

  rank1 [style=invis]
  rank2 [style=invis]

  ck1 [label="CK: Impacts of computing" shape="box"]
  ck2 [label="CK: Computational thinking" shape="box"]
  ck3 [label="CK: Networks and system design" shape="box"]
  ck4 [label="CK: Cybersecurity" shape="box"]
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

  ck1  -> lai_yyy;
  ck2  -> lai_xxx;
  ck3  -> lai_yyy;
  ck4  -> lai_yyy;
  pck1 -> lai_525;
  pck2 -> lai_525;
  pck2 -> lai_xxx;
  pck3 -> lai_525;
  pck4 -> lai_xxx;
  pck5 -> lai_xxx;
  l1   -> lai_525;
  l1   -> lai_700;
  l2   -> lai_xxx;
  l2   -> lai_525;
  l2   -> lai_700;
  l3   -> lai_yyy;
  l3   -> lai_700;
  l4   -> lai_yyy;
  l4   -> lai_700;

  edge [style=invis];

  rank1 -> rank2;
  ck1 -> ck2 -> ck3 -> ck4 -> pck1 -> pck2 -> pck3 -> pck4 -> pck5 -> l1 -> l2 -> l3 -> l4;

  subgraph outcomes {
   rank="same"
    ck1
    ck2
    ck3
    ck4
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

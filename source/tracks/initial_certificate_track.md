---
title: Initial Certificate Track
---

## Initial Certificate Track

```{.graphviz caption="The Initial Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"
  bgcolor="transparent"
  graph [fontname="Helvetica", nodesep=0.35]
  node [fontname="Helvetica", fontsize=11, shape="box", style="rounded,filled", penwidth=0, margin="0.18,0.1"]
  edge [color="#9aa5b1", arrowsize=0.75, penwidth=1.3]

  cse_majors [label="Completed undergraduate\n CS major\n or qualifying coursework" width=3 fillcolor="#e8eef7" fontcolor="#1d3f6e"]
  initial [label="Initial coursework\n& residency" width=2.4 fillcolor="#1d5fa8" fontcolor="white"]
  init_cert_outcome [label="Certificate of Advanced Study\n Recommendation for NYS Initial Certificate in CS\n Qualified to teach CS in NY for 5 years" width=5 fillcolor="#1f7a4d" fontcolor="white"]
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

Please see the [program web site](https://ed.buffalo.edu/academics/teacher-ed/computer-science.html) for updates and details on application. 

- **An undergraduate degree** from an accredited institution
- **Content knowledge**:
  - Either an undergraduate major in CS or a related field, or 
  - 12 credit hours of CS satisfying the [content knowledge program outcomes](#cs-content-knowledge)
- **Contact information for two references**
- **Unofficial transcripts from all colleges attended**. (UB transcripts are automatically submitted for current UB students and alumni.)
- **Statement of education and career goals**

### Learning outcomes

The Initial Certificate Track learning outcomes are aligned with the overarching 
[CS Education Program outcomes](#program-outcomes). Incoming students are expected to 
already have a strong content background in computer science.

` @list:trackoutcomes:initial `{=comment}

 - [PK1](#pk1 "Human development"){.outcome .pk}: Human development
 - [PK2](#pk2 "Learning"){.outcome .pk}: Learning
 - [PK3](#pk3 "Supporting students with disabilities"){.outcome .pk}: Supporting students with disabilities
 - [PK4](#pk4 "Language acquisition and literacy"){.outcome .pk}: Language acquisition and literacy
 - [PK5](#pk5 "Curriculum and instruction"){.outcome .pk}: Curriculum and instruction
 - [PK6](#pk6 "Professional practice and obligations"){.outcome .pk}: Professional practice and obligations
 - [PCK1](#pck1 "Computing as a literacy"){.outcome .pck}: Computing as a literacy
 - [PCK2](#pck2 "Supporting learner identities"){.outcome .pck}: Supporting learner identities
 - [PCK3](#pck3 "Shaping the learning environment"){.outcome .pck}: Shaping the learning environment
 - [PCK4](#pck4 "Teaching with computational media"){.outcome .pck}: Teaching with computational media
 - [PCK5](#pck5 "Feedback and assessment"){.outcome .pck}: Feedback and assessment
















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
| [LAI 611](#lai-611): Methods in Teaching Computer Science, Grades K-12        | 3       |

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
| [LAI 516](#lai-516): Infrastructure for K12 Computing Education        | 3       |

The table below aligns Initial Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

` @table:alignment:initial `{=comment}

```{=html}
<table>
<thead><tr><th class="divider">Outcome</th><th><a href="#lai-605">605</a></th><th><a href="#lai-676">676</a></th><th class="divider"><a href="#lai-698">698</a></th><th><a href="#lai-562">562</a></th><th><a href="#lai-574">574</a></th><th class="divider"><a href="#lai-611">611</a></th><th><a href="#lai-515">515</a></th><th><a href="#lai-667">667</a></th><th class="divider"><a href="#lai-668">668</a></th><th><a href="#lai-516">516</a></th><th><a href="#lai-595">595</a></th><th><a href="#lai-674">674</a></th></tr></thead>
<tbody>
<tr><td class="divider"><a href="#pk1" class="outcome pk" title="Human development">PK1</a></td><td></td><td></td><td class="divider"></td><td><span class="dot pk"></span></td><td><span class="dot pk"></span></td><td class="divider"></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pk2" class="outcome pk" title="Learning">PK2</a></td><td></td><td></td><td class="divider"></td><td></td><td><span class="dot pk"></span></td><td class="divider"></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pk3" class="outcome pk" title="Supporting students with disabilities">PK3</a></td><td></td><td></td><td class="divider"></td><td></td><td><span class="dot pk"></span></td><td class="divider"><span class="dot pk"></span></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pk4" class="outcome pk" title="Language acquisition and literacy">PK4</a></td><td></td><td></td><td class="divider"></td><td><span class="dot pk"></span></td><td></td><td class="divider"><span class="dot pk"></span></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pk5" class="outcome pk" title="Curriculum and instruction">PK5</a></td><td></td><td></td><td class="divider"><span class="dot pk"></span></td><td></td><td></td><td class="divider"></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pk6" class="outcome pk" title="Professional practice and obligations">PK6</a></td><td></td><td></td><td class="divider"><span class="dot pk"></span></td><td></td><td></td><td class="divider"></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck1" class="outcome pck" title="Computing as a literacy">PCK1</a></td><td><span class="dot pck"></span></td><td></td><td class="divider"></td><td></td><td></td><td class="divider"></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck2" class="outcome pck" title="Supporting learner identities">PCK2</a></td><td><span class="dot pck"></span></td><td><span class="dot pck"></span></td><td class="divider"></td><td><span class="dot pck"></span></td><td></td><td class="divider"></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck3" class="outcome pck" title="Shaping the learning environment">PCK3</a></td><td><span class="dot pck"></span></td><td></td><td class="divider"></td><td></td><td></td><td class="divider"><span class="dot pck"></span></td><td><span class="dot pck"></span></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck4" class="outcome pck" title="Teaching with computational media">PCK4</a></td><td></td><td><span class="dot pck"></span></td><td class="divider"></td><td></td><td></td><td class="divider"><span class="dot pck"></span></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck5" class="outcome pck" title="Feedback and assessment">PCK5</a></td><td></td><td><span class="dot pck"></span></td><td class="divider"></td><td></td><td></td><td class="divider"><span class="dot pck"></span></td><td></td><td></td><td class="divider"></td><td></td><td></td><td></td></tr>
</tbody>
</table>
```
```{=latex}
\begin{longtable}{l|ccc|ccc|ccc|ccc}
\toprule
\textbf{Outcome} & \textbf{\hyperlink{lai-605}{605}} & \textbf{\hyperlink{lai-676}{676}} & \textbf{\hyperlink{lai-698}{698}} & \textbf{\hyperlink{lai-562}{562}} & \textbf{\hyperlink{lai-574}{574}} & \textbf{\hyperlink{lai-611}{611}} & \textbf{\hyperlink{lai-515}{515}} & \textbf{\hyperlink{lai-667}{667}} & \textbf{\hyperlink{lai-668}{668}} & \textbf{\hyperlink{lai-516}{516}} & \textbf{\hyperlink{lai-595}{595}} & \textbf{\hyperlink{lai-674}{674}} \\
\midrule
\endhead
\bottomrule
\endlastfoot
\OutcomeBadge{OutcomePK}{PK1} &  &  &  & \OutcomeDot{OutcomePK} & \OutcomeDot{OutcomePK} &  &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePK}{PK2} &  &  &  &  & \OutcomeDot{OutcomePK} &  &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePK}{PK3} &  &  &  &  & \OutcomeDot{OutcomePK} & \OutcomeDot{OutcomePK} &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePK}{PK4} &  &  &  & \OutcomeDot{OutcomePK} &  & \OutcomeDot{OutcomePK} &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePK}{PK5} &  &  & \OutcomeDot{OutcomePK} &  &  &  &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePK}{PK6} &  &  & \OutcomeDot{OutcomePK} &  &  &  &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePCK}{PCK1} & \OutcomeDot{OutcomePCK} &  &  &  &  &  &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePCK}{PCK2} & \OutcomeDot{OutcomePCK} & \OutcomeDot{OutcomePCK} &  & \OutcomeDot{OutcomePCK} &  &  &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePCK}{PCK3} & \OutcomeDot{OutcomePCK} &  &  &  &  & \OutcomeDot{OutcomePCK} & \OutcomeDot{OutcomePCK} &  &  &  &  &  \\
\OutcomeBadge{OutcomePCK}{PCK4} &  & \OutcomeDot{OutcomePCK} &  &  &  & \OutcomeDot{OutcomePCK} &  &  &  &  &  &  \\
\OutcomeBadge{OutcomePCK}{PCK5} &  & \OutcomeDot{OutcomePCK} &  &  &  & \OutcomeDot{OutcomePCK} &  &  &  &  &  &  \\
\end{longtable}
```

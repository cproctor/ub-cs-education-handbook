---
title: Professional Certificate Track
---

## Professional Certificate Track

```{.graphviz caption="The Professional Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"
  bgcolor="transparent"
  graph [fontname="Helvetica", nodesep=0.35]
  node [fontname="Helvetica", fontsize=11, shape="box", style="rounded,filled", penwidth=0, margin="0.18,0.1"]
  edge [color="#9aa5b1", arrowsize=0.75, penwidth=1.3]

  init_cert [label="Teachers holding an initial\n or professional teaching\n certificate in any subject" width=3 fillcolor="#e8eef7" fontcolor="#1d3f6e"]
  professional [label="Professional coursework" width=2.4 fillcolor="#1d5fa8" fontcolor="white"]
  pro_cert_outcome [label="EdM\n Recommendation for NYS Professional Certificate in CS\n (or Additional Certificate in CS, if initial\n certificate was in another subject)\n Qualified to teach CS in NY" width=5 fillcolor="#1f7a4d" fontcolor="white"]

  init_cert -> professional -> pro_cert_outcome;
}
```

### Audience

The Professional Certificate Track is available to teachers holding an initial or professional 
NY teaching certificate **in any subject area** who wish to earn certification in Computer Science. 
Admission does not require an existing certificate in CS: candidates who already hold an initial 
certificate in CS earn a recommendation for NYS **Professional Certification in CS** upon 
completion, while candidates whose initial certificate is in a different subject earn a 
recommendation for an **Additional Certification in CS** instead, since New York only issues 
"professional" certification as an upgrade within the same subject as the initial certificate.
This track requires one year of full-time coursework.

### Admission requirements

- **Initial or Professional NY teacher certification**, in any subject area
- **Application essay** focused on vision for CS education
- **Recommendation letter** focused on preparation to succeed and potential for impact

### Learning outcomes

The Professional Certificate Track learning outcomes are aligned with the overarching 
[CS Education Program outcomes](#program-outcomes). Incoming students are expected to 
already have a strong content background in computer science as well as a strong background
in pedagogical knowledge. This track emphasizes the synthesis of content knowledge and pedagogical 
knowledge into CS pedagogical content knowledge and leadership. 

` @list:trackoutcomes:professional `{=comment}

 - [PCK1](#pck1 "Computing as a literacy"){.outcome .pck}: Computing as a literacy
 - [PCK2](#pck2 "Supporting learner identities"){.outcome .pck}: Supporting learner identities
 - [PCK3](#pck3 "Shaping the learning environment"){.outcome .pck}: Shaping the learning environment
 - [PCK4](#pck4 "Teaching with computational media"){.outcome .pck}: Teaching with computational media
 - [PCK5](#pck5 "Feedback and assessment"){.outcome .pck}: Feedback and assessment
 - [L1](#l1 "Equity and opportunity"){.outcome .l}: Equity and opportunity
 - [L2](#l2 "Connected learning"){.outcome .l}: Connected learning
 - [L3](#l3 "Interdisciplinary connections"){.outcome .l}: Interdisciplinary connections
 - [L4](#l4 "Design and research"){.outcome .l}: Design and research
















### Coursework

Coursework consists of 30 credits. Courses may be taken in any order and pace.

| Course                                                                   | Credits   |
| ------------------------------------------------------------------------ | --------- |
| [LAI 573](#lai-573): Technology as Social Practice                     | 3         |
| [LAI 605](#lai-605): Critical Computational Literacies                   | 3         |
| [LAI 611](#lai-611): Methods in Teaching Computer Science, Grades K-12   | 3         |
| [LAI 676](#lai-676): The Pedagogy of Programming                         | 3         |
| [LAI 677](#lai-677): Survey of Topics in K12 Computer Science            | 3         |
| [LAI 516](#lai-516): Infrastructure for K12 Computing Education          | 3         |
| Electives                                                                | 12        |

Students will choose from the following electives:

- [LAI 573](#lai-573): Technology as Social Practice, recommended for elementary teachers.
- [LAI 508](#lai-508): Educational Uses of the Internet, recommended for secondary teachers.
- [LAI 686](#lai-686): Critical Computational Literacies Design Studio, recommended for 
  teachers interested in educational technology design.
- [DEE 520](#dee-520): Computing Education Research, recommended for teachers interested in 
  participating in research on computing education.
- Graduate-level CSE courses. Recommended for students with strong content background, especially 
  those interested in teaching Advanced Placement courses.
- Other LAI, LIS, or interdisciplinary courses with advisor approval.

The table below aligns Professional Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

` @table:alignment:professional `{=comment}

```{=html}
<table>
<thead><tr><th class="divider">Outcome</th><th><a href="#lai-516">516</a></th><th><a href="#lai-573">573</a></th><th><a href="#lai-605">605</a></th><th><a href="#lai-611">611</a></th><th><a href="#lai-676">676</a></th><th><a href="#lai-677">677</a></th></tr></thead>
<tbody>
<tr><td class="divider"><a href="#pck1" class="outcome pck" title="Computing as a literacy">PCK1</a></td><td></td><td></td><td><span class="dot pck"></span></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck2" class="outcome pck" title="Supporting learner identities">PCK2</a></td><td></td><td><span class="dot pck"></span></td><td><span class="dot pck"></span></td><td></td><td><span class="dot pck"></span></td><td></td></tr>
<tr><td class="divider"><a href="#pck3" class="outcome pck" title="Shaping the learning environment">PCK3</a></td><td></td><td></td><td><span class="dot pck"></span></td><td><span class="dot pck"></span></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck4" class="outcome pck" title="Teaching with computational media">PCK4</a></td><td></td><td></td><td></td><td><span class="dot pck"></span></td><td><span class="dot pck"></span></td><td></td></tr>
<tr><td class="divider"><a href="#pck5" class="outcome pck" title="Feedback and assessment">PCK5</a></td><td></td><td></td><td></td><td><span class="dot pck"></span></td><td><span class="dot pck"></span></td><td></td></tr>
<tr><td class="divider"><a href="#l1" class="outcome l" title="Equity and opportunity">L1</a></td><td><span class="dot l"></span></td><td></td><td><span class="dot l"></span></td><td></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#l2" class="outcome l" title="Connected learning">L2</a></td><td><span class="dot l"></span></td><td></td><td><span class="dot l"></span></td><td></td><td><span class="dot l"></span></td><td></td></tr>
<tr><td class="divider"><a href="#l3" class="outcome l" title="Interdisciplinary connections">L3</a></td><td><span class="dot l"></span></td><td></td><td></td><td></td><td></td><td><span class="dot l"></span></td></tr>
<tr><td class="divider"><a href="#l4" class="outcome l" title="Design and research">L4</a></td><td><span class="dot l"></span></td><td></td><td></td><td></td><td></td><td><span class="dot l"></span></td></tr>
</tbody>
</table>
```
```{=latex}
\begin{longtable}{l|cccccc}
\toprule
\textbf{Outcome} & \textbf{\hyperlink{lai-516}{516}} & \textbf{\hyperlink{lai-573}{573}} & \textbf{\hyperlink{lai-605}{605}} & \textbf{\hyperlink{lai-611}{611}} & \textbf{\hyperlink{lai-676}{676}} & \textbf{\hyperlink{lai-677}{677}} \\
\midrule
\endhead
\bottomrule
\endlastfoot
\OutcomeBadge{OutcomePCK}{PCK1} &  &  & \OutcomeDot{OutcomePCK} &  &  &  \\
\OutcomeBadge{OutcomePCK}{PCK2} &  & \OutcomeDot{OutcomePCK} & \OutcomeDot{OutcomePCK} &  & \OutcomeDot{OutcomePCK} &  \\
\OutcomeBadge{OutcomePCK}{PCK3} &  &  & \OutcomeDot{OutcomePCK} & \OutcomeDot{OutcomePCK} &  &  \\
\OutcomeBadge{OutcomePCK}{PCK4} &  &  &  & \OutcomeDot{OutcomePCK} & \OutcomeDot{OutcomePCK} &  \\
\OutcomeBadge{OutcomePCK}{PCK5} &  &  &  & \OutcomeDot{OutcomePCK} & \OutcomeDot{OutcomePCK} &  \\
\OutcomeBadge{OutcomeL}{L1} & \OutcomeDot{OutcomeL} &  & \OutcomeDot{OutcomeL} &  &  &  \\
\OutcomeBadge{OutcomeL}{L2} & \OutcomeDot{OutcomeL} &  & \OutcomeDot{OutcomeL} &  & \OutcomeDot{OutcomeL} &  \\
\OutcomeBadge{OutcomeL}{L3} & \OutcomeDot{OutcomeL} &  &  &  &  & \OutcomeDot{OutcomeL} \\
\OutcomeBadge{OutcomeL}{L4} & \OutcomeDot{OutcomeL} &  &  &  &  & \OutcomeDot{OutcomeL} \\
\end{longtable}
```

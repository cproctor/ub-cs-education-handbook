---
title: Advanced Certificate Track
---

## Advanced Certificate Track {#advanced-certificate-track-for-in-service-teachers}

```{.graphviz caption="The Advanced Certificate Track"}
digraph G {
  rank="max"
  rankdir="LR"
  bgcolor="transparent"
  graph [fontname="Helvetica", nodesep=0.35]
  node [fontname="Helvetica", fontsize=11, shape="box", style="rounded,filled", penwidth=0, margin="0.18,0.1"]
  edge [color="#9aa5b1", arrowsize=0.75, penwidth=1.3]

  other_cert [label="Teachers holding a certificate,\n or preservice teachers,\n in another discipline" width=3 fillcolor="#e8eef7" fontcolor="#1d3f6e"]
  advanced_certificate [label="Advanced certificate\n coursework" width=2.4 fillcolor="#1d5fa8" fontcolor="white"]
  adv_cert_outcome [label="Certificate of Advanced Study\n Qualified to teach CS in NY" width=5 fillcolor="#1f7a4d" fontcolor="white"]
  other_cert -> advanced_certificate -> adv_cert_outcome;
}
```
### Audience

The Advanced Certificate Track is designed for New York teachers currently holding 
a teaching certificate in another discipline, or for preservice teachers currently preparing
to teach in another discipline. 
This program builds on teachers’ expertise, experience, identities, and 
commitments to grow into a new subject area. There are no content knowledge 
prerequisites, however the program will require teachers to complete college-level 
CS coursework and will draw on existing pedagogical knowledge and 
pedagogical content knowledge in their current disciplines.

The Advanced Certificate Track can be completed remotely by working 
professionals at their own pace. An ongoing context of practice is required, 
as teachers will design and implement interdisciplinary CS lessons as part of 
the program.

### Admission requirements

- Either: 
  - **Initial or Professional NY teacher certification** in any discipline and 
  - **Teaching experience** (minimum one year recommended)
- Or: 
  - **Current enrollment in a teacher preparation program**.
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

` @list:trackoutcomes:advanced_certificate `{=comment}

 - [CK1](#ck1 "Impacts of computing"){.outcome .ck}: Impacts of computing
 - [CK2](#ck2 "Computational thinking"){.outcome .ck}: Computational thinking
 - [CK3](#ck3 "Networks and system design"){.outcome .ck}: Networks and system design
 - [CK4](#ck4 "Cybersecurity"){.outcome .ck}: Cybersecurity
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

The Advanced Certificate consists of five courses and a total of 15 credit hours. 
Courses may be taken in any order and at any pace.

| Course                                                                 | Credits |
| ---------------------------------------------------------------------- | ------- |
| [LAI 515](#lai-515): Action Research to Improve Teaching and Learning  | 3       |
| [LAI 676](#lai-676): The Pedagogy of Programming                       | 3       |
| [LAI 677](#lai-677): Survey of Topics in K12 Computer Science          | 3       |
| [LAI 605](#lai-605): Critical Computational Literacies                 | 3       |
| [LAI 516](#lai-516): Infrastructure for K12 Computing Education        | 3       |

Students with relevant prior experience may substitute a maximum of one course for another course, 
with advisor permission. Additionally, students who complete LAI 515 as part of a UB teacher 
preparation program also satisfy that requirement for the Advanced Certificate Program.

The table below aligns Initial/Professional Certificate Track learning outcomes with courses 
providing summative assessments of this learning.

` @table:alignment:advanced_certificate `{=comment}

```{=html}
<table>
<thead><tr><th class="divider">Outcome</th><th><a href="#lai-515">515</a></th><th><a href="#lai-516">516</a></th><th><a href="#lai-605">605</a></th><th><a href="#lai-676">676</a></th><th><a href="#lai-677">677</a></th></tr></thead>
<tbody>
<tr><td class="divider"><a href="#ck1" class="outcome ck" title="Impacts of computing">CK1</a></td><td></td><td></td><td></td><td><span class="dot ck"></span></td><td><span class="dot ck"></span></td></tr>
<tr><td class="divider"><a href="#ck2" class="outcome ck" title="Computational thinking">CK2</a></td><td></td><td></td><td></td><td><span class="dot ck"></span></td><td><span class="dot ck"></span></td></tr>
<tr><td class="divider"><a href="#ck3" class="outcome ck" title="Networks and system design">CK3</a></td><td></td><td></td><td></td><td></td><td><span class="dot ck"></span></td></tr>
<tr><td class="divider"><a href="#ck4" class="outcome ck" title="Cybersecurity">CK4</a></td><td></td><td></td><td></td><td></td><td><span class="dot ck"></span></td></tr>
<tr><td class="divider"><a href="#pck1" class="outcome pck" title="Computing as a literacy">PCK1</a></td><td></td><td></td><td><span class="dot pck"></span></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck2" class="outcome pck" title="Supporting learner identities">PCK2</a></td><td></td><td></td><td><span class="dot pck"></span></td><td><span class="dot pck"></span></td><td></td></tr>
<tr><td class="divider"><a href="#pck3" class="outcome pck" title="Shaping the learning environment">PCK3</a></td><td><span class="dot pck"></span></td><td></td><td><span class="dot pck"></span></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#pck4" class="outcome pck" title="Teaching with computational media">PCK4</a></td><td></td><td></td><td></td><td><span class="dot pck"></span></td><td></td></tr>
<tr><td class="divider"><a href="#pck5" class="outcome pck" title="Feedback and assessment">PCK5</a></td><td></td><td></td><td></td><td><span class="dot pck"></span></td><td></td></tr>
<tr><td class="divider"><a href="#l1" class="outcome l" title="Equity and opportunity">L1</a></td><td></td><td><span class="dot l"></span></td><td><span class="dot l"></span></td><td></td><td></td></tr>
<tr><td class="divider"><a href="#l2" class="outcome l" title="Connected learning">L2</a></td><td><span class="dot l"></span></td><td><span class="dot l"></span></td><td><span class="dot l"></span></td><td><span class="dot l"></span></td><td></td></tr>
<tr><td class="divider"><a href="#l3" class="outcome l" title="Interdisciplinary connections">L3</a></td><td></td><td><span class="dot l"></span></td><td></td><td></td><td><span class="dot l"></span></td></tr>
<tr><td class="divider"><a href="#l4" class="outcome l" title="Design and research">L4</a></td><td><span class="dot l"></span></td><td><span class="dot l"></span></td><td></td><td></td><td><span class="dot l"></span></td></tr>
</tbody>
</table>
```
```{=latex}
\begin{longtable}{l|ccccc}
\toprule
\textbf{Outcome} & \textbf{\hyperlink{lai-515}{515}} & \textbf{\hyperlink{lai-516}{516}} & \textbf{\hyperlink{lai-605}{605}} & \textbf{\hyperlink{lai-676}{676}} & \textbf{\hyperlink{lai-677}{677}} \\
\midrule
\endhead
\bottomrule
\endlastfoot
\OutcomeBadge{OutcomeCK}{CK1} &  &  &  & \OutcomeDot{OutcomeCK} & \OutcomeDot{OutcomeCK} \\
\OutcomeBadge{OutcomeCK}{CK2} &  &  &  & \OutcomeDot{OutcomeCK} & \OutcomeDot{OutcomeCK} \\
\OutcomeBadge{OutcomeCK}{CK3} &  &  &  &  & \OutcomeDot{OutcomeCK} \\
\OutcomeBadge{OutcomeCK}{CK4} &  &  &  &  & \OutcomeDot{OutcomeCK} \\
\OutcomeBadge{OutcomePCK}{PCK1} &  &  & \OutcomeDot{OutcomePCK} &  &  \\
\OutcomeBadge{OutcomePCK}{PCK2} &  &  & \OutcomeDot{OutcomePCK} & \OutcomeDot{OutcomePCK} &  \\
\OutcomeBadge{OutcomePCK}{PCK3} & \OutcomeDot{OutcomePCK} &  & \OutcomeDot{OutcomePCK} &  &  \\
\OutcomeBadge{OutcomePCK}{PCK4} &  &  &  & \OutcomeDot{OutcomePCK} &  \\
\OutcomeBadge{OutcomePCK}{PCK5} &  &  &  & \OutcomeDot{OutcomePCK} &  \\
\OutcomeBadge{OutcomeL}{L1} &  & \OutcomeDot{OutcomeL} & \OutcomeDot{OutcomeL} &  &  \\
\OutcomeBadge{OutcomeL}{L2} & \OutcomeDot{OutcomeL} & \OutcomeDot{OutcomeL} & \OutcomeDot{OutcomeL} & \OutcomeDot{OutcomeL} &  \\
\OutcomeBadge{OutcomeL}{L3} &  & \OutcomeDot{OutcomeL} &  &  & \OutcomeDot{OutcomeL} \\
\OutcomeBadge{OutcomeL}{L4} & \OutcomeDot{OutcomeL} & \OutcomeDot{OutcomeL} &  &  & \OutcomeDot{OutcomeL} \\
\end{longtable}
```

### Teaching practicum

The Advanced Certificate requires 50 hours of teaching practicum. Students will complete 25 hours of practicum in [LAI 515](#lai-515) and an additional 25 hours in [LAI 516](#lai-516).

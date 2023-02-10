---
title: Alignment of Program Outcomes with New York State Teaching Standards
---

## Appendix I: Alignment of Program Outcomes with New York State Teaching Standards {#appendix-1-tpap}

```{.graphviz caption="Alignment of Program Outcomes with New York State Teaching Standards"}
digraph G {
  rank="max"
  rankdir="LR"

  node [width=4.5]

  rank1 [style=invis]
  rank2 [style=invis]

  ny1 [label="I. Knowledge of Students and Student Learning" shape="box"]
  ny2 [label="II. Knowledge of Content and Instructional Planning" shape="box"]
  ny3 [label="III. Instructional Practice" shape="box"]
  ny4 [label="IV. Learning Environment" shape="box"]
  ny5 [label="V. Assessment for Student Learning" shape="box"]
  ny6 [label="VI. Professional Responsibilities and Collaboration" shape="box"]
  ny7 [label="VII. Professional Growth" shape="box"]

  node [width=3.5]

  ck1 [label="CK1: Impacts of computing" shape="box"]
  ck2 [label="CK2: Computational thinking" shape="box"]
  ck3 [label="CK3: Networks and system design" shape="box"]
  ck4 [label="CK4: Cybersecurity" shape="box"]
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

  ny1 -> pk1;
  ny1 -> pk2;
  ny1 -> pk3;
  ny1 -> pk4;
  ny2 -> ck1;
  ny2 -> ck2;
  ny2 -> ck3;
  ny2 -> ck4;
  ny2 -> pk5;
  ny3 -> pck2;
  ny3 -> pck4;
  ny3 -> l1;
  ny4 -> pck1;
  ny4 -> pck3;
  ny4 -> l2;
  ny5 -> pck5;
  ny6 -> pk6;
  ny6 -> l3;
  ny7 -> l4;

  edge [style=invis];

  rank1 -> rank2;
  ny1 -> ny2 -> ny3 -> ny4 -> ny5 -> ny6 -> ny7;

  subgraph ny {
    rank="same"
    rank1
    ny1
    ny2
    ny3
    ny4
    ny5
    ny6
    ny7
  }
  subgraph ub {
   rank="same"
   rank2
   ck1
   ck2
   ck3 
   ck4
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
   l1
   l2
   l3
   l4
  }
}
```

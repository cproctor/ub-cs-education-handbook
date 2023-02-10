---
title: Alignment of Program Outcomes with CSTA Standards
---

## Appendix II: Alignment of Program Outcomes with CSTA Standards {#appendix-2-csta}

```{.graphviz caption="Alignment of Program Outcomes with CSTA Standards"}
digraph G {
  rank="max"
  rankdir="LR"

  node [width=4.5]

  rank1 [style=invis]
  rank2 [style=invis]

  csta1a [label="1a. Apply CS practices" shape="box"]
  csta1b [label="1b. Apply knowledge of computing systems" shape="box"]
  csta1c [label="1c. Model networks and the Internet" shape="box"]
  csta1d [label="1d. Use and analyze data" shape="box"]
  csta1e [label="1e. Develop programs and interpret algorithms" shape="box"]
  csta1f [label="1f. Analyze impacts of computing " shape="box"]
  csta2a [label="2a. Examine issues of equity in CS" shape="box"]
  csta2b [label="2b. Minimize threats to inclusion" shape="box"]
  csta2c [label="2c. Represent diverse perspectives" shape="box"]
  csta2d [label="2d. Use data for decision-making to improve equity" shape="box"]
  csta2e [label="2e. Use accessible instructional materials " shape="box"]
  csta3a [label="3a. Pursue targeted professional development" shape="box"]
  csta3b [label="3b. Model continuous learning" shape="box"]
  csta3c [label="3c. Examine and counteract personal bias" shape="box"]
  csta3d [label="3d. Commit to the mission of CS for all students" shape="box"]
  csta3e [label="3e. Leverage community resources" shape="box"]
  csta3f [label="3f. Participate in CS professional learning communities" shape="box"]
  csta4a [label="4a. Analyze CS curricula" shape="box"]
  csta4b [label="4b. Develop standards-aligned learning experiences" shape="box"]
  csta4c [label="4c. Design inclusive learning experiences" shape="box"]
  csta4d [label="4d. Build connections between CS and other disciplines" shape="box"]
  csta4e [label="4e. Plan projects that have personal meaning to students" shape="box"]
  csta4f [label="4f. Plan instruction to foster student understanding" shape="box"]
  csta4g [label="4g. Inform instruction through assessment " shape="box"]
  csta5a [label="5a. Use inquiry to facilitate student learning" shape="box"]
  csta5b [label="5b. Cultivate a positive classroom climate" shape="box"]
  csta5c [label="5c. Promote student self-efficacy" shape="box"]
  csta5d [label="5d. Support student collaboration" shape="box"]
  csta5e [label="5e. Encourage student communication" shape="box"]
  csta5f [label="5f. Guide students’ use of feedback" shape="box"]

  node [width=3.5]

  ck1 [label="CK1: Impacts of computing" shape="box"]
  ck2 [label="CK2: Computational thinking" shape="box"]
  ck3 [label="CK3: Networks and system design" shape="box"]
  #ck4 [label="CK4: Cybersecurity" shape="box"]
  #pk1 [label="PK1: Human development" shape="box"]
  #pk2 [label="PK2: Learning" shape="box"]
  pk3 [label="PK3: Supporting students with disabilities" shape="box"]
  pk4 [label="PK4: Language acquisition and literacy" shape="box"]
  pk5 [label="PK5: Curriculum and instruction" shape="box"]
  #pk6 [label="PK6: Professional practice and obligations" shape="box"]
  #pck1 [label="PCK1: Computing as a literacy" shape="box"]
  pck2 [label="PCK2: Supporting learner identities" shape="box"]
  pck3 [label="PCK3: Shaping the learning environment" shape="box"]
  pck4 [label="PCK4: Teaching with computational media" shape="box"]
  pck5 [label="PCK5: Feedback and assessment" shape="box"]
  l1 [label="L1: Equity and opportunity" shape="box"]
  l2 [label="L2: Connected learning" shape="box"]
  l3 [label="L3: Interdisciplinary connections" shape="box"]
  l4 [label="L4: Design and research" shape="box"]

  csta1a -> ck2;
  csta1b -> ck1;
  csta1c -> ck3;
  csta1d -> ck2;
  csta1e -> ck2;
  csta1f -> ck1;
  csta2a -> ck1;
  csta2a -> l1;
  csta2b -> l1;
  csta2c -> l1;
  csta2d -> l4;
  csta2e -> l2;
  csta2e -> l3;
  csta3a -> l4;
  csta3b -> l4;
  csta3c -> l1;
  csta3d -> l1;
  csta3e -> l2;
  csta3f -> l4;
  csta4a -> l4;
  csta4b -> pk5;
  csta4c -> pk3;
  csta4c -> pk4;
  csta4c -> pk5;
  csta4c -> pck2;
  csta4d -> l3;
  csta4e -> pck2;
  csta4e -> l2;
  csta4f -> pk5;
  csta4f -> pck4;
  csta4g -> pck5;
  csta5a -> l2;
  csta5b -> pck3;
  csta5c -> pck2;
  csta5d -> pck4;
  csta5e -> pck2;
  csta5e -> pck3;
  csta5e -> l3;
  csta5f -> pck5;

  edge [style=invis];

  rank1 -> rank2;
  csta1a -> csta1b -> csta1c -> csta1d -> csta1e -> csta1f -> csta2a -> csta2b -> csta2c -> csta2d -> csta2e -> csta3a -> csta3b -> csta3c -> csta3d -> csta3e -> csta3f -> csta4a -> csta4b -> csta4c -> csta4d -> csta4e -> csta4f -> csta5a -> csta5b -> csta5c -> csta5d -> csta5e -> csta5f;

  subgraph csta {
    rank="same"
    rank1
    csta1a
    csta1b
    csta1c
    csta1d
    csta1e
    csta1f
    csta2a
    csta2b
    csta2c
    csta2d
    csta2e
    csta3a
    csta3b
    csta3c
    csta3d
    csta3e
    csta3f
    csta4a
    csta4b
    csta4c
    csta4d
    csta4e
    csta4f
    csta4g
    csta5a
    csta5b
    csta5c
    csta5d
    csta5e
    csta5f
  }
  subgraph ub {
   rank="same"
   rank2
   ck1
   ck2
   ck3 
   #ck4
   pk3
   pk4
   pk5
   #pk9
   #pck1
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

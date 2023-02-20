# eng.dep.scidtb

SciDTB: Discourse Dependency TreeBank for Scientific Abstracts

The following information about the dataset is extracted from the original paper.

## Introduction

SciDTB is a domain-specific discourse treebank annotated on scientific articles. Different from widely-used RST-DT and PDTB, SciDTB uses dependency trees to represent discourse structure, which is flexible and simplified to some extent but do not sacrifice structural integrity.

The corpus contains 798 unique abstracts from ACL anthology, and 18,978 discourse relations in total.

The dataset is publicly available at: https://github.com/PKU-TANGENT/SciDTB 

### Notes on Discourse Segmentation

Discourse Segmentation follows the criterion of Polanyi (1988) and Irmer (2011) which treats clauses as EDUs.
However, since a discourse unit is a semantic concept but a clause is defined syntactically, in some cases segmentation by clauses is still not the most proper strategy. In practice, we refer to the guidelines defined by (Carlson and Marcu, 2001). For example, subjective clauses, objective clauses of non-attributive verbs and verb complement clauses are not segmented. Nominal post- modifiers with predicates are treated as EDUs.
Strong discourse cues such as “despite” and “because of ” starts a new EDU no matter they are followed by a clause or a phrase

### Notes on Discourse Relations 

A discourse relation is defined as tri-tuple (h, d, r), where h means the head EDU, d is the
dependent EDU, and r defines the relation category between h and d. For a discourse relation, head EDU is defined as the unit with essential information and dependent EDU with supportive content. Here, we follow Carlson and Marcu (2001) to adopt deletion test in the determination of head and dependent.

For the relation categories, the authors mainly refer to the work of (Carlson and Marcu, 2001) and (Bunt
and Prasad, 2016).
The corpus is annotated with 17 coarse-grained relation types and 26 fine-grained relations.

It is noted that some modifications were made to adapt to the scientific domain. For example, In
SciDTB, Background relation is divided into three subtypes: Related, Goal, and General, because the
background description in scientific abstracts usually has more different intents. 

## DISRPT 2023 Shared Task Information

For the 2023 shared task, the original split from the authors is adopted, 
with 492 documents in the `train` set, 154 in the `dev` set, and 152 in the `test` set. 

Data has been tokenized, split into sentences, POS tagged, and parsed using Stanza.


## References

[SciDTB: Discourse Dependency TreeBank for Scientific Abstracts](https://aclanthology.org/P18-2071/) (Yang & Li, ACL 2018)
```
@inproceedings{yang-li-2018-scidtb,
    title = "{S}ci{DTB}: Discourse Dependency {T}ree{B}ank for Scientific Abstracts",
    author = "Yang, An  and
      Li, Sujian",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P18-2071",
    doi = "10.18653/v1/P18-2071",
    pages = "444--449",
    abstract = "Annotation corpus for discourse relations benefits NLP tasks such as machine translation and question answering. In this paper, we present SciDTB, a domain-specific discourse treebank annotated on scientific articles. Different from widely-used RST-DT and PDTB, SciDTB uses dependency trees to represent discourse structure, which is flexible and simplified to some extent but do not sacrifice structural integrity. We discuss the labeling framework, annotation workflow and some statistics about SciDTB. Furthermore, our treebank is made as a benchmark for evaluating discourse dependency parsers, on which we provide several baselines as fundamental work.",
}

```

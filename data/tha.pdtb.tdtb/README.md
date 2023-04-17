#tha.pdtb.tdtb

## Introduction
The Thai Discourse Treebank (TDTB) is a project at Chulalongkorn University, Bangkok, Thailand. The annotation adopts the sense inventory from PDTB 3.0. 


## Data 
The documents are sampled from the LST20 corpus (Boonkrwan et al., 2020). The text consists of news articles in various genres. In the LST20 corpus, the word segmentation, sentence segmentation, and POS tags are manually annotated as part of the original LST20 corpus. 

This corpus consists 180 documents annotated with explicit discourse relations and the accompanying two argument spans. The total number of relations is 10,868 relations.

| Split | Relations |
|-------|-----------|
| train | 8279 |
| dev | 1244 |
| test | 1345 |
| *total* | 10868 | 

We trained a dependency parser using MALT parser trained on UD-Thai (aka Universal Dependency) dependency treebank. To the best of our knowledge, there exists no off-the-shelf dependency parser for Thai, and the UD-Thai treebank is the largest publicly available treebank. The parser is trained on gold-standard word tokenization and part-of-speech tags remapped to the UD POS tag scheme. The 5-fold crossvalidated unlabled attachment score (UAS) is 0.81, and labeled attachment score (LAS) is 0.73. 

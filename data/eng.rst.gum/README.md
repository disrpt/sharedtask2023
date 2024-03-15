# eng.rst.gum

### The Georgetown University Multilayer (GUM) Corpus: v.9.

To cite this corpus, please refer to the following article:

Zeldes, Amir (2017) "The GUM Corpus: Creating Multilayer Resources in the Classroom".
Language Resources and Evaluation 51(3), 581–612.

```
@Article{Zeldes2017,
author    = {Amir Zeldes},
title     = {The {GUM} {C}orpus: Creating Multilayer Resources in the Classroom},
journal   = {Language Resources and Evaluation},
year      = {2017},
volume    = {51},
number    = {3},
pages     = {581--612},
doi       = {http://dx.doi.org/10.1007/s10579-016-9343-x}
}
```

## Introduction

GUM v9 is a corpus of English texts from twelve text types:

- Interviews from Wikimedia
- News from Wikinews
- Travel guides from Wikivoyage
- How-to guides from wikiHow
- Academic writing from Creative Commons sources
- Biographies from Wikipedia
- Fiction from Creative Commons sources
- Online forum discussions from Reddit
- Face-to-face conversations from the Santa Barbara Corpus
- Political speeches
- OpenStax open access textbooks
- YouTube Creative Commons vlogs

The corpus is created as part of the course LING-367 (Computational Corpus Linguistics) at Georgetown University.

For more details see: https://gucorpling.org/gum

## DISRPT 2023 Shared Task Information

For the DISRPT 2023 shared task on elementary discourse unit segmentation,
only 11 open text genres are included with plain text, while the remaining genre,
containing Reddit forum discussions, **must be reconstructed** using the script
in `utils/process_underscores.py` (see main repository README).
The data follows the established `train`, `dev`, and `test` partitions used for other tasks
(e.g. for the conll shared task on UD parsing), which can be found [here](https://github.com/amir-zeldes/gum/blob/master/splits.md).

POS tags and syntactic parses are manually annotated gold data.

### Notes on Segmentation

GUM RST guidelines follow the RST-DT segmentation guidelines for English,
according to which most clauses,
including adnominal and nested clauses are discourse units.
This dataset contains discontinuous discourse units (split 'same-unit').
Note that the `.conllu` data contains some reconstructed ellipsis tokens with
decimal IDs (e.g. 12.1); these do not appear in the other formats and are ignored in token
index spans.


### Notes on Relation Classification
GUM v9 data contains 32 fine-grained relation labels and 15 coarse-grained relation classes.
The coarse-grained relation classes are the target labels to predict
(and thus are provided in the `label` column) while the fine-grained
relation labels are provided in the `orig_label` column for reference.

A full list of the relation inventory and definitions of individual relations
can be found [here](https://wiki.gucorpling.org/gum/rst).

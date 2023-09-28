# GENTLE

Repository for the Genre Tests for Linguistic Evaluation (GENTLE) Corpus

This repository contains release versions of the Genre Tests for Linguistic Evaluation (GENTLE) corpus, an English out-of-domain test set following the same multilayer annotations found in the [GUM corpus](https://gucorpling.org/gum/). The texts are of the following 8 genres:

* dictionary entries
* live esports commentary
* legal documents
* medical notes
* poetry
* mathematical proofs
* course syllabuses
* threat letters

## Splits - test only

The entire corpus is designed to be a *test set* of challenging genres for NLP systems to be evaluated on. Although one can train a model on this corpus, or concatenate it to another training set, we present this entire corpus as a test set, and do not provide any official train / dev data.

## Citing

To cite this corpus in general, please refer to the following article: (TBA)
<!--

Zeldes, Amir (2017) "The GUM Corpus: Creating Multilayer Resources in the Classroom". Language Resources and Evaluation 51(3), 581–612.

```
@Article{Zeldes2017,
author    = {Amir Zeldes},
title     = {The {GUM} Corpus: Creating Multilayer Resources in the Classroom},
journal   = {Language Resources and Evaluation},
year      = {2017},
volume    = {51},
number    = {3},
pages     = {581--612},
doi       = {http://dx.doi.org/10.1007/s10579-016-9343-x}
}
```
-->

## Directories

The corpus is downloadable in multiple formats. Not all formats contain all annotations: The most accessible format is probably CoNLL-U dependencies (in `dep/`), but the most complete XML representation is in [PAULA XML](https://www.sfb632.uni-potsdam.de/en/paula.html), and the easiest way to search in the corpus is using [ANNIS](http://corpus-tools.org/annis). Here is [an example query](https://gucorpling.org/annis/#_q=ZW50aXR5IC0-YnJpZGdlIGVudGl0eSAmICMxIC0-aGVhZCBsZW1tYT0ib25lIg&_c=R1VN&cl=5&cr=5&s=0&l=10) for phrases headed by 'one' bridging back to a different, previously mentioned entity. Other formats may be useful for other purposes. See website for more details.

* _build/ - The [GUM build bot](https://gucorpling.org/gum/build.html) and utilities for data merging and validation
* annis/ - The entire merged corpus, with all annotations, as a relANNIS 3.3 corpus dump, importable into [ANNIS](http://corpus-tools.org/annis)
* const/ - Constituent trees with function labels and PTB POS tags in the PTB bracketing format (automatic parser output from gold POS with functions projected from gold dependencies)
* coref/ - Entity and coreference annotation in two formats:
* conll/ - CoNLL shared task tabular format (with Wikification but no bridging or split antecedent annotations)
* tsv/ - WebAnno .tsv format, including entity type, salience and information status annotations, Wikification, bridging, split antecedent and singleton entities
* ontogum/ - alternative version of coreference annotation in CoNLL, tsv and CoNLL-U formats following OntoNotes guidelines (see Zhu et al. 2021)
* dep/ - Dependency trees using Universal Dependencies, enriched with metadata, sentence types, speaker information,  enhanced dependencies, entities, information status, salience, centering, coreference, bridging, Wikification, XML markup, morphological tags and Universal POS tags according to the UD standard
* paula/ - The entire merged corpus in standoff [PAULA XML](https://github.com/korpling/paula-xml), with all annotations
* rst/ - Rhetorical Structure Theory analyses
* rstweb/ - full .rs3 format data as used by RSTTool and rstWeb (recommended)
* lisp_nary/ - n-ary lisp trees (.dis format)
* lisp_binary/ - binarized lisp trees (.dis format)
* dependencies/ - a converted RST dependency representation (.rsd format)
* disrpt/ - plain segmentation and relation-per-line data formats following the DISRPT shared task specification
* xml/ - vertical XML representations with 1 token or tag per line, metadata, and tab delimited lemmas and POS tags (extended VVZ style, vanilla, UPOS and CLAWS5, as well as dependency functions), compatible with the IMS Corpus Workbench (a.k.a. TreeTagger format).

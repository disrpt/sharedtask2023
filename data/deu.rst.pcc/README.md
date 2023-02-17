# deu.rst.pcc

The Potsdam Commenraty Corpus

Citation: Stede, Manfred and A. Neumann (2014). Potsdam Commentary Corpus 2.0: Annotation for Discourse Research. Proc. of the Language Resources and Evaluation Conference (LREC), Reykjavik.

Please cite this paper if publishing separately about the data.

## Introduction

The Potsdam Commentary Corpus or PCC was assembled by Dr. Manfred Stede and his colleagues at the Department of Linguistics, University of Potsdam. The PCC contains 176 German newspaper commentaries, which are annotated with syntax trees and three layers of discourse-level information: nominal coreference, connectives and their arguments (similar to the PDTB), and trees reflecting discourse structure according to Rhetorical Structure Theory (Mann and Thompson, 1988).

In the RST framework (Mann and Thompson, 1988), a text's discourse structure can be represented as a tree in four aspects: 

  1. the leaves correspond to text fragments called elementary discourse units (the mininal discourse units); 
  2. the internal nodes of the tree correspond to contiguous text spans; 
  3. each node is characterized by its nuclearity, or essential unit of information; and 
  4. each node is also characterized by a rhetorical relation between two or more non-overlapping, adjacent text spans.

See: http://angcl.ling.uni-potsdam.de/resources/pcc.html

## DISRPT 2023 shared task information

For the DISRPT 2023 shared tasks, the data is divided into train, test and dev partitions, comprising 142, 17 and 17 documents, respectively. There are no discontinuous discourse units in the data.

For relation classification, sparse some sparse original labels were collapsed into more common categories recommended by the corpus designers, as follows:

  * enablement => background
  * justify => reason
  * motivation => reason
  * otherwise => antithesis
  * unless => antithesis 

The original labels are retained in .rels files under `orig_label`; for the shared task, the final `label` column should be predicted.

Syntactic (automatic) dependency parses are made available using Stanza with the 2.7 GSD model for German, but xpos tags are taken from the original PCC corpus STTS tags, and are therefore not harmonized with the universal upos tags column. Due to the original tokenization of the corpus, fused tokens such as 'im', 'ins' etc. are retained in the data without CoNLL-U super-tokens, and are given the appropriate STTS tags (e.g. APPRART).

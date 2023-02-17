# por.pdtb.crpc

Portuguese Discourse Bank

## Introduction

The CRPC-DB is a Discourse Bank for Portuguese annotated according to the Penn Discourse Treebank scheme (Prasad et al., 2008). The corpus is labeled for discourse relations (also referred to as rhetorical relations or coherence relations), such as cause and condition, that hold between two spans of text and contribute to ensure the overall cohesion and coherence. The scheme follows the principles of the PDTB 2.0 annotation proposal and the PDTB 3.0 sense hierarchy (Webber et al., 2016). The annotation is applied over 319 files of the PAROLE corpus, a subset of the Reference Corpus of Contemporary Portuguese (CRPC) (Généreux et al., 2012). The files are newspaper, fiction and didactic/scientific texts.

The corpus contains the annotation of Explicit, Implicit, AltLex, EntRel and NoRel, for a total of 14,579 annotations.

More information at: https://www.clul.ulisboa.pt/en/recurso/portuguese-discourse-bank


## DISRPT 2023 shared task information

The texts were tokenized using the LX-tokenizer which separates punctuation marks from words, detects sentence boundaries and deals with contracted forms and clitics in Portuguese.
Sentence segmentation, POS tagging and syntactic parses were obtained using Stanza.

The corpus was not originally split into a train / dev / test partition. We thus split this corpus based on their genre, trying to have different genres in each split, if they represent at least 3 documents.
In the end, we have: newspaper articles propotionally appearing in each split, 1 technical in dev and 1 in test, as well as 1 fiction in each partition, and ‘varia’ only in train.

## References

Mendes, Amália & Pierre Lejeune (2022). CRPC-DB – A Discourse Bank for Portuguese. In Computational Processing of the Portuguese Language PROPOR 2022 (pp. 79-89). Berlin, Heidelberg: Springer. http://hdl.handle.net/10451/54255

Généreux, M., Hendrickx, I., and Mendes, A. (2012). Introducing the reference corpus of contemporary portuguese on-line. In Nicoletta Calzolari, et al., editors, LREC’2012 – Eighth International Conference on Language Resources and Evaluation, pages 2237–2244, Istanbul,Turkey, May. European Language Resources Association (ELRA).

Prasad, R., Dinesh, N., Lee, A., Miltsakaki, E., Robaldo, L., Joshi, A. K., and Webber, B. L. (2008). The Penn Discourse Treebank 2.0. In LREC2008.

Webber, B., Prasad, R., Lee, A., and Joshi, A. (2016). A discourse-annotated corpus of conjoined VPs. In Proceedings of the 10th Linguistics Annotation Workshop, pages 22–31.

The licence for this corpus is: license is Creative Commons CC BY-NC-ND 4.0

# por.pdtb.crpc

### Portuguese Discourse Bank

## Introduction

The CRPC-DB is a Discourse Bank for Portuguese annotated according to the Penn Discourse Treebank scheme (Prasad et al., 2008). The corpus is labeled for discourse relations (also referred to as rhetorical relations or coherence relations), such as cause and condition, that hold between two spans of text and contribute to ensure the overall cohesion and coherence. The scheme follows the principles of the PDTB 2.0 annotation proposal and the PDTB 3.0 sense hierarchy (Webber et al., 2016). The annotation is applied over 319 files of the PAROLE corpus, a subset of the Reference Corpus of Contemporary Portuguese (CRPC) (Généreux et al., 2012). The files are newspaper, fiction and didactic/scientific texts.

The corpus contains the annotation of Explicit, Implicit, AltLex, EntRel and NoRel, for a total of 14,579 annotations.

More information at: https://www.clul.ulisboa.pt/en/recurso/portuguese-discourse-bank


## DISRPT 2023 Shared Task Information

The texts were tokenized using the LX-tokenizer which separates punctuation marks from words, splits into sentences and deals with contracted forms and clitics in Portuguese.
POS tagging and syntactic parses were obtained using Stanza.

As for the others datasets in this shared task, EntRel and NoRel are not integrated.

The corpus was not originally split into a `train` / `dev` / `test` partition. We thus split this corpus based on their genre, trying to have different genres in each split, if they represent at least 3 documents. For this task, some documents are not integrated.
In the end, we have: 
- newspaper articles propotionally appearing in each split, 
- 1 fiction in each partition, and ‘varia’ only in `train`.


## References

Mendes, Amália & Pierre Lejeune (2022).[ CRPC-DB – A Discourse Bank for Portuguese](https://dl.acm.org/doi/abs/10.1007/978-3-030-98305-5_8). In Computational Processing of the Portuguese Language PROPOR 2022 (pp. 79-89). Berlin, Heidelberg: Springer. http://hdl.handle.net/10451/54255
```
@inproceedings{CRPC-DB-Portuguese,
author = {Mendes, Am\'{a}lia and Lejeune, Pierre},
title = {CRPC-DB a Discourse Bank for Portuguese},
year = {2022},
isbn = {978-3-030-98304-8},
publisher = {Springer-Verlag},
address = {Berlin, Heidelberg},
url = {https://doi.org/10.1007/978-3-030-98305-5_8},
doi = {10.1007/978-3-030-98305-5_8},
abstract = {We present a new resource for discourse studies in Portuguese, the CRPC Discourse Bank (CRPC-DB). CRPC-DB follows the Penn Discourse Treebank style of annotation. The annotation is performed on the PAROLE corpus, a free subset of the Reference Corpus of Contemporary Portuguese (CRPC) that includes news, fiction and didactic/scientific texts. The discourse bank covers explicit and implicit relations at intra and inter-sentential levels, and includes for now a total of 14,436 discourse relations. We present the main guidelines of our annotation and discuss specific cases. An experiment in inter-annotator agreement was performed and holds results of 0.88 F1-score for discourse relation identification, 0.71 Cohen’s K for the classification of discourse relation types, and 0,75 for top-level sense classification. The CRPC-DB will be distributed free of charge through the PORTULAN CLARIN infrastructure.},
booktitle = {Computational Processing of the Portuguese Language: 15th International Conference, PROPOR 2022, Fortaleza, Brazil, March 21–23, 2022, Proceedings},
pages = {79–89},
numpages = {11},
keywords = {Discourse bank, Text coherence, PDTB-style of annotation, Discourse relations},
location = {Fortaleza, Brazil}
}
```


Généreux, M., Hendrickx, I., and Mendes, A. (2012). [Introducing the reference corpus of contemporary portuguese on-line](https://aclanthology.org/L12-1143/). In Nicoletta Calzolari, et al., editors, LREC’2012 – Eighth International Conference on Language Resources and Evaluation, pages 2237–2244, Istanbul,Turkey, May. European Language Resources Association (ELRA).
```
@inproceedings{genereux-etal-2012-introducing,
    title = "Introducing the Reference Corpus of Contemporary {P}ortuguese Online",
    author = "G{\'e}n{\'e}reux, Michel  and
      Hendrickx, Iris  and
      Mendes, Am{\'a}lia",
    booktitle = "Proceedings of the Eighth International Conference on Language Resources and Evaluation ({LREC}'12)",
    month = may,
    year = "2012",
    address = "Istanbul, Turkey",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2012/pdf/309_Paper.pdf",
    pages = "2237--2244",
    abstract = "We present our work in processing the Reference Corpus of Contemporary Portuguese and its publication online. After discussing how the corpus was built and our choice of meta-data, we turn to the processes and tools involved for the cleaning, preparation and annotation to make the corpus suitable for linguistic inquiries. The Web platform is described, and we show examples of linguistic resources that can be extracted from the platform for use in linguistic studies or in NLP.",
}
```


Prasad, R., Dinesh, N., Lee, A., Miltsakaki, E., Robaldo, L., Joshi, A. K., and Webber, B. L. (2008). [The Penn Discourse Treebank 2.0](https://aclanthology.org/L08-1093/). In LREC2008.
```
@inproceedings{prasad-etal-2008-penn,
    title = "The {P}enn {D}iscourse {T}ree{B}ank 2.0.",
    author = "Prasad, Rashmi  and
      Dinesh, Nikhil  and
      Lee, Alan  and
      Miltsakaki, Eleni  and
      Robaldo, Livio  and
      Joshi, Aravind  and
      Webber, Bonnie",
    booktitle = "Proceedings of the Sixth International Conference on Language Resources and Evaluation ({LREC}'08)",
    month = may,
    year = "2008",
    address = "Marrakech, Morocco",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2008/pdf/754_paper.pdf",
    abstract = "We present the second version of the Penn Discourse Treebank, PDTB-2.0, describing its lexically-grounded annotations of discourse relations and their two abstract object arguments over the 1 million word Wall Street Journal corpus. We describe all aspects of the annotation, including (a) the argument structure of discourse relations, (b) the sense annotation of the relations, and (c) the attribution of discourse relations and each of their arguments. We list the differences between PDTB-1.0 and PDTB-2.0. We present representative statistics for several aspects of the annotation in the corpus.",
}
```


Webber, B., Prasad, R., Lee, A., and Joshi, A. (2016). [A discourse-annotated corpus of conjoined VPs](https://aclanthology.org/W16-1704/). In Proceedings of the 10th Linguistics Annotation Workshop, pages 22–31.
```
@inproceedings{webber-etal-2016-discourse,
    title = "A Discourse-Annotated Corpus of Conjoined {VP}s",
    author = "Webber, Bonnie  and
      Prasad, Rashmi  and
      Lee, Alan  and
      Joshi, Aravind",
    booktitle = "Proceedings of the 10th Linguistic Annotation Workshop held in conjunction with {ACL} 2016 ({LAW}-X 2016)",
    month = aug,
    year = "2016",
    address = "Berlin, Germany",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W16-1704",
    doi = "10.18653/v1/W16-1704",
    pages = "22--31",
}
```


### Licence
The licence for this corpus is `Creative Commons CC BY-NC-ND 4.0`. 

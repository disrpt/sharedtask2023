# tur.pdtb.tdb

### Turkish Discourse Bank 1.0 & Turkish Discourse Bank 1.1 

## Introduction  

Turkish Discourse Bank 1.0 is a 400,000-word corpus funded by TÜBİTAK (The Scientific and Technological Research Council of Turkey) annotated in the PDTB style. For more information regarding TDB, please visit: http://medid.ii.metu.edu.tr/theCorpus.html. TDB 1.0 contains explicit discourse connectives as well phrasal expressions based on postpositions, i.e: 

- conjunctions such as 've' (and), 'ama' (but), etc. 
- adverbials such as 'aksine' (to the contrary),
- postpositions such as için 'for' (conveying the purpose or reason sense), 
- phrasal expressions such as 'bunun için' (for this reason).

Postpositions are single word connectives and they always appear after the verb of the syntactically dependent argument. The phrasal expressions annotated in TDB 1.0 are derived from postpositions and mostly contain a deictic element such as 'bu' (this), 'o' (that). Phrasal expressions are a sub-type of alternative lexicalizations.   

As in the PDTB, in TDB,

- explicit connectives may be continuous or discontinuous, as in 've' (and), 'hem ... hem' (both ... and), 
- explicit connectives may be pre-modified as in 'tam aksine' (just to the contrary); they may also be post-modified as in 'sanki ... gibi' (as if)
- phrasal expressions may be pre-modified, as in 'ancak bundan sonra' (only after this), or they may be post-modified by a focus particle, as in 'bu amaçla da' (for this reason - focus particle). 

Turkish Discourse Bank 1.1 (TDB 1.1) is an extension on the Turkish Discourse Bank 1.0. TDB 1.1 added sense annotations to a subset of the Turkish Discourse Bank 1.0 (10% of the corpus, 20 documents), which consists of the content of the relation classification task for Turkish. Please refer to the paper titled "TDB 1.1: Extensions on Turkish Discourse Bank" (https://www.aclweb.org/anthology/W17-0809/) for more details. 


## DISRPT 2023 Shared Task Information

The data was automatically parsed using the UDPipe Turkish model (https://github.com/jwijffels/udpipe.models.ud.2.0/blob/master/inst/udpipe-ud-2.0-170801/turkish-ud-2.0-170801.udpipe). 

### Obtaining the Text

Since the underlying texts cannot be placed openly online, the shared task data has replaced token information with underscores. To reconstruct the data, users must obtain the raw texts by filling in the user agreement form (`tdb_shared_task_user_agreement.docx`) which they email to `corpora@metu.edu.tr` and run the Python script in `utils/process_underscores.py tdb -m add`. For more details, run `python utils/process_underscores.py -h`.


### Notes on Relation Classification

1. Only a subset of the TDB 1.0 is used for the relation classification. Not all documents used in the segmentation and connective detection tasks will be found in the .rels files. 
2. In addition to the inventory of the sense labels used in PDTB3 for English, there are three Level-2 sense labels developed for TDB1.1: Comparison.Degree, Expansion.Manner, and Expansion.Correction. For more details, please refer to the paper (https://www.aclweb.org/anthology/W17-0809/). 
3. The predicted label (the last column) for each instance has been truncated at Level-2. For instance, the predicted label for the sense label “Temporal.Asynchronous.Precedence” would be “Temporal.Asynchronous”. However, we keep the original label in the third-to-last column called “orig_label”, which matches the directionality information provided in the “dir” column. Moreover, when there are multiple sense labels available, the sense label that has a lower frequency (the frequency is based on Level-2 relations) is chosen as the sense label to predict, and the directionality information thus corresponds to this chosen sense. Both sense labels are included in the “orig_label”, separated by a semicolon.

This dataset contains discontinuous discourse units.

## Notes

A list of all explicit connectives and phrasal expressions annotated in TDB 1.0 can be found in Demirşahin and Zeyrek (2017). 

An introduction to TDB can be found in Zeyrek and Webber (2008)

The full tag set of TDB can be found in Zeyrek et al. (2013)

The list of all modifiers can be found in Çakmak (2015). 


## References

Zeyrek, D., & Kurfalı, M. (2017, April). [TDB 1.1: Extensions on Turkish discourse bank](https://aclanthology.org/W17-0809/). In Proceedings of the 11th Linguistic Annotation Workshop (pp. 76-81).
```
@inproceedings{zeyrek-kurfali-2017-tdb,
    title = "{TDB} 1.1: Extensions on {T}urkish Discourse Bank",
    author = "Zeyrek, Deniz  and
      Kurfal{\i}, Murathan",
    booktitle = "Proceedings of the 11th Linguistic Annotation Workshop",
    month = apr,
    year = "2017",
    address = "Valencia, Spain",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-0809",
    doi = "10.18653/v1/W17-0809",
    pages = "76--81",
    abstract = "This paper presents the recent developments on Turkish Discourse Bank (TDB). First, the resource is summarized and an evaluation is presented. Then, TDB 1.1, i.e. enrichments on 10{\%} of the corpus are described (namely, senses for explicit discourse connectives, and new annotations for three discourse relation types - implicit relations, entity relations and alternative lexicalizations). The method of annotation is explained and the data are evaluated.",
}
```

Zeyrek, D., & Kurfalı, M. (2018, May). [An assessment of explicit inter-and intra-sentential discourse connectives in Turkish Discourse Bank](https://aclanthology.org/L18-1634/). In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).
```
@inproceedings{zeyrek-kurfali-2018-assessment,
    title = "An Assessment of Explicit Inter- and Intra-sentential Discourse Connectives in {T}urkish Discourse Bank",
    author = "Zeyrek, Deniz  and
      Kurfal{\i}, Murathan",
    booktitle = "Proceedings of the Eleventh International Conference on Language Resources and Evaluation ({LREC} 2018)",
    month = may,
    year = "2018",
    address = "Miyazaki, Japan",
    publisher = "European Language Resources Association (ELRA)",
    url = "https://aclanthology.org/L18-1634",
}
```

Çakmak, Deniz Hande. (2015). [The Role of Modifiers in Turkish Discourse Bank](https://open.metu.edu.tr/handle/11511/25017). Unpublished MS Thesis. Middle East Technical University, Cognitive Science Department. 
```
@mastersthesis{çakmak_2015, 
    title={The Role of modifiers in Turkish discourse bank}, 
    school={Middle East Technical University}, 
    author={Çakmak, Deniz Hande}, year={2015},
    }
```

Demirşahin, I., & Zeyrek, D. (2017). Pair annotation as a novel annotation procedure: The case of Turkish Discourse Bank. In Handbook of Linguistic Annotation (pp. 1219-1240). Springer, Dordrecht.
```
@Inbook{Demirşahin2017,
    author="Demir{\c{s}}ahin, I{\c{s}}{\i}n
    and Zeyrek, Deniz",
    editor="Ide, Nancy
    and Pustejovsky, James",
    title="Pair Annotation as a Novel Annotation Procedure: The Case of Turkish Discourse Bank",
    bookTitle="Handbook of Linguistic Annotation",
    year="2017",
    publisher="Springer Netherlands",
    address="Dordrecht",
    pages="1219--1240",
    abstract="In this chapter, we provide an overview of Turkish Discourse Bank, a resource of {\$}{\$}{\backslash}sim {\$}{\$}400,000 words built on a sub-corpus of the 2-million-word METU Turkish Corpus annotated following the principles of Penn Discourse Tree Bank. We first present the annotation framework we adopted, explaining how it differs from the annotation of the original language, English. Then we focus on a novel annotation procedure that we have devised and named pair annotation after pair programming. We discuss the advantages it has offered as well as its potential drawbacks.",
    isbn="978-94-024-0881-2",
    doi="10.1007/978-94-024-0881-2_46",
    url="https://doi.org/10.1007/978-94-024-0881-2_46",
}
```

Zeyrek, D., Demirşahin, I., Sevdik-Çallı, A. B., & Çakıcı, R. (2013). [Turkish Discourse Bank: Porting a discourse annotation style to a morphologically rich language](https://journals.uic.edu/ojs/index.php/dad/article/view/10772). D&D, 4(2), 174-184.
```
@article{zeyrek bozşahin_sevdik çallı_çakıcı_2013, 
    title={Turkish Discourse Bank: Porting a discourse annotation style to a morphologically rich language}, 
    url={https://hdl.handle.net/11511/32505}, 
    journal={Dialogue and Discourse}, 
    author={Zeyrek Bozşahin, Deniz and Sevdik Çallı, Ayışığı B. and Çakıcı, Ruket}, 
    year={2013}, 
    pages={174–184},
}
```

Zeyrek, D., & Webber, B. (2008). [A discourse resource for Turkish: Annotating discourse connectives in the METU corpus](https://aclanthology.org/W14-4916/). In Proceedings of the 6th workshop on Asian language resources.
```
@inproceedings{demirsahin-zeyrek-2014-annotating,
    title = "Annotating Discourse Connectives in Spoken {T}urkish",
    author = "Demir{\c{s}}ahin, Isin  and
      Zeyrek, Deniz",
    booktitle = "Proceedings of {LAW} {VIII} - The 8th Linguistic Annotation Workshop",
    month = aug,
    year = "2014",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics and Dublin City University",
    url = "https://aclanthology.org/W14-4916",
    doi = "10.3115/v1/W14-4916",
    pages = "105--109",
}
```
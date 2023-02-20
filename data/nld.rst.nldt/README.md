# nld.rst.nldt

### Dutch Discourse Treebank (NLDT)

## Description

Citation: Gisela Redeker, Ildikó Berzlánovich, Nynke van der Vliet, Gosse Bouma and Markus Egg (2012). [Multi-Layer Discourse Annotation of a Dutch Text Corpus](https://aclanthology.org/L12-1528/). In: Proceedings of LREC 2012. Istanbul, Turkey, 2820-2825.
```
@inproceedings{redeker-etal-2012-multi,
    title = "Multi-Layer Discourse Annotation of a {D}utch Text Corpus",
    author = "Redeker, Gisela  and
      Berzl{\'a}novich, Ildik{\'o}  and
      van der Vliet, Nynke  and
      Bouma, Gosse  and
      Egg, Markus",
    booktitle = "Proceedings of the Eighth International Conference on Language Resources and Evaluation ({LREC}'12)",
    month = may,
    year = "2012",
    address = "Istanbul, Turkey",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2012/pdf/887_Paper.pdf",
    pages = "2820--2825",
    abstract = "We have compiled a corpus of 80 Dutch texts from expository and persuasive genres, which we annotated for rhetorical and genre-specific discourse structure, and lexical cohesion with the goal of creating a gold standard for further research. The annota{\^A}{\neg}tions are based on a segmentation of the text in elementary discourse units that takes into account cues from syntax and punctuation. During the labor-intensive discourse-structure annotation (RST analysis), we took great care to thoroughly reconcile the initial analyses. That process and the availability of two independent initial analyses for each text allows us to analyze our disagreements and to assess the confusability of RST relations, and thereby improve the annotation guidelines and gather evidence for the classification of these relations into larger groups. We are using this resource for corpus-based studies of discourse relations, discourse markers, cohesion, and genre differences, e.g., the question of how discourse structure and lexical cohesion interact for different genres in the overall organization of texts. We are also exploring automatic text segmentation and semi-automatic discourse annotation.",
}
```


NLDT is a corpus of 80 Dutch texts from expository texts (encyclopedias and science news web pages) and persuasive genres (fund-raising letters and commercial advertisements), which were annotated for rhetorical and genre-specific discourse structure, and lexical cohesion with the goal of creating a gold standard for further research. The annotations are based on a segmentation of the texts into elementary discourse units that takes into account cues from syntax and punctuation.  

## DISRPT 2023 Shared Task Information

For the DISRPT 2023 shared task, `train`/`dev`/`test` partitions were balanced for genre. 
Syntactic parses in UD were produced using Stanza. 

The data contains no split EDUs, which were prevented in a handful of cases through some reordering of clauses in the original RST data. These segment orders were retained in the 2023 shared task data.

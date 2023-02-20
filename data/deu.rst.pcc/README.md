# deu.rst.pcc

### The Potsdam Commenraty Corpus


## Introduction

The Potsdam Commentary Corpus or PCC was assembled by Dr. Manfred Stede and his colleagues at the Department of Linguistics, University of Potsdam. The PCC contains 176 German newspaper commentaries, which are annotated with syntax trees and three layers of discourse-level information: nominal coreference, connectives and their arguments (similar to the PDTB), and trees reflecting discourse structure according to Rhetorical Structure Theory (Mann and Thompson, 1988).

In the RST framework (Mann and Thompson, 1988), a text's discourse structure can be represented as a tree in four aspects: 

  1. the leaves correspond to text fragments called elementary discourse units (the mininal discourse units); 
  2. the internal nodes of the tree correspond to contiguous text spans; 
  3. each node is characterized by its nuclearity, or essential unit of information; and 
  4. each node is also characterized by a rhetorical relation between two or more non-overlapping, adjacent text spans.

See: http://angcl.ling.uni-potsdam.de/resources/pcc.html


## DISRPT 2023 Shared Task Information

For the DISRPT 2023 shared tasks, the data is divided into `train`, `dev`, and`test` partitions, 
comprising 142, 17 and 17 documents, respectively. 
There are no discontinuous discourse units in the data. 

For relation classification, some sparse original labels were collapsed into more common categories recommended by the corpus designers, as follows:

  * enablement => background
  * justify => reason
  * motivation => reason
  * otherwise => antithesis
  * unless => antithesis 

The original labels are retained in .rels files under `orig_label`; 
for the shared task, the final `label` column should be predicted.

Syntactic (automatic) dependency parses are made available using Stanza 
with the 2.7 GSD model for German, but xpos tags are taken from the original PCC corpus STTS tags, 
and are therefore not harmonized with the universal upos tags column. 
Due to the original tokenization of the corpus, 
fused tokens such as 'im', 'ins' etc. are retained in the data without CoNLL-U super-tokens, 
and are given the appropriate STTS tags (e.g. APPRART).



## References

[Potsdam Commentary Corpus 2.0: Annotation for Discourse Research](https://aclanthology.org/L14-1468/) (Stede & Neumann, LREC 2014)

Please cite this paper if publishing separately about the data.

```
@inproceedings{stede-neumann-2014-potsdam,
    title = "{P}otsdam Commentary Corpus 2.0: Annotation for Discourse Research",
    author = "Stede, Manfred  and
      Neumann, Arne",
    booktitle = "Proceedings of the Ninth International Conference on Language Resources and Evaluation ({LREC}'14)",
    month = may,
    year = "2014",
    address = "Reykjavik, Iceland",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2014/pdf/579_Paper.pdf",
    pages = "925--929",
    abstract = "We present a revised and extended version of the Potsdam Commentary Corpus, a collection of 175 German newspaper commentaries (op-ed pieces) that has been annotated with syntax trees and three layers of discourse-level information: nominal coreference,connectives and their arguments (similar to the PDTB, Prasad et al. 2008), and trees reflecting discourse structure according to Rhetorical Structure Theory (Mann/Thompson 1988). Connectives have been annotated with the help of a semi-automatic tool, Conano (Stede/Heintze 2004), which identifies most connectives and suggests arguments based on their syntactic category. The other layers have been created manually with dedicated annotation tools. The corpus is made available on the one hand as a set of original XML files produced with the annotation tools, based on identical tokenization. On the other hand, it is distributed together with the open-source linguistic database ANNIS3 (Chiarcos et al. 2008; Zeldes et al. 2009), which provides multi-layer search functionality and layer-specific visualization modules. This allows for comfortable qualitative evaluation of the correlations between annotation layers.",
}
```
# spa.rst.rststb

### The RST Spanish Treebank

Citation: da Cunha, Iria; Torres-Moreno, Juan-Manuel; Sierra, Gerardo (2011). [On the Development of the RST Spanish Treebank](https://aclanthology.org/W11-0401/). In Proceedings of the 5th Linguistic Annotation Workshop. 49th Annual Meeting of the Association for Computational Linguistics (ACL). Portland, Oregon, USA.
```
@inproceedings{da-cunha-etal-2011-development,
    title = "On the Development of the {RST} {S}panish Treebank",
    author = "da Cunha, Iria  and
      Torres-Moreno, Juan-Manuel  and
      Sierra, Gerardo",
    booktitle = "Proceedings of the 5th Linguistic Annotation Workshop",
    month = jun,
    year = "2011",
    address = "Portland, Oregon, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W11-0401",
    pages = "1--10",
}
```


## Introduction

The RST Spanish Treebank is an on-line specialized text corpus for Spanish. It was annotated using the discourse relations from the Rhetorical Structure Theory (RST) by Mann and Thompson (1988).


### Segmentation

  * Each Elementary Discourse Unit (EDU) must include a finite verb, an infinitive or a gerund. Participles are not considered for segmentation.
  * Fragments found between brackets are only considered as EDUs if they contain a verb.
  * Completive clauses should not be segmented, whether they represent the subject, direct object, indirect object or circumstance of a main clause.
  

## DISRPT 2023 Shared Task Information

Automatic parses were added using Stanza's pretrained Spanish Ancora model. The data contains discontinuous discourse units (originally connected via "same-unit" relations). 

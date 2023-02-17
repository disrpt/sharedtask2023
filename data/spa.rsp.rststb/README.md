# spa.rst.rststb

The RST Spanish Treebank

Citation: da Cunha, Iria; Torres-Moreno, Juan-Manuel; Sierra, Gerardo (2011). "On the Development of the RST Spanish Treebank". In Proceedings of the 5th Linguistic Annotation Workshop. 49th Annual Meeting of the Association for Computational Linguistics (ACL). Portland, Oregon, USA.


## Introduction

The RST Spanish Treebank is an on-line specialized text corpus for Spanish. It was annotated using the discourse relations from the Rhetorical Structure Theory (RST) by Mann and Thompson (1988).

### Segmentation

  * Each Elementary Discourse Unit (EDU) must include a finite verb, an infinitive or a gerund. Participles are not considered for segmentation.
  * Fragments found between brackets are only considered as EDUs if they contain a verb.
  * Completive clauses should not be segmented, whether they represent the subject, direct object, indirect object or circumstance of a main clause.
  
## DISRPT 2021 shared task information

Automatic parses were added using Stanza's pretrained Spanish Ancora model. The data contains discontinuous discourse units (originally connected via "same-unit" relations). This dataset contains discontinuous discourse units (split 'same-unit').

# zho.pdtb.cdtb

### Chinese Discourse Treebank 0.5

Zhou, Yuping, et al. [Chinese Discourse Treebank 0.5 LDC2014T21](https://catalog.ldc.upenn.edu/LDC2014T21). Web Download. Philadelphia: Linguistic Data Consortium, 2014.

```
@Misc{CDTB-LDC,
  author       = {Yuping Zhou, Jill Lu, Jennifer Zhang, Nianwen Xue},
  year         = {2014},
  title        = {{Chinese Discourse Treebank 0.5 LDC2014T21}},
  organization = {Linguistic Data Consortium},
  address      = {Philadelphia}
}
```


## Introduction

Chinese Discourse Treebank 0.5, Linguistic Data Consortium (LDC) Catalog Number LDC2014T21 and ISBN 1-58563-692-4, was developed at Brandeis University as part of the Chinese Treebank Project and consists of approximately 73,000 words of Chinese newswire text annotated for discourse relations. It follows the lexically grounded approach of the Penn Discourse Treebank (PDTB) (LDC2008T05) with adaptations based on the linguistic and statistical characteristics of Chinese text. Discourse relations are lexically anchored by discourse connectives (e.g., because, but, therefore), which are viewed as predicates that take abstract objects such as propositions, events and states as their arguments. Along with PDTB-style schemes for English, Turkish, Hindi and Czech, Chinese Discourse Treebank provides an additional perspective on how the PDTB approach can be extended for cross-lingual annotation of discourse relations.

### Data

Data was selected from the newswire material in [Chinese Treebank 8.0 (LDC2013T21)](https://catalog.ldc.upenn.edu/LDC2013T21), specifically, from Xinhua News Agency stories. There are approximately 5,500 annotation instances. 

## DISRPT 2023 Shared Task Information

Syntactic dependency parses are made available using the CoreNLP conversion to UD syntax from the gold Chinese Treebank constituent trees.

### Obtaining the Text

Since the underlying Xinhua news text cannot be placed openly online, the shared task data has replaced token information with underscores. To reconstruct the data, users must obtain a copy of the LDC release of the Chinese Discourse Treebank 0.5 (LDC2014T21) and run the Python script in `utils/process_underscores.py cdtb -m add`. For more details, run `python utils/process_underscores.py -h`. 

### Notes on Segmentation

(The organizers wish to thank Bonnie Webber for this introduction; see also the description of the English PDTB)

Texts in PDTB-style corpora are not split into discourse units. Rather, annotation proceeds from using evidence to recognize a potential discourse relation and then verifying it is one. Evidence includes (1) a word or phrase that COULD be an explicit discourse connective that is verified as functioning as a discourse connective; sentences that are adjacent within a paragraph or clauses that are adjacent within a sentence, absent a discourse connective; or clauses within a sentence found in a particular syntactic configuration that correlates with a discourse relation.

Once a discourse relation is annotated, there will be several segments:
  * one or more segments expressing Arg1 of the relation
  * one or more segments expressing Arg2 of the relation
  * usually one segment corresponding to an explicit connective if one is present in the relation
   (but possibly more, for discontinous connectives)
  * one or more segments that are OUTSIDE the given relation
  * optionally, a segment (either outside the relation, or within one of the arguments)
   indicating the attribution of the relation
  * optionally, in the absense of an explicit connective, segments WITHIN one or
    both arguments that is taken to provide evidence for that relation.

Each relation segments a text independently. Segments may be discontinuous, and within a sentence, which (potentially discontinuous segments) correspond to Arg1 and which to Arg2 depends on whether the syntactic elements representing Arg1 and Arg2 are in a syntactically coordinating or a syntactically subordinating relation.  In the former, Arg1 precedes Arg2. In the latter, Arg2 is associated with the syntactically subordinate constituent, whether it is to the left or right of Arg1.

With respect to PDTB-style corpora, the DISRPT segmentation task only requires identifying segments corresponding to the **explicit connectives** in the text.

  * Labelling a token with "Seg=B-Conn" indicates that it is at the beginning of an explicit connective.
  * Labelling a token with "Seg=I-Conn" indicates that it is a continuation of the start of the connective
   to its left;
  * Labelling a token with "_" indicates that is is outside the segment to its left.

The following illustrate DISRPT labelling of a sentence with several distinct connectives:

```
1	与	_	P	P	_	3	prep	_	Seg=B-Conn
2	此	_	PN	PN	_	1	pobj	_	Seg=I-Conn
3	同时	_	NT	NT	_	12	nsubj	_	Seg=I-Conn
4	，	_	PU	PU	_	12	punct	_	_
5	各	_	DT	DT	_	8	det	_	_
6	项	_	M	M	_	5	clf	_	_
7	配套	_	NN	NN	_	8	nn	_	_
8	改革	_	NN	NN	_	9	nn	_	_
9	步伐	_	NN	NN	_	12	nsubj	_	_
10	也	_	AD	AD	_	12	advmod	_	Seg=B-Conn
11	进一步	_	AD	AD	_	12	advmod	_	_
12	加快	_	VV	VV	_	0	root	_	_
13	。	_	PU	PU	_	12	punct	_	_
```

### Notes on relation Classification 

When there are multiple sense labels available, the sense label that has a lower frequency is chosen as the sense label to predict, and the directionality information thus corresponds to this chosen sense. All sense labels are included in the “orig_label” column, separated by a semicolon. 



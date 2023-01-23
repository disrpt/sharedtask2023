# Sample Data
Sample data for the DISRPT2023 shared task: file are named with language and framework.  

You will find here samples from 6 languages : Basque, Chinese, Dutch, Persian, Protuguese and Russian.



## Formats
### TASK 1: Discourse Unit Segmentation across Formalisms
#### Treebank format `*.conllu`
Files are given in the 10 column, tab delimited CoNLL-U format, with three kinds of lines:

- Token lines (10 columns, word form in column 2) - the last column (CoNLL-U MISC field) may include an annotation **BeginSeg=Yes** to indicate the beginning of a discourse unit - this is the annotation systems should predict. Note: Other annotations from the original treebanks may also be present in this field, in which case they will be pipe separated, e.g. BeginSeg=Yes|SpaceAfter=No.
- Blank lines between sentences
- Comment lines (some optional) - begin with # and contain one of three key-value pairs, e.g.:
    - \# newdoc id = GUM_academic_art [This is the identifier indicating a new corpus document]
    - \# sent_id = GUM_academic_art-1 [If the treebank has native sentence IDs, there are included in this way for reference]
    - \# text = Aesthetic Appreciation and Spanish Art: [Original, untokenized sentence text - not available for all treebanks]  

Example: (from The Georgetown University Multilayer (GUM) corpus)

```
# newdoc id = GUM_fiction_veronique
# sent_id = GUM_fiction_veronique-1
# text = The Cost to Be Wise
1	The	the	DET	DT	Definite=Def|PronType=Art	2	det	_	BeginSeg=Yes
2	Cost	cost	PROPN	NNP	Number=Sing	0	root	_	_
3	to	to	PART	TO	_	5	mark	_	_
4	Be	be	AUX	NNP	Number=Sing	5	cop	_	_
5	Wise	Wise	PROPN	NNP	Number=Sing	2	xcomp	_	_

# sent_id = GUM_fiction_veronique-2
# text = Veronique stayed with me that night, lying next to me in my blankets and furs.
1	Veronique	Veronique	PROPN	NNP	Number=Sing	2	nsubj	_	BeginSeg=Yes
2	stayed	stay	VERB	VBD	Mood=Ind|Tense=Past|VerbForm=Fin	0	root	_	_
3	with	with	ADP	IN	_	4	case	_	_
4	me	me	PRON	PRP	Case=Acc|Number=Sing|Person=1|PronType=Prs	2	obl	_	_
5	that	that	DET	DT	Number=Sing|PronType=Dem	6	det	_	_
6	night	night	NOUN	NN	Number=Sing	2	obl:tmod	_	SpaceAfter=No
7	,	,	PUNCT	,	_	8	punct	_	_
8	lying	lie	VERB	VBG	VerbForm=Ger	2	advcl	_	BeginSeg=Yes
9	next	next	ADJ	JJ	Degree=Pos	8	advmod	_	_
10	to	to	ADP	TO	_	11	case	_	_
11	me	me	PRON	PRP	Case=Acc|Number=Sing|Person=1|PronType=Prs	9	obl	_	_
12	in	in	ADP	IN	_	14	case	_	_
13	my	my	PRON	PRP$	Number=Sing|Person=1|Poss=Yes|PronType=Prs	14	nmod:poss	_	_
14	blankets	blanket	NOUN	NNS	Number=Plur	8	obl	_	_
15	and	and	CCONJ	CC	_	16	cc	_	_
16	furs	fur	NOUN	NNS	Number=Plur	14	conj	_	SpaceAfter=No
17	.	.	PUNCT	.	_	2	punct	_	_

# sent_id = GUM_fiction_veronique-3
# text = She didn't sleep, I don't think.
1	She	she	PRON	PRP	Case=Nom|Gender=Fem|Number=Sing|Person=3|PronType=Prs	4	nsubj	_	BeginSeg=Yes
2	did	do	AUX	VBD	Mood=Ind|Tense=Past|VerbForm=Fin	4	aux	_	SpaceAfter=No
3	n't	n't	PART	RB	Polarity=Neg	4	advmod	_	_
...

```

#### Plain format `*.tok`
This format contains one token per line, with a running ID and word form in the first two tab delimited columns, and the possible annotation BeginSeg=Yes in the tenth and last column (if a new segment boundary is present). Document boundaries are indicated by comments, but other annotations are not used:  

Example: (from The Georgetown University Multilayer (GUM) corpus)
```
# newdoc id = GUM_fiction_veronique
1	The	_	_	_	_	_	_	_	BeginSeg=Yes
2	Cost	_	_	_	_	_	_	_	_
3	to	_	_	_	_	_	_	_	_
4	Be	_	_	_	_	_	_	_	_
5	Wise	_	_	_	_	_	_	_	_
6	Veronique	_	_	_	_	_	_	_	BeginSeg=Yes
7	stayed	_	_	_	_	_	_	_	_
8	with	_	_	_	_	_	_	_	_
9	me	_	_	_	_	_	_	_	_
10	that	_	_	_	_	_	_	_	_
11	night	_	_	_	_	_	_	_	_
12	,	_	_	_	_	_	_	_	_
13	lying	_	_	_	_	_	_	_	BeginSeg=Yes
14	next	_	_	_	_	_	_	_	_
15	to	_	_	_	_	_	_	_	_
16	me	_	_	_	_	_	_	_	_
17	in	_	_	_	_	_	_	_	_
18	my	_	_	_	_	_	_	_	_
19	blankets	_	_	_	_	_	_	_	_
20	and	_	_	_	_	_	_	_	_
21	furs	_	_	_	_	_	_	_	_
22	.	_	_	_	_	_	_	_	_
23	She	_	_	_	_	_	_	_	BeginSeg=Yes
24	did	_	_	_	_	_	_	_	_
25	n't	_	_	_	_	_	_	_	_
...

```

### TASK 2: Discourse Connective Identification across Languages
- Files are given in the same formats as in TASK 1: `*.conllu` and `*.tok`.  

- **Labels**, on the other hand, are differents. **Spans of discourse connectives** are annotated :
    - `Seg=B-Conn`  to indicate the **B**eginning of a span
    - `Seg=I-Conn`  to indicate the continuation of a span : the token is **I**nside a span 

Example: (from wsj_0553: Explicit connectives 'but', 'in the end", 'especially if', 'as')
```
1	But	_	_	_	_	_	_	_	Seg=B-Conn
2	in	_	_	_	_	_	_	_	Seg=B-Conn
3	the	_	_	_	_	_	_	_	Seg=I-Conn
4	end	_	_	_	_	_	_	_	Seg=I-Conn
5	his	_	_	_	_	_	_	_	_
6	resignation	_	_	_	_	_	_	_	_
7	as	_	_	_	_	_	_	_	_
8	Chancellor	_	_	_	_	_	_	_	_
9	of	_	_	_	_	_	_	_	_
10	the	_	_	_	_	_	_	_	_
11	Exchequer	_	_	_	_	_	_	_	_
12	may	_	_	_	_	_	_	_	_
13	be	_	_	_	_	_	_	_	_
14	a	_	_	_	_	_	_	_	_
15	good	_	_	_	_	_	_	_	_
16	thing	_	_	_	_	_	_	_	_
17	,	_	_	_	_	_	_	_	_
18	especially	_	_	_	_	_	_	_	Seg=B-Conn
19	if	_	_	_	_	_	_	_	Seg=I-Conn
20	it	_	_	_	_	_	_	_	_
21	works	_	_	_	_	_	_	_	_
22	as	_	_	_	_	_	_	_	Seg=B-Conn
23	he	_	_	_	_	_	_	_	_
24	no	_	_	_	_	_	_	_	_
25	doubt	_	_	_	_	_	_	_	_
26	intends	_	_	_	_	_	_	_	_
...
```

### TASK 3: Discourse Relation Classification across Formalisms
File `*.rels` are given in a 12 columns format, separated by tabulation, as described below : 

- doc	&rarr;  Name of the doument
- unit1_toks	&rarr;  Range of unit 1 tokens ID
- unit2_toks	&rarr;  Range of unit 2 tokens ID
- unit1_txt	    &rarr;  Text of unit 1
- unit2_txt	&rarr;  Text of unit 2
- s1_toks	&rarr;  Range of tokens ID of the sentence that contains unit 1
- s2_toks	&rarr;  Range of tokens ID of the sentence that contains unit 2
- unit1_sent	&rarr;  Text of the sentence that contains unit 1
- unit2_sent	&rarr;  Text of the sentence that contains unit 2
- dir	&rarr;  Direction of the relation `>` or `<`
- orig_label	&rarr;  Original label
- label&rarr;  Label to predict, maximum 2 level of sub-label

## Syntactic parsing
Some languages allow multi-words contraction :  
    - English: `that's` &rarr; `that` + `is`  
    - German: `im` &rarr; `in` + `dem`  
    ...  
    - French, Persian, Portuguese, Spanish, Turkish...

When it is available, text tokenization reflects those cases by providing the contracted form (with a range of IDs as ID) followed by both of parts of the "extended" form.

Example: (from the Brazilian Portuguese Cross-document Structure Theory News Corpus)
```
# newdoc id = D1_C13_Folha_07-08-2010_07h21
# sent_id = D1_C13_Folha_07-08-2010_07h21-1
# text = Quinze voluntários da ONG francesa Ação Contra a Fome ( ACF ) foram assassinados no nordeste do Sri Lanka , informou hoje um porta-voz da organização .
1	Quinze	quinze	NUM	NUM	NumType=Card	2	nummod	_	BeginSeg=Yes
2	voluntários	voluntário	NOUN	NOUN	Gender=Masc|Number=Plur	15	nsubj:pass	_	_
3-4	da	_	_	_	_	_	_	_	_
3	de	de	ADP	ADP	_	5	case	_	_
4	a	o	DET	DET	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	5	det	_	_
5	ONG	ONG	PROPN	PROPN	Gender=Fem|Number=Sing	2	nmod	_	_
6	francesa	francês	ADJ	ADJ	Gender=Fem|Number=Sing	5	amod	_	_
7	Ação	Ação	PROPN	PROPN	Gender=Fem|Number=Sing	5	appos	_	_
8	Contra	Contra	PROPN	PROPN	Number=Sing	7	flat:name	_	_
9	a	o	DET	DET	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	flat:name	_	_
10	Fome	Fome	PROPN	PROPN	Number=Sing	7	flat:name	_	_
11	(	(	PUNCT	PUNCT	_	12	punct	_	BeginSeg=Yes
12	ACF	ACF	PROPN	PROPN	Gender=Fem|Number=Sing	5	appos	_	_
13	)	)	PUNCT	PUNCT	_	12	punct	_	_
14	foram	ser	AUX	AUX	Mood=Ind|Number=Plur|Person=3|VerbForm=Fin	15	aux:pass	_	BeginSeg=Yes
15	assassinados	assassinar	VERB	VERB	Gender=Masc|Number=Plur|VerbForm=Part|Voice=Pass	24	ccomp	_	_
16-17	no	_	_	_	_	_	_	_	_
16	em	em	ADP	ADP	_	18	case	_	_
17	o	o	DET	DET	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	18	det	_	_
18	nordeste	nordeste	NOUN	NOUN	Gender=Masc|Number=Sing	15	obl	_	_
19-20	do	_	_	_	_	_	_	_	_
19	de	de	ADP	ADP	_	21	case	_	_
20	o	o	DET	DET	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	21	det	_	_
21	Sri	Sri	PROPN	PROPN	Gender=Masc|Number=Sing	18	nmod	_	_
22	Lanka	Lanka	PROPN	PROPN	Number=Sing	21	flat:name	_	_
23	,	,	PUNCT	PUNCT	_	15	punct	_	_
24	informou	informar	VERB	VERB	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	_	BeginSeg=Yes
25	hoje	hoje	ADV	ADV	_	24	advmod	_	_
26	um	um	DET	DET	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	27	det	_	_
27	porta-voz	porta-voz	NOUN	NOUN	Gender=Masc|Number=Sing	24	nsubj	_	_
28-29	da	_	_	_	_	_	_	_	_
28	de	de	ADP	ADP	_	30	case	_	_
29	a	o	DET	DET	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	30	det	_	_
30	organização	organização	NOUN	NOUN	Gender=Fem|Number=Sing	27	nmod	_	_
31	.	.	PUNCT	PUNCT	_	24	punct	_	_

```

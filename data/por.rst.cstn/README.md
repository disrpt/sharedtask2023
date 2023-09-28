# por.rst.cstn

### Cross-document Structure Theory News Corpus

Cardoso, P.C.F.; Maziero, E.G.; Jorge, M.L.C.; Seno, E.M.R.; Di Felippo, A.; Rino, L.H.M.; Nunes, M.G.V.; Pardo, T.A.S. (2011).
[CSTNews - A Discourse-Annotated Corpus for Single and Multi-Document Summarization of News Texts in Brazilian Portuguese](https://www.semanticscholar.org/paper/CSTNews-A-Discourse-Annotated-Corpus-for-Single-and-Cardoso-Maziero/d84cfba46785136129a276e906119ecd190085fd). In the Proceedings of the 3rd RST Brazilian Meeting, pp. 88-105. October 26, Cuiabá/MT, Brazil.
```
@InProceedings{CardosoMazieroRosarioCastroJorgeEtAl2011,
author    = {Paula Christina Figueira Cardoso and Erick Galani Maziero and Maria Luc\'{i}a del Rosario Castro Jorge and M. Eloize and R. Kibar Aji Seno and Ariani Di Felippo and Lucia Helena Machado Rino and Maria das Gra\c{c}as Volpe Nunes and Thiago Alexandre Salgueiro Pardo},
title     = {{CSTNews} - A Discourse-Annotated Corpus for Single and Multi-Document Summarization of News Texts in {B}razilian {P}ortuguese},
booktitle = {Proceedings of the 3rd RST Brazilian Meeting},
year      = {2011},
pages     = {88--105},
address   = {Cuiab\'{a}, Brazil}
}
```


## Introduction

The CSTNews corpus was annotated by groups of computational linguists from NILC (http://nilc.icmc.usp.br). The corpus is avaiable for download and use for research purposes (http://conteudo.icmc.usp.br/pessoas/taspardo/sucinto/cstnews.html).

The sucinto project (http://conteudo.icmc.usp.br/pessoas/taspardo/sucinto/) aimed at investigating and exploring generic and topic-focused multi-document summarization strategies for providing a more feasible and intelligent access to on-line information provided by news agencies. This commitment brought back old and well-known scientific challenges from the first studies in summarization in the 50s as well as introduced several new and exciting challenges, e.g., to deal with redundant, complementary and contradictory information, to normalize different writing styles and referring expression choices, to balance different perspectives and sides of the same events and facts, to properly deal with evolving events and their narration in different moments, and to arrange information pieces from different texts to produce coherent and cohesive summaries, among several others. An ultimate goal of this project was to pull the developed tools together as on-line applications for final users.

This project took into consideration not only classical approaches to single and multi-document summarization, but also new ones, following different paradigms and using knowledge of varied nature ranging from empirical and statistical data to semantic and discourse models. Research interests included (i) the modeling of the summarization process (content selection, planning, aggregation, generalization, substitution, information ordering, etc.) by means of Cross-document Structure Theory (CST), Rhetorical Structure Theory (RST), ontologies, and language and summarization statistical models, (ii) the investigation of related tasks as discourse parsing, topic detection, temporal annotation and resolution, coreference resolution, text-summary alignment, and multilingual processing, and (iii) the linguistic characterization of multi-document summaries and their manual production.

The project was developed at NILC (Interinstitutional Center for Computational Linguistics), one of the biggest research groups on Natural Language Processing and Computational Linguistics in Brazil. It started in 2007 as a natural follow up to some previous projects on single-document summarization carried out at NILC (FAPESP #2006/02887-9; see also related projects). It was supported by the research agencies FAPESP, CNPq, and CAPES, which have granted scholarships for undergraduate and graduate students and regular financial support for the project (FAPESP# 2015/17841-3, FAPESP #2012/03071-3, FAPESP #2009/05603-0). The project was officially over at the end of 2017.


## DISRPT 2023 Shared Task Information

The corpus is composed of 140 news texts clustered in 50 groups, totaling 2221 sentences. The number of texts per cluster varies from 2 to 3. Each cluster groups texts from different news sources about the same event. To avoid biases, texts from the same cluster were put together in the same split (dev, test or train). As a result, the test set is somewhat smaller than the dev set, but this was not altered in order to respect the existing splits of the corpus from other tasks and papers.

Data was automatically parsed using the Stanza Portuguese model (based on UD Portuguese-Bosque 2.7). Note that the data includes .conllu multi-word tokens, for example fused articles and prepositions are decomposed automatically:

```
# newdoc_id = D4_C36_JB
# sent_id = D4_C36_JB-1
# text = Presença constante na cena política brasileira nas últimas quatro décadas , o senador Antonio Carlos Magalhães ( DEM-BA ) morreu na manhã desta sexta-feira , em São Paulo , vítima de insuficiência cardíaca .
1	Presença	presença	NOUN	NOUN	Gender=Fem|Number=Sing	22	obl	_	BeginSeg=Yes
2	constante	constante	ADJ	ADJ	Gender=Fem|Number=Sing	1	amod	_	_
3-4	na	_	_	_	_	_	_	_	_
3	em	em	ADP	ADP	_	5	case	_	_
4	a	o	DET	DET	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	5	det	_	_
5	cena	cena	NOUN	NOUN	Gender=Fem|Number=Sing	1	nmod	_	_
6	política	político	ADJ	ADJ	Gender=Fem|Number=Sing	5	amod	_	_
7	brasileira	brasileiro	ADJ	ADJ	Gender=Fem|Number=Sing	5	amod	_	_
8-9	nas	_	_	_	_	_	_	_	_
8	em	em	ADP	ADP	_	12	case	_	_
9	as	o	DET	DET	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	12	det	_	_
10	últimas	último	ADJ	ADJ	Gender=Fem|NumType=Ord|Number=Plur	12	amod	_	_
11	quatro	quatro	NUM	NUM	NumType=Card	12	nummod	_	_
12	décadas	década	NOUN	NOUN	Gender=Fem|Number=Plur	1	nmod	_	_
...
```

### Notes
This dataset contains discontinuous discourse units (split 'same-unit').

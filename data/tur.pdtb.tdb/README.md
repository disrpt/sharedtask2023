# tur.pdtb.tdb

Turkish Discourse Bank 1.0 & Turkish Discourse Bank 1.1 

## Introduction  

Turkish Discourse Bank 1.0 is a 400,000-word corpus funded by TÜBİTAK (The Scientific and Technological Research Council of Turkey) annotated in the PDTB style. For more information regarding TDB, please visit: http://medid.ii.metu.edu.tr/theCorpus.html. TDB 1.0 contains explicit discourse connectives as well phrasal expressions based on postpositions, i.e: 

-conjunctions such as 've' (and), 'ama' (but), etc. 
-adverbials such as 'aksine' (to the contrary),
-postpositions such as için 'for' (conveying the purpose or reason sense), 
-phrasal expressions such as 'bunun için' (for this reason).

Postpositions are single word connectives and they always appear after the verb of the syntactically dependent argument. The phrasal expressions annotated in TDB 1.0 are derived from postpositions and mostly contain a deictic element such as 'bu' (this), 'o' (that). Phrasal expressions are a sub-type of alternative lexicalizations.   

As in the PDTB, in TDB,

-explicit connectives may be continuous or discontinuous, as in 've' (and), 'hem ... hem' (both ... and), 
-explicit connectives may be pre-modified as in 'tam aksine' (just to the contrary); they may also be post-modified as in 'sanki ... gibi' (as if)
-phrasal expressions may be pre-modified, as in 'ancak bundan sonra' (only after this), or they may be post-modified by a focus particle, as in 'bu amaçla da' (for this reason - focus particle). 

Turkish Discourse Bank 1.1 (TDB 1.1) is an extension on the Turkish Discourse Bank 1.0. TDB 1.1 added sense annotations to a subset of the Turkish Discourse Bank 1.0 (10% of the corpus, 20 documents), which consists of the content of the relation classification task for Turkish. Please refer to the paper titled "TDB 1.1: Extensions on Turkish Discourse Bank" (https://www.aclweb.org/anthology/W17-0809/) for more details. 

## DISRPT 2023 shared task information

The data was automatically parsed using the UDPipe Turkish model (https://github.com/jwijffels/udpipe.models.ud.2.0/blob/master/inst/udpipe-ud-2.0-170801/turkish-ud-2.0-170801.udpipe). 

### Obtaining the text

Since the underlying texts cannot be placed openly online, the shared task data has replaced token information with underscores. To reconstruct the data, users must obtain the raw texts by filling in the user agreement form (`tdb_shared_task_user_agreement.docx`) which they email to `corpora@metu.edu.tr` and run the Python script in `utils/process_underscores.py tdb -m add`. For more details, run `python utils/process_underscores.py -h`.


### Notes on relation classification

1. Only a subset of the TDB 1.0 is used for the relation classification. Not all documents used in the segmentation and connective detection tasks will be found in the .rels files. 
2. In addition to the inventory of the sense labels used in PDTB3 for English, there are three Level-2 sense labels developed for TDB1.1: Comparison.Degree, Expansion.Manner, and Expansion.Correction. For more details, please refer to the paper (https://www.aclweb.org/anthology/W17-0809/). 
3. The predicted label (the last column) for each instance has been truncated at Level-2. For instance, the predicted label for the sense label “Temporal.Asynchronous.Precedence” would be “Temporal.Asynchronous”. However, we keep the original label in the third-to-last column called “orig_label”, which matches the directionality information provided in the “dir” column. Moreover, when there are multiple sense labels available, the sense label that has a lower frequency (the frequency is based on Level-2 relations) is chosen as the sense label to predict, and the directionality information thus corresponds to this chosen sense. Both sense labels are included in the “orig_label”, separated by a semicolon.

This dataset contains discontinuous discourse units.

## Notes

A list of all explicit connectives and phrasal expressions annotated in TDB 1.0 can be found in Demirşahin and Zeyrek (2017). 

An introduction to TDB can be found in Zeyrek and Webber (2008)

The full tag set of TDB can be found in Zeyrek et al. (2013)

The list of all modifiers can be found in Çakmak (2015). 


References: 

Zeyrek, D., & Kurfalı, M. (2017, April). TDB 1.1: Extensions on Turkish discourse bank. In Proceedings of the 11th Linguistic Annotation Workshop (pp. 76-81).

Zeyrek, D., & Kurfalı, M. (2018, May). An assessment of explicit inter-and intra-sentential discourse connectives in Turkish Discourse Bank. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).

Çakmak, Deniz Hande. (2015). The Role of Modifiers in Turkish Discourse Bank. Unpublished MS Thesis. Middle East Technical University, Cognitive Science Department. 

Demirşahin, I., & Zeyrek, D. (2017). Pair annotation as a novel annotation procedure: The case of Turkish Discourse Bank. In Handbook of Linguistic Annotation (pp. 1219-1240). Springer, Dordrecht.

Zeyrek, D., Demirşahin, I., Sevdik-Çallı, A. B., & Çakıcı, R. (2013). Turkish Discourse Bank: Porting a discourse annotation style to a morphologically rich language. D&D, 4(2), 174-184.

Zeyrek, D., & Webber, B. (2008). A discourse resource for Turkish: Annotating discourse connectives in the METU corpus. In Proceedings of the 6th workshop on Asian language resources.

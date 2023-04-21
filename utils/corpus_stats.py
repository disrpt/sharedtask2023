import locale
import io, sys, re, os
from glob import glob
from collections import defaultdict, OrderedDict

#data_dir = ".." + os.sep + "data"
#print(data_dir)
#data_dir = '/home/cbraud/projects/disrpt/sharedtask2023/data'
#data_dir = '/home/cbraud/projects/disrpt/disrpt23_laura/data_clean'
#data_dir = '/home/lriviere/disrpt_lau/disrpt23_dev/data_clean'
data_dir = '../data'
corpora = [o for o in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir,o))]
#corpora = [o for o in corpora if "gum" in o]
stats = defaultdict(OrderedDict)
gold_syn = ["eng.rst.gum","eng.rst.rstdt","eng.pdtb.pdtb","zho.pdtb.cdtb"]
#test = False
test = True

for corpus in corpora:
	print( "Processing CORPUS", corpus)
	d = stats[corpus]
	d["corpus"] = corpus
	d["lang"], d["framework"] = corpus.split(".")[:-1]
	#files = glob(".." + os.sep + "data" + os.sep + corpus + os.sep + "*.rels")
	files = glob(data_dir + os.sep + corpus + os.sep + "*.rels")
	print(files)
	rels_types = set()
	for file_ in files:
		print(f"step-1 >>> {file_}")
		text = io.open(file_, encoding="utf8").read()
		#rels_types = set()
		if "train" in file_:
			print("train")
			rel_rows = [l.split("\t")[-1] for i,l in enumerate(text.split("\n")) if "\t" in l and i>0]
			rels = set(rel_rows)
			rels_types.update(rels)
			#d["rels"] = len(rel_rows)
			if "rels" in d:
				d["rels"] += len(rel_rows)
			else:
				d["rels"] = len(rel_rows)
			#d["rel_types"] = len(rels)
			print(f"train  {rels, len(rels)}" )
			d["discont"] = "yes" if "<*>" in text else "no"
		elif "test" in file_:
			print("test")
			rel_rows = [l.split("\t")[-1] for i,l in enumerate(text.split("\n")) if "\t" in l and i>0]
			rels = set(rel_rows)
			rels_types.update(rels)
			#print(len)
			if "rels" in d:
				d["rels"] += len(rel_rows)
			else:
				d["rels"] = len(rel_rows)
			print(f"test {rels, len(rels)}" )
		elif "dev" in file_: 
			print("dev")
			rel_rows = [l.split("\t")[-1] for i,l in enumerate(text.split("\n")) if "\t" in l and i>0]
			rels = set(rel_rows)
			rels_types.update(rels)
			if "rels" in d:
				d["rels"] += len(rel_rows)
			else:
				d["rels"] = len(rel_rows)
			print(f"dev {rels, len(rels)}" )
		
	print(f"nb de rels types= {len(rels_types)}")


	#files = glob(".." + os.sep + "data" + os.sep + corpus + os.sep + "*.conllu")
	files = glob(data_dir + os.sep + corpus + os.sep + "*.conllu")
	# sort files
	train_f = [f for f in files if "train." in f]
	test_f = [f for f in files if "test." in f]
	dev_f = [f for f in files if "dev." in f]
	files = train_f + dev_f + test_f

	all_toks = 0
	all_sents = 0
	all_docs = 0
	all_segs = 0
	train_exist = False # for corp with no train
	for file_ in files:
		print(file_)
		text = io.open(file_,encoding="utf8").read()
		docs = text.count("# newdoc")
		if docs == 0:
			sys.stderr.write("No documents found in " + file_)
			sys.exit(0)
		sents = text.count("\n1\t")
		segs = text.count("BeginSeg") + text.count("B-Conn")
		just_toks = text.strip()
		just_toks = re.sub(r"\n+",r'\n',just_toks) # Remove blank lines
		just_toks = re.sub(r"^[0-9]+-[^\n]+\n",r'\n',just_toks,flags=re.MULTILINE)  # Remove multi-toks if present
		just_toks = re.sub(r"^#[^\n]+\n",r'',just_toks,flags=re.MULTILINE)  # Remove comment lines
		toks = just_toks.count("\n") + 1
		if "_train" in file_:
			part = "train"
			train_exist = True
		elif "_test" in file_:
			part = "test"
			#print('ok test')
		elif "_dev" in file_:
			part = "dev"
		print( part )
		d[part+"_toks"] = toks
		d[part+"_sents"] = sents
		d[part+"_docs"] = docs
		d[part+"_segs"] = segs
		all_toks += toks
		all_sents += sents
		all_docs += docs
		all_segs += segs
	if train_exist == False:
		d["train_toks"] = 0
		d["train_sents"] = 0
		d["train_docs"] = 0
		d["train_segs"] = 0

	
	""" d["dev_tok%"] = 100*d["dev_toks"]/float(all_toks)
	if test:
		d["test_tok%"] = 100*d["test_toks"]/float(all_toks)
	d["train_tok%"] = 100*d["train_toks"]/float(all_toks)
	d["dev_doc%"] = 100*d["dev_docs"]/float(all_docs)
	if test:
		d["test_doc%"] = 100*d["test_docs"]/float(all_docs)
	d["train_doc%"] = 100*d["train_docs"]/float(all_docs) """




	d["total_sents"] = all_sents
	d["total_toks"] = all_toks
	d["total_docs"] = all_docs
	d["total_segs"] = all_segs
	d["seg_style"] = "Conn" if "pdtb" in corpus else "EDU"
	d["underscored"] = "yes" if "pdtb" in corpus or "rstdt" in corpus or ".tdb" in corpus else "no"
	if corpus == "GUM":
		d["underscored"] = "part"
	#if "SpaceAfter" in text:
	#	d["SpaceAfter"] = "yes"
	#else:
	#	d["SpaceAfter"] = "no"
	if text.count("\tcase\t") > 50:
		if text.count("\tdobj\t") > 1:
			d["syntax"] = "UD (V1)"
		else:
			d["syntax"] = "UD"
	else:
		d["syntax"] = "other"
	if corpus in gold_syn:
		d["syntax"] += " (gold)"
	if re.search(r'^[0-9]+-',text,flags=re.MULTILINE) is not None:
		d["MWTs"] = "yes"
	else:
		d["MWTs"] = "no"
	if re.search(r'^[0-9]+\.',text,flags=re.MULTILINE) is not None:
		d["ellip"] = "yes"
	else:
		d["ellip"] = "no"

first = True
for corpus in sorted(stats.keys()):
	d = stats[corpus]
	if first:
		print("| " + " | ".join([k for k in d.keys() if "%" not in k]) + " |")
		print("| " + " | ".join(["---" for k in d.keys() if "%" not in k]) + " |")
	first = False
	vals = []
	for key in d.keys():
		#print(f"{key} :: {d[key]}")
		if "%" not in key:
			if isinstance(d[key],str):
				vals.append(str(d[key]))
			else:
				#vals.append(locale.format("%d", key, grouping=True))
				vals.append(f'{d[key]:,}')
	print("| "+" | ".join(vals) + " |")

"""
process_underscores.py

Script to handle licensed data for which underlying text cannot be posted online (e.g. LDC data).
Users need a copy of the LDC distribution of an underlying resource to restore text in some of the corpora.


"""

__author__ = "Amir Zeldes"
__license__ = "Apache 2.0"
__version__ = "2.0.0"

import io, re, os, sys
from glob import glob
from collections import defaultdict
from argparse import ArgumentParser

PY3 = sys.version_info[0] == 3
if not PY3:
	input = raw_input


gum_docs = {
	"GUM_reddit_macroeconomics": [
		{"year": "2017", "month": "09", "id": "6zm74h", "type": "post","source":"undef"},
		{"year": "2017", "month": "09", "id": "dmwwqlt", "type":"comment","source":"undef"}
	],
	"GUM_reddit_stroke": [
		{"year": "2017", "month": "08", "id": "6ws3eh", "type": "post","source":"undef"},
		{"year": "2017", "month": "08", "id": "dmaei1x", "type":"comment","source":"undef"},
		{"year": "2017", "month": "08", "id": "dmaiwsm", "type":"comment","source":"undef"},
		{"year": "2017", "month": "09", "id": "dmkx8bk", "type":"comment","source":"undef"},
		{"year": "2017", "month": "09", "id": "dmm1327", "type":"comment","source":"undef"},
		{"year": "2017", "month": "08", "id": "dmaoodn", "type":"comment","source":"undef"}
	],
	"GUM_reddit_polygraph": [
		{"year": "2014", "month": "12", "id": "2q6qnv", "type": "post","source":"undef"}
	],
	"GUM_reddit_ring": [
		{"year": "2016", "month": "09", "id": "5570x1", "type": "post","source":"undef"},
		{"year": "2016", "month": "09", "id": "d885ma0", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d8880w7", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88u7dg", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88unu3", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88v0sz", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88xaqu", "type":"comment","source":"undef"},
		{"year": "2016", "month": "10", "id": "d893mj9", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88s4bb", "type":"comment","source":"undef"},
		{"year": "2016", "month": "10", "id": "d88zt6x", "type":"comment","source":"undef"}
	],
	"GUM_reddit_space": [
		{"year": "2016", "month": "08", "id": "50hx5c", "type": "post","source":"undef"},
		{"year": "2016", "month": "08", "id": "d7471k5", "type":"comment","source":"undef"},
		{"year": "2016", "month": "08", "id": "d74i5ka", "type":"comment","source":"undef"},
		{"year": "2016", "month": "08", "id": "d74ppi0", "type":"comment","source":"undef"}
	],
	"GUM_reddit_superman": [
		#{"year": "2017", "month": "04", "id": "68e0u3", "type": "post", "title_only": True},  # Post title not included in this document
		{"year": "2017", "month": "05", "id": "dgys1z8", "type":"comment","source":"undef"}
	],
	"GUM_reddit_bobby": [
		{"year":"2018","month":"06","id":"8ph56q","type": "post","source":"undef"},
		{"year":"2018","month":"06","id":"e0b8zz4","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0dwqlg","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e15pcqu","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0dz1mp","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e1uuo9e","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0brc9w","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0bz951","type":"comment","source":"undef"}
	],
	"GUM_reddit_escape": [
		{"year":"2017","month":"05","id":"69r98j","type": "post","source":"undef"},
		{"year":"2017","month":"05","id":"dh96n8v","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9enpe","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dht8oyn","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dhn0hoe","type":"comment","source":"undef"},
		{"year":"2017","month":"07","id":"dk9ted1","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh98kcg","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9zxej","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"di9x7j9","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"di9xsrt","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"din85zf","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dinab0w","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dinaggd","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dinbyb9","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dj65sp1","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dizdd8a","type":"comment","source":"undef"},
		{"year":"2017","month":"07","id":"dk78qw8","type":"comment","source":"undef"},
		{"year":"2017","month":"08","id":"dm0gqc7","type":"comment","source":"undef"},
		{"year":"2017","month":"10","id":"domd1r0","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9irie","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9iw36","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"djlcwu5","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dlzcxpy","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dhabstb","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dhbr3m6","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"diz97qy","type":"comment"}
	],
	"GUM_reddit_gender": [
		{"year":"2018","month":"09","id":"9e5urs","type":"post","source":"bigquery"},
		{"year":"2018","month":"09","id":"e5mg3s7","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5mkpok","type":"comment","source":"bigquery"},
		{"year":"2018","month":"09","id":"e5nxbmb","type":"comment","source":"bigquery"},
		{"year":"2018","month":"09","id":"e5nzg9j","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5mh94v","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5mmenp","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5ms5u3","type":"comment","source":"undef"}
	],
	"GUM_reddit_monsters":[
		{"year":"2018","month":"09","id":"9eci2u","type":"post","source":"undef"},
		{"year":"2018","month":"09","id":"e5ox2jr","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5p3gtl","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5pnfro","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5q08o4","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5pney1","type":"comment","source":"undef"},
	],
	"GUM_reddit_pandas":[
		{"year":"2018","month":"09","id":"9e3s9h","type":"post","source":"undef"},
		{"year":"2018","month":"09","id":"e5lwy6n","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m397o","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3xgb","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3z2e","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lwbbt","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m38sr","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m42cu","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lvlxm","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lvqay","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lw5t6","type":"comment","source":"undef"},  # Blowhole
		{"year":"2018","month":"09","id":"e5lwz31","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lxi0s","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lwxqq","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lzv1b","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m48ag","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m1yqe","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lx0sw","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m2n80","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m2wrh","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3blb","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lvxoc","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m1abg","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m1w5i","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3pdi","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3ruf","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m4yu2","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m5bcb","type":"comment","source":"undef"}
	],
	"GUM_reddit_steak": [
		{"year":"2015","month":"08","id":"3im341","type":"post","source":"undef"}
	],
	"GUM_reddit_card": [
		{"year":"2019","month":"08","id":"cmqrwo","type":"post","source":"undef"},
		{"year":"2019","month":"08","id":"ew3zrqg","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew43d2c","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew43oks","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew43ymc","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew46h1p","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew46oly","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew46wq7","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew470zc","type":"comment","source":"undef"}
	],
	"GUM_reddit_callout": [
		{"year":"2019","month":"09","id":"d1eg3u","type":"post","source":"undef"},
		{"year":"2019","month":"09","id":"ezkucpg","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezkv0cc","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezkwbx9","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezlh2o6","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezlkajf","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezlnco2","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezo20yy","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezkwcvh","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezl07dm","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezmajm7","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezl1wz3","type":"comment","source":"undef"},
	],
	"GUM_reddit_conspiracy": [
		{"year":"2019","month":"02","id":"aumhwo","type":"post","source":"undef"},
		{"year":"2019","month":"02","id":"eh9rt0n","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eh9tvyw","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"ehc0l2q","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"ehclwtv","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eh9jo5x","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"ehr2665","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eha3c1q","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eha5jlq","type":"comment","source":"undef"},
	],
	"GUM_reddit_introverts": [
		{"year":"2019","month":"06","id":"by820m","type":"post","source":"undef","title_double": True},  # Possible title was repeated by annotator
		{"year":"2019","month":"06","id":"eqeik8m","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqfgaeu","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqfplpg","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqg6a5u","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqh6j29","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqhjtwr","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqi2jl3","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqii2kf","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqhlj8j","type":"comment","source":"undef"},

	],
	"GUM_reddit_racial": [
		{"year":"2019","month":"09","id":"d1urjk","type":"post","source":"undef"},
		{"year":"2019","month":"09","id":"ezq9y6w","type":"comment","source":"bigquery"},
		{"year":"2019","month":"09","id":"ezqpqmm","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezq8xs7","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezr55wk","type":"comment","source":"undef"},
	],
	"GUM_reddit_social": [
		{"year":"2019","month":"09","id":"d1qy3g","type":"post","source":"undef"},
		{"year":"2019","month":"09","id":"ezpb3jg","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpdmy3","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpjor8","type":"comment","source":"bigquery"},
		{"year":"2019","month":"09","id":"ezpiozm","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpc1ps","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezp9fbh","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezqrumb","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpe0e6","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpf71f","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezt7qlf","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpc4jj","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpa2e4","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpfzql","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpi39v","type":"comment","source":"undef"},
	]
}

def underscore_files(filenames):
	def underscore_rel_field(text):
		blanked = []
		text = text.replace("<*>","❤")
		for c in text:
			if c!="❤" and c!=" ":
				blanked.append("_")
			else:
				blanked.append(c)
		return "".join(blanked).replace("❤","<*>")

	for f_path in filenames:
		skiplen = 0
		with io.open(f_path, 'r', encoding='utf8') as fin:
			lines = fin.readlines()

		with io.open(f_path, 'w', encoding='utf8', newline="\n") as fout:
			output = []
			if f_path.endswith(".rels"):
				for l, line in enumerate(lines):
					line = line.strip()
					if "\t" in line and l > 0:
						doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, orig_label, label = line.split("\t")
						if "GUM" in doc and "reddit" not in doc:
							output.append(line)
							continue
						unit1_txt = underscore_rel_field(unit1_txt)
						unit2_txt = underscore_rel_field(unit2_txt)
						unit1_sent = underscore_rel_field(unit1_sent)
						unit2_sent = underscore_rel_field(unit2_sent)
						fields = doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, orig_label, label
						line = "\t".join(fields)
					output.append(line)
			else:
				doc = ""
				for line in lines:
					line = line.strip()
					if line.startswith("# newdoc_id"):
						doc = line.split("=",maxsplit=1)[1].strip()
					if "GUM" in doc and "reddit" not in doc:
						output.append(line)
						continue
					if line.startswith("# text"):
						m = re.match(r'(# text ?= ?)(.+)',line)
						if m is not None:
							line = m.group(1) + re.sub(r'[^\s]','_',m.group(2))
							output.append(line)
					elif "\t" in line:
						fields = line.split("\t")
						tok_col, lemma_col = fields[1:3]
						if lemma_col == tok_col:  # Delete lemma if identical to token
							fields[2] = '_'
						elif tok_col.lower() == lemma_col:
							fields[2] = "*LOWER*"
						if skiplen < 1:
							fields[1] = len(tok_col)*'_'
						else:
							skiplen -=1
						output.append("\t".join(fields))
						if "-" in fields[0]:  # Multitoken
							start, end = fields[0].split("-")
							start = int(start)
							end = int(end)
							skiplen = end - start + 1
					else:
						output.append(line)
			fout.write('\n'.join(output) + "\n")


def get_no_space_strings(cache_dict):
	import ast

	no_space_docs = defaultdict(str)

	for doc in gum_docs:
		for post in gum_docs[doc]:
			if post["id"] in cache_dict:
				json_result = cache_dict[post["id"]]
			parsed = ast.literal_eval(json_result)[0]
			if post["type"]=="post":
				plain = parsed["selftext"]
				title = parsed["title"]
				if "title_only" in post:
					if post["title_only"]:
						plain = ""
				if "title_double" in post:
					title = title + " " + title
			else:
				plain = parsed["body"]
				title = ""
			if "_space" in doc:
				plain = plain.replace("&gt;","")  # GUM_reddit_space has formatting &gt; to indicate indented block quotes
			elif "_gender" in doc:
				plain = plain.replace("- The vast","The vast")
				plain = plain.replace("- Society already accommodates","Society already accommodates")
				plain = plain.replace("- Society recognizes disabilities","Society recognizes disabilities")
				plain = plain.replace("- It’s a waste of time","It’s a waste of time")
				plain = plain.replace("PB&amp;J","PB&J")
			elif "_monsters" in doc:
				plain = plain.replace("1. He refers to","a. He refers to")
				plain = plain.replace("2. Using these","b. Using these")
				plain = plain.replace("3. And he has","c. And he has")
				plain = plain.replace("&#x200B; &#x200B;","")
				plain = re.sub(r' [0-9]+\. ',' ',plain)
			elif "_ring" in doc:
				plain = plain.replace("&gt;",">")
			elif "_escape" in doc:
				plain = plain.replace("*1 year later*","1 year later")
			elif "_racial" in doc:
				plain = plain.replace("> ","")
			elif "_callout" in doc:
				plain = plain.replace("_it","it").replace("well?_","well?").replace(">certain","certain")
			elif "_conspiracy" in doc:
				plain = plain.replace(">", "")
			elif "_stroke" in doc:
				plain = plain.replace("&amp;", "&")
			elif "_bobby" in doc:
				plain = plain.replace("&amp;", "&")
			elif "_introvert" in doc:
				plain = plain.replace("enjoy working out.","enjoy working out").replace("~~","")
			elif "_social" in doc:
				plain = plain.replace("the purpose","those purpose").replace("&#x200B;","")
			no_space = re.sub(r"\s","",plain).replace("*","")
			no_space = re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',no_space)  # Remove Wiki style links: [text](URL)
			if no_space_docs[doc] == "":
				no_space_docs[doc] += re.sub(r"\s","",title).replace("*","")
			no_space_docs[doc] += no_space

	return no_space_docs


def harvest_text(files):
	"""

	:param files: LDC files containing raw text data
	:return: Dictionary of document base names (e.g. wsj_0013) to string of non-whitespace characters in the document
	"""

	docs = {}

	for file_ in files:
		docname = os.path.basename(file_)
		if "." in docname:
			docname = docname.split(".")[0]
		try:
			text = io.open(file_,encoding="utf8").read()
		except:
			text = io.open(file_,encoding="Latin1").read()  # e.g. wsj_0142
		text = text.replace(".START","")  # Remove PDTB .START codes
		text = re.sub(r'\s','', text)  # Remove all whitespace
		docs[docname] = text

	return docs


def get_proxy_data():
	import requests
	out_posts = {}
	tab_delim = requests.get("https://corpling.uis.georgetown.edu/gum/fetch_text_proxy.py").text
	for line in tab_delim.split("\n"):
		if "\t" in line:
			post, text = line.split("\t")
			out_posts[post] = text
	return out_posts


def restore_docs(path_to_underscores,text_dict):
	def restore_range(range_string, underscored, tid_dict):
		output = []
		tok_ids = []
		range_strings = range_string.split(",")
		for r in range_strings:
			if "-" in r:
				s, e = r.split("-")
				tok_ids += list(range(int(s),int(e)+1))
			else:
				tok_ids.append(int(r))

		for tok in underscored.split():
			if tok == "<*>":
				output.append(tok)
			else:
				tid = tok_ids.pop(0)
				output.append(tid_dict[tid])
		return " ".join(output)

	dep_files = glob(path_to_underscores+os.sep+"*.conllu")
	tok_files = glob(path_to_underscores+os.sep+"*.tok")
	rel_files = glob(path_to_underscores+os.sep+"*.rels")
	skiplen = 0
	token_dict = {}
	tid2string = defaultdict(dict)
	for file_ in dep_files + tok_files + rel_files:
		lines = io.open(file_,encoding="utf8").readlines()
		underscore_len = 0  # Must match doc_len at end of file processing
		doc_len = 0
		if file_.endswith(".rels"):
			output = []
			violation_rows = []
			for l, line in enumerate(lines):
				line = line.strip()
				if l > 0 and "\t" in line:
					fields = line.split("\t")
					docname = fields[0]
					text = text_dict[docname]
					if "GUM_" in docname and "reddit" not in docname:  # Only Reddit documents need reconstruction in GUM
						output.append(line)
						continue
					doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, orig_label, label = line.split("\t")
					underscore_len += unit1_txt.count("_") + unit2_txt.count("_") + unit1_sent.count("_") + unit2_sent.count("_")
					if underscore_len == 0:
						sys.stderr.write("! Non-underscored file detected - " + os.path.basename(file_) + "\n")
						sys.exit(0)
					unit1_txt = restore_range(unit1_toks, unit1_txt, tid2string[docname])
					unit2_txt = restore_range(unit2_toks, unit2_txt, tid2string[docname])
					unit1_sent = restore_range(s1_toks, unit1_sent, tid2string[docname])
					unit2_sent = restore_range(s2_toks, unit2_sent, tid2string[docname])
					plain = unit1_txt + unit2_txt + unit1_sent + unit2_sent
					plain = plain.replace("<*>","").replace(" ","")
					doc_len += len(plain)
					fields = doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, orig_label, label
					line = "\t".join(fields)
					if doc_len != underscore_len and len(violation_rows) == 0:
						violation_rows.append(str(l) + ": " + line)
				output.append(line)

		else:
			tokfile = True if ".tok" in file_ else False
			output = []
			parse_text = ""
			docname = ""
			for line in lines:
				line = line.strip()
				if "# newdoc_id " in line:
					tid = 0
					if parse_text !="":
						if not tokfile:
							token_dict[docname] = parse_text
					parse_text = ""
					docname = re.search(r'# newdoc_id ?= ?([^\s]+)',line).group(1)
					if "GUM" in docname and "reddit" not in docname:
						output.append(line)
						continue
					if docname not in text_dict:
						raise IOError("! Text for document name " + docname + " not found.\n Please check that your LDC data contains the file for this document.\n")
					if ".tok" in file_:
						text = token_dict[docname]
					else:
						text = text_dict[docname]
					doc_len = len(text)
					underscore_len = 0

				if "GUM" in docname and "reddit" not in docname:
					output.append(line)
					continue

				if line.startswith("# text"):
					m = re.match(r'(# ?text ?= ?)(.+)',line)
					if m is not None:
						i = 0
						sent_text = ""
						for char in m.group(2).strip():
							if char != " ":
								sent_text += text[i]
								i+=1
							else:
								sent_text += " "
						line = m.group(1) + sent_text
						output.append(line)
				elif "\t" in line:
					fields = line.split("\t")
					if skiplen < 1:
						underscore_len += len(fields[1])
						fields[1] = text[:len(fields[1])]
					if not "-" in fields[0] and not "." in fields[0]:
						parse_text += fields[1]
						tid += 1
						tid2string[docname][tid] = fields[1]
					if not tokfile:
						if fields[2] == '_' and not "-" in fields[0] and not "." in fields[0]:
							fields[2] = fields[1]
						elif fields[2] == "*LOWER*":
							fields[2] = fields[1].lower()
					if skiplen < 1:
						text = text[len(fields[1]):]
					else:
						skiplen -=1
					output.append("\t".join(fields))
					if "-" in fields[0]:  # Multitoken
						start, end = fields[0].split("-")
						start = int(start)
						end = int(end)
						skiplen = end - start + 1
				else:
					output.append(line)

		if not doc_len == underscore_len:
			if ".rels" in file_:
				sys.stderr.write(
					"\n! Tried to restore file " + os.path.basename(file_) + " but source text has different length than tokens in shared task file:\n" + \
					"  Source text in data/: " + str(doc_len) + " non-whitespace characters\n" + \
					"  Token underscores in " + file_ + ": " + str(underscore_len) + " non-whitespace characters\n" + \
					"  Violation row: " + violation_rows[0])
			else:
				sys.stderr.write("\n! Tried to restore document " + docname + " but source text has different length than tokens in shared task file:\n" + \
						  "  Source text in data/: " + str(doc_len) + " non-whitespace characters\n" + \
						  "  Token underscores in " + file_+": " + str(underscore_len) + " non-whitespace characters\n")
			with io.open("debug.txt",'w',encoding="utf8") as f:
				f.write(text_dict[docname])
				f.write("\n\n\n")
				f.write(parse_text)
			sys.exit(0)

		if not tokfile and parse_text != "":
			token_dict[docname] = parse_text

		with io.open(file_, 'w', encoding='utf8', newline="\n") as fout:
			fout.write("\n".join(output) + "\n")

	sys.stderr.write("o Restored text in " + str(len(dep_files)) + " .conllu files, " + str(len(tok_files)) +
					 " .tok files and "+ str(len(rel_files)) + " .rels files\n")


p = ArgumentParser()
p.add_argument("corpus",action="store",choices=["rstdt","pdtb","cdtb","tdb","gum","all"],default="all",help="Name of the corpus to process or 'all'")
p.add_argument("-m","--mode",action="store",choices=["add","del"],default="add",help="Use 'add' to restore data and 'del' to replace text with underscores")
opts = p.parse_args()

# DEL MODE - MAKE UNDERSCORES
if opts.mode == "del":  # Remove text from resources that need to be underscored for distribution
	files = []
	if opts.corpus == "rstdt" or opts.corpus == "all":
		corpus_files = glob(os.sep.join(["..","data","eng.rst.rstdt","*.conllu"])) + \
					   glob(os.sep.join(["..","data","eng.rst.rstdt","*.tok"])) + \
					   glob(os.sep.join(["..", "data", "eng.rst.rstdt", "*.rels"]))
		sys.stderr.write("o Found " + str(len(corpus_files)) + " files in " + os.sep.join(["..","data","eng.rst.rstdt"]) + "\n")
		files += corpus_files
	if opts.corpus == "pdtb" or opts.corpus == "all":
		corpus_files = glob(os.sep.join(["..","data","eng.pdtb.pdtb","*.conllu"])) + \
					   glob(os.sep.join(["..","data","eng.pdtb.pdtb","*.tok"])) + \
					   glob(os.sep.join(["..", "data", "eng.pdtb.pdtb", "*.rels"]))
		sys.stderr.write("o Found " + str(len(corpus_files)) + " files in " + os.sep.join(["..","data","eng.pdtb.pdtb"]) + "\n")
		files += corpus_files
	if opts.corpus == "cdtb" or opts.corpus == "all":
		corpus_files = glob(os.sep.join(["..","data","zho.pdtb.cdtb","*.conllu"])) + \
					   glob(os.sep.join(["..","data","zho.pdtb.cdtb","*.tok"])) + \
					   glob(os.sep.join(["..","data","zho.pdtb.cdtb","*.rels"]))
		sys.stderr.write("o Found " + str(len(corpus_files)) + " files in " + os.sep.join(["..","data","zho.pdtb.cdtb"]) + "\n")
		files += corpus_files
	if opts.corpus == "tdb" or opts.corpus == "all":
		corpus_files = glob(os.sep.join(["..","data","tur.pdtb.tdb","*.conllu"])) + \
					   glob(os.sep.join(["..","data","tur.pdtb.tdb","*.tok"])) + \
					   glob(os.sep.join(["..","data","tur.pdtb.tdb","*.rels"]))
		sys.stderr.write("o Found " + str(len(corpus_files)) + " files in " + os.sep.join(["..","data","tur.pdtb.tdb"]) + "\n")
		files += corpus_files
	if opts.corpus == "gum" or opts.corpus == "all":
		corpus_files = glob(os.sep.join(["..","data","eng.rst.gum","*.conllu"])) + \
					   glob(os.sep.join(["..","data","eng.rst.gum","*.tok"])) + \
					   glob(os.sep.join(["..","data","eng.rst.gum","*.rels"]))
		sys.stderr.write("o Found " + str(len(corpus_files)) + " files in " + os.sep.join(["..","data","eng.rst.gum"]) + "\n")
		files += corpus_files
	underscore_files(files)
	sys.stderr.write("o Replaced text with underscores in " + str(len(files)) + " files\n")
	sys.exit(1)


# ADD MODE - RESTORE TEXT

# Prompt user for corpus folders
if opts.corpus == "rstdt" or opts.corpus == "all":
	rstdt_path = input("Enter path for LDC RST-DT data/ folder:\n> ")
	if not os.path.isdir(rstdt_path):
		sys.stderr.write("Can't find directory at: " + rstdt_path + "\n")
		sys.exit(0)
	files = glob(os.sep.join([rstdt_path,"RSTtrees-WSJ-main-1.0","TRAINING","*.edus"])) + glob(os.sep.join([rstdt_path,"RSTtrees-WSJ-main-1.0","TEST","*.edus"]))
	docs2text = harvest_text(files)
	restore_docs(os.sep.join(["..","data","eng.rst.rstdt"]),docs2text)
if opts.corpus == "pdtb" or opts.corpus == "all":
	pdtb_path = input("Enter path for LDC Treebank 2 raw/wsj/ folder:\n> ")
	if not os.path.isdir(pdtb_path):
		sys.stderr.write("Can't find directory at: " + pdtb_path + "\n")
		sys.exit(0)
	files = []
	for i in range(0,25):
		dir_name = str(i) if i > 9 else "0" + str(i)
		files += glob(os.sep.join([pdtb_path,dir_name,"wsj_*"]))
	docs2text = harvest_text(files)
	restore_docs(os.sep.join(["..","data","eng.pdtb.pdtb"]),docs2text)
if opts.corpus == "cdtb" or opts.corpus == "all":
	cdtb_path = input("Enter path for LDC Chinese Discourse Treebank 0.5 raw/ folder:\n> ")
	if not os.path.isdir(cdtb_path):
		sys.stderr.write("Can't find directory at: " + cdtb_path + "\n")
		sys.exit(0)
	files = glob(os.sep.join([cdtb_path,"*.raw"]))
	docs2text = harvest_text(files)
	restore_docs(os.sep.join(["..","data","zho.pdtb.cdtb"]),docs2text)
if opts.corpus == "tdb" or opts.corpus == "all":
	tdb_path = input("Enter path for Turkish Discourse Bank 1.0 raw/01/ folder:\n> ")
	if not os.path.isdir(tdb_path):
		sys.stderr.write("Can't find directory at: " + tdb_path + "\n")
		sys.exit(0)
	files = glob(os.sep.join([tdb_path,"*.txt"]))
	docs2text = harvest_text(files)
	restore_docs(os.sep.join(["..","data","tur.pdtb.tdb"]),docs2text)

if opts.corpus == "gum" or opts.corpus == "all":
	response = input("Do you want to try downloading reddit data from an available server?\n"+
					 "Confirm: you are solely responsible for downloading reddit data and "+
					 "may only use it for non-commercial purposes:\n[Y]es/[N]o> ")
	if response == "Y":
		print("Retrieving reddit data by proxy...")
		data = get_proxy_data()
		docs2text = get_no_space_strings(data)
	else:
		sys.stderr.write("Aborting\n")
		sys.exit(0)
	restore_docs(os.sep.join(["..","data","eng.rst.gum"]),docs2text)
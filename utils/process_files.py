"""
process_files.py

Script to clean input dependency treebanks in CoNLL-U format
for the DISRPT 2019 shared task, and optionally output the plain text version

Output files contain three kinds of lines:
  * Token lines - 10 column, tab delimited CoNLL-U format
  * Blank lines between sentences - multiple consecutive blank lines will be deleted
  * Comment lines (some optional) - begin with # and contain one of three key-value pairs, e.g.:
    * # newdoc_id = GUM_academic_art  [This is the identifier indicating a new corpus document]
    * # sent_id = GUM_academic_art-1  [If the treebank has native sentence IDs, there are included in this way for reference]
    * # text = Aesthetic Appreciation and Spanish Art: [Original, untokenized sentence text - not available for all treebanks]

Other types of comments are deleted from original treebanks.

If the plain (-p) option is used, a plain version without sentence and tree information is also outputted

"""

__author__ = "Amir Zeldes"
__license__ = "Apache 2.0"
__version__ = "1.0.1"

import io, sys, os, re
from argparse import ArgumentParser
from glob import glob

p = ArgumentParser()
p.add_argument("files",help="A glob pattern with files to process")
p.add_argument("-p","--plain",action="store_true",help="Also output plain text version")
p.add_argument("-s","--sample",action="store_true",help="Set outfile names to sample.tok and sample.conll")
p.add_argument("-c","--corpus",action="store",help="Corpus name to output",default=None)

opts = p.parse_args()

files = glob(opts.files)
last_line = ""
multitoken = False

for infile in files:
	sys.stderr.write("i Processing file " + os.path.basename(infile) + "\n")
	docids = False
	firstdoc = True
	output = []
	plain_output = []
	token_counter = 0
	outfile = os.path.basename(infile)
	name_parts = outfile.rsplit(".",1)
	if len(name_parts) > 1:
		extension = name_parts[-1]
		outfile = name_parts[0]
	else:
		extension = "conll"
	outfile = outfile + "_clean." + extension
	plainfile = outfile + "_plain.tok"
	if opts.sample:
		outfile = "sample.conll"
		plainfile = "sample.tok"
	if opts.corpus is not None:
		outfile = opts.corpus
		if "_dev" in infile:
			outfile += "_dev"
		elif "_test" in infile:
			outfile += "_test"
		else:
			outfile += "_train"
		plainfile = outfile + ".tok"
		outfile += ".conll"
	lines = io.open(infile,encoding="utf8").read().strip().replace("\r","\n").split("\n")
	for i, line in enumerate(lines):
		if "\t" in line:  # Token line
			token_counter += 1
			fields = line.split("\t")
			multitoken = "-"  in fields[0]
			if len(fields) != 10:
				raise IOError("x Token line must contain 10 fields but " + str(len(fields)) + " found on line " + str(i) + "\n")
			output.append(line)
			fields[0] = str(token_counter)
			fields[2:] = ["_"] * 8
			if "BeginSeg=Yes" in line:
				fields[9] = "BeginSeg=Yes"
			elif "Seg=B-Conn" in line:
				fields[9] = "Seg=B-Conn"
			if "Seg=I-Conn" in line:
				fields[9] = "Seg=I-Conn"
			if not multitoken:  # No multitokens in .tok files
				plain_output.append("\t".join(fields))
		else:
			if line.startswith("#"):
				m = re.match(r'# ?(newdoc_id|sent_id|text) ?= ?(.+)',line)
				if m is not None:
					docids = True
					outline = "# " + m.group(1) + " = " + m.group(2)
					if m.group(1) == "newdoc_id":
						if not firstdoc:
							plain_output.append("")
							if not last_line == "":  # Make sure there is a blank line between documents
								output.append("")
						else:
							firstdoc = False
						plain_output.append(line)
						token_counter = 0
					output.append(line)
			elif len(line.strip()) == 0:
				if last_line.strip() != "":
					output.append("")

		last_line = line.strip()

	if not docids:
		sys.stderr.write("i No newdoc IDs in file " + os.path.basename(infile) + "\n")

	with io.open(outfile,'w',encoding="utf8",newline="\n") as f:
		f.write("\n".join(output) + "\n")

	if opts.plain:
		with io.open(plainfile,'w',encoding="utf8",newline="\n") as f:
			f.write("\n".join(plain_output) + "\n")


sys.stderr.write("Done.\n")
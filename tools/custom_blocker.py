## BLOCK ON ARTIST AND TITLE ###

import os


class Custom_blocker(object, table_a, table_b):

	def __init__ (self, table_a, table_b):
		self.fp_a = os.path.relpath(table_a, os.curdir)
		self.fp_b = os.path.relpath(table_b, os.curdir)
		with open(fp_a,'r') as data_file:
		   self.a_att = data_file.readline().split(",")
		with open(fp_b,'r') as data_file:
			self.b_att = data_file.readline().split(",")	
		self.candiates = 0

	def block_by(self, a_att, b_att):
		
		if a_att not in self.a_att:
			print("Error: attribute " + a_att + " not found\n")
			return
		else 
			idx_a = self.a_att.index(a_att)
		
		if b_att not in self.b_att:
			print("Error: attribute " + b_att + " not found\n")
			return
		else
			idx_b = self.b_att.index(b_att)

		 ##### Start Inverted Index #####
		if os.getpath.pathsize(self.fp_a) > os.getpath.pathsize(self.fp_b):
			bigger = self.fp_a
			idx = idx_a
		else
			bigger = self.fp_b
			idx = idx_b

		# Construct inverted index. Keys are ranges of string length 
		invert_idx = {}
		with open(bigger, 'r') as data_file:
			for i, info in enumerate(data_file):
				data = data_file.split(",")
				target_att = data[idx]
				target_len = len(target_att)
				







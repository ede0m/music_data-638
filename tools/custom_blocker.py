## BLOCK ON ARTIST AND TITLE ###

import os
import re
from pprint import pprint


class Custom_blocker(object):

	def __init__ (self, table_a, table_b):
		self.fp_a = os.path.relpath(table_a, os.curdir)
		self.fp_b = os.path.relpath(table_b, os.curdir)
		with open(self.fp_a,'r') as data_file:
		   tmp = data_file.readline().rstrip().split(",")
		   self.a_att = [x.strip(" ") for x in tmp] 
		with open(self.fp_b,'r') as data_file:
			tmp = data_file.readline().rstrip().split(",")
			self.b_att = [x.strip(" ") for x in tmp] 

		self.ignore_words = ["A", "I", "the", "The", "In", "in", "are", "of", "Are", "you", "You", "Me", "me"]
		self.invert_idx = {}
		self.candiates = 0

	
	def block_by(self, a_att, b_att):
		
		if a_att not in self.a_att:
			print("Error: attribute " + a_att + " not found in A\n")
			return
		else:
			idx_a = self.a_att.index(a_att)
		
		if b_att not in self.b_att:
			print("Error: attribute " + b_att + " not found in B\n")
			return
		else:
			idx_b = self.b_att.index(b_att)

		 ##### Start Inverted Index #####
		if os.path.getsize(self.fp_a) > os.path.getsize(self.fp_b):
			bigger = self.fp_a
			smaller = self.fp_b
			idx_big = idx_a
			idx_sm = idx_b
		else:
			bigger = self.fp_b
			smaller = self.fp_a
			idx_big = idx_b
			idx_sm = idx_a

		# Construct inverted index. String Tokens
		with open(bigger, 'r') as data_file:
			itr = iter(data_file)
			next(itr)
			for i, line in enumerate(itr):
				data = line.split(",")
				ID = data[0]
				target_att = data[idx_big]
				#target_len = len(target_att)
				tokens = re.split(r'[- /]', target_att)
				for token in tokens:
					if self.invert_idx.get(token) == None:
						self.invert_idx[token] = {}
						self.invert_idx[token][ID] = target_att
					else:
						self.invert_idx[token][ID] = target_att

		
		# Start blocking process #
		with open(smaller, 'r') as data_file:
			itr = iter(data_file)
			next(itr)
			
			for i, line in enumerate(itr):
				data = line.split(",")
				target_att = data[idx_sm]
				tokens = re.split(r'[- /]', target_att)
				tokens[:] = [value for value in tokens if value != ""]
				print('\n\n', tokens)

				# Get to first indexable token 
				for j in range(len(tokens)):
					if tokens[j] in self.ignore_words:
						print('IGNORED A COMMON TOKEN ')
						continue
					docs = self.invert_idx.get(tokens[j])
					if docs != None:
						print('FOUND FIRST TOKEN: ', tokens[j])
						break
				
				if not docs:
					print("EXAMPLE TOKENS EXAUSTED \n")
				else:
					# for subsequent tokens in string, converge on IDs that also have that token
					for token in tokens[(j+1):]: 
						query = self.invert_idx.get(token)
						# this token may help converge on a possible candidate
						if query != None:
							print('FOUND ', token)
							temp = {}
							for key in docs.keys():
								if query.get(key) != None:
									temp[key] = docs[key]
							# Token helped converge
							if temp:
								docs = temp
								# We have exausted all but one possibility for a match
								if len(docs.keys()) == 1:
									print('POSSIBLE MATCH')
									pprint(docs)
									print(self.invert_idx[token][list(docs.keys())[0]])
									print('\n\n')
									self.candiates+=1
									break
							# Token did not help
							else:
								print("TOKIN", token, 'does not benifit')

							if tokens[len(tokens)-1] == token:
								print('DID NOT CONVERGE. LIST OF CLOSEST MATCHES\n')
								pprint(docs)
						else:
							print('NO ENTRY ', token)
					





blocker = Custom_blocker( "../csv/msd_final.csv", "../csv/musicbrainz_final.csv")
#print(blocker.a_att)
#print(blocker.b_att)
blocker.block_by("Title", "Song")
print('\n\n', blocker.candiates)






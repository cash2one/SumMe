'author pol'
from PreProcessing import preprocessor
import math
#should contain these:
#a list containing:
	#sentence number,
	#sentence itself
	#words(this would be a dict)
		#word
		#POS tag
article =  [] #is this shit even needed

global sentences
sentences = [] # 0sentence number, 1the sentence, 2the tuples of words 0 = word 1 = pos 
			#and their corresponding POS tags, and the 3language id
			#4when chunkSents is invoked chunks of the sentence is appended
			#5when getTriple() is invoked svos of the sentence is appended
			#6when getFreq() is invoked frequencies of the sentences is also appended
#class Sentence:
#	self.SentNum
#	self.langId
#	self.Sent
#	self.SentenceScore
#	self.Words
#	self.Chunks


def chunkSents():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.append(preprocessor.enChunk(sents[2]))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.append(preprocessor.tlChunk(sents[2]))
			sentences[sents[0]] = sents
	#return sentences

def clearMem():
	global sentences 
	sentences = []
	#return sentences

def getTriple():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.append(preprocessor.getSVO(sents[4],True))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.append(preprocessor.getSVO(sents[4],False))
			sentences[sents[0]] = sents
	#return sentences



def getSentences(str):
	
	sents  = preprocessor.sentence_tokenizer(str)
	sentNum = 0
	sentence = [] 
	global sentences
	sentences = []
	for sent in sents:
		sentence.append(sentNum)
		sentence.append(sent)
		ID = preprocessor.LangDetect(sent)
		if ID == "en":
			sentence.append(getPOS(sent))
			sentence.append(ID)
			print(ID+" "+sent)
		elif ID =="tl":
			sentence.append(getFilPOS(preprocessor.tokenizer(sent)))
			sentence.append(ID)
			print(ID+" "+sent)
		else :
			sentence.append(getPOS(sent))
			sentence.append(ID)
			print(ID+" "+sent)
		sentNum+=1
		sentences.append(sentence)
		sentence = []
		
	#return sentences
	#article.append(sentences)
	
	#article = [] #clears the article altogether
	#for sent in article:
	#	print(sent)
	#	print("\n")
	
def getPOS(sent):
	words = []
	POS = preprocessor.posTagger(sent)
	for item in POS:
		word = (item[0],item[1])
		words.append(word)
	return words

def getFilPOS(sent):
	words = []
	return preprocessor.filposTagger(sent)

def getFreq():
	global sentences
	for sents in sentences:
		if sents[3] =="en":
			sents.append(preprocessor.getFreqs(sents[4],True))
			sentences[sents[0]] = sents
		elif sents[3] =="tl":
			sents.append(preprocessor.getFreqs(sents[4],False))
			sentences[sents[0]] = sents
	#return sentences
	#	idf = math.log10(len(sentences)/n[1])
	#	print(idf)
	#	ideff.append((n[0],idf))
def getIDF():
	global sentences
	nWords = []
	
	for sents in sentences:
		for tup in sents[6]:
			if tup[0][0] not in nWords:
				nWords.append(tup[0][0])
	nDocs = Docs(nWords,[0]*len(nWords))
	for sents in sentences:
		for tup in sents[6]:
			if tup[0][0] in nWords :
				nDocs.show[nDocs.words.index(tup[0][0])] +=1
	for n in nDocs.words:
		print(nDocs.show[nDocs.words.index(n)])
		idf = math.log10(len(sentences)/nDocs.show[nDocs.words.index(n)])
		print(idf)
		print(n)
class Docs:
	def __init__(self, words,show):
		self.words = words
		self.show = show

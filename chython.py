# -*- coding: utf-8 -*-
import re
import parser
import sys
import codecs

keywords = {
          # logic
          u'和':"and",
          u"且":"and",
          u"或":"or",
          u"或者":"or",
          u"真": "True",
          u"假":"False",
          u"实":"True",
          u"虛":"False",
          u"空":"None",
          u"等于":"==",
          u"少于":"<",
          u"多于":">",
          u"少于或等于":"<=",
          u"少于或者等于":"<=",
          u"多于或等于":">=",
          u"多于或者等于":">=",
          u"不等于":"!=",
          # def
          u'定义':"def",
          u"类":"class",
          u"我":"self",
          u"自个儿":"self",
          u"共用":"global",
          u"全域":"global",
          # import
          u"从":"from",
          u"导入":"import", # I don't like this name.
          u"作为":"as",
          # flow
          u"返回":"return",
          u"略过":"pass",
          u"引发":"raise",
          u"继续":"continue",
          # control
          u"如果":"if",
          u"假使":"elif",
          u"否则如果":"elif",
          u"否则":"else",
          # for loop
          u"取":"for",
          u"自":"in",
          u"在":"in",
          u"不在":"not in",
          # while loop
          u"当":"while",
          u"跳出":"break",
          u"中断":"break",
          # try
          u"尝试":"try",
          u"异常":"except",
          u"最后":"finally",
          u"申明":"assert",
          # built in methods
          u"执行":"exec",
          u"函数":"lambda",
          u"打印":"print",
          u"伴隨":"with",
          u"产生":"yield",
          # type casts
          u"整数":"int",
          u"字符串":"str",
          # functions
          u"范围":"range",
          # modules
          u"系统":"sys",
          u"数学":"math",
}

splitters = [
	'.',
	",",
	"{",
	"}",
	"(",
	")",
	"[",
	"]",
	"+",
	"-",
	"/",
	"*",
	"\t",
	"\"",
	"\'",
	"\t",
	"\n",
	" "]

def translate(list_of_words):
	translated = []
	for word in list_of_words:
		if word in keywords:
			translated.append(keywords[word])
		else:
			if is_chinese(word):
				translated.append(to_unicode_name(word))
			else:
				translated.append(word)
	return translated

def is_chinese(word):
	for char in word:
		if ord(char) > 255:
			return True
	return False

def to_unicode_name(word):
	result = ''
	for char in word:
		ordinal = ord(char)
		if ordinal > 255:
			result = '{r}{w}'.format(r=result, w='n'+str(ord(char)))
	return result

def find_next_splitter(string, current_index):
	for i in range(current_index, len(string)):
		if string[i] in splitters:
			return i
	return len(string)

def to_python_terms(string):
	list_of_words = []
	index = 0
	while index < len(string):
		next_splitter = find_next_splitter(string, index)
		splitter = string[next_splitter]
		list_of_words.append(string[index:next_splitter])
		list_of_words.append(splitter)
		index = next_splitter+1
	return list_of_words

source_file = sys.argv[1]
target_file = sys.argv[2]
chinese_source = codecs.open(source_file, encoding='utf-8', mode='r')
english_target = open(target_file, 'w')

line = chinese_source.readline()
while line != '':
	orig_list = to_python_terms(line)
	trans_list = translate(orig_list)
	for word in trans_list:
		english_target.write(word)
	line = chinese_source.readline()

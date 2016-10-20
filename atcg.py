''' 
	atcg.py

	Reverse complement plugin for Sublime Text 2
'''
import sublime, sublime_plugin

class BaseCommand(sublime_plugin.TextCommand):
	def __init__(self, view):
		self.view = view

	def run(self, edit):
		view = self.view
		sels = view.sel()
		if len(sels) > 1 or not sels[0].empty():
		    for sel in view.sel():
		    	if not sel.empty():
		    		s = view.substr(sel).strip()
		    		s = self.convert(s)
		    		view.replace(edit, sel, s)
		else:
			all = sublime.Region(0, view.size())
			s = view.substr(all).strip()
			s = self.convert(s)
			view.replace(edit, all, s)

	def convert(self, s):
		complines = []
		# Gracefully handle line endings
		if '\n' in s:
			postfix = '\n'
		else:
			postfix = ''
		for line in s.split('\n'):
			complines.append(''.join(self.process(line)))
		return postfix.join(complines)

class ReverseComplementCommand(BaseCommand):
	@staticmethod
	def process(s):
		return ComplementCommand.process(ReverseCommand.process(s))

class ReverseCommand(BaseCommand):
	@staticmethod
	def process(s):
		return s[::-1]

class ComplementCommand(BaseCommand):
	@staticmethod
	def process(l):
		flip = {
			'A': 'T',
			'C': 'G',
			'G': 'C',
			'T': 'A',
			'N': 'N',
			'a': 't',
			'c': 'g',
			'g': 'c',
			't': 'a',
			'n': 'n'
		}
		line_complement = []
		for i in list(l):
			if not i in flip:
				sublime.error_message('Selection contains non-nucleotides.')
				return False
			line_complement.append(flip[i])
		return line_complement
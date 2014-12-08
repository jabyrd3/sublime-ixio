import sublime, sublime_plugin
from . import requests
class IxioCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			s = ""
			if not region.empty():
				s = self.view.substr(region)
			else:
				s = self.view
			r = requests.post('http://ix.io', data={"f:1":s})
			sublime.set_clipboard(r.text)
			print('ix.io post success: ' + r.text)

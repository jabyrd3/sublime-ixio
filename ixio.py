import sublime, sublime_plugin
from . import requests
import re

SETTINGS_FILE = "ixio.sublime-settings"
settings =  None
username = None
password = None
class IxioCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			s = ""
			if not region.empty():
				s = self.view.substr(region)
			else:
				s = self.view
			if username == None:
				r = requests.post('http://ix.io', data={"f:1":s})
			else:
				r = requests.post('http://ix.io', auth=(username, password), data={"f:1":s})
			sublime.set_clipboard(re.search("(?P<url>https?://[^\s]+)", r.text).group("url"))
			print('ix.io post success: ' + r.text)

class DebugCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print(username)
		print(password)
class StatusCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("status")

def plugin_loaded():
	global settings;
	global username;
	global password;
	settings = sublime.load_settings(SETTINGS_FILE)
	username = settings.get("ixioUn")
	password = settings.get("ixioPw")

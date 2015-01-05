import sublime
import sublime_plugin
import urllib.request
import re
import webbrowser
import libs.html2text

SETTINGS_FILE = "Preferences.sublime-settings"
settings = None
username = None
password = None
statusId = None


class IxioCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				s = self.view.substr(sublime.Region(0, self.view.size()))
			else:
				s = self.view.substr(region)
			if username is None:
				#r = requests.post("http://ix.io", data={"f:1": s})
				print("test")
			else:
				print("test")
				#r = requests.post(
				   #"http://ix.io", auth=(username, password), data={"f:1": s})
			# sublime.set_clipboard(
			#     re.search("(?P<url>https?://[^\s]+)", r.text).group("url"))
			print("ix.io post success: " + r.text)

class StatusCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		r = urllib.request.urlopen("http://ix.io/user/" + username)
		content = html2text.html2text(r.read())
		content += "\n NOTE: select a line and right-click to open that paste in a browser"
		newWindow = self.view.window().new_file()
		activeView = self.view.window().active_view()
		global statusId
		statusId = activeView.id()
		activeView.set_scratch(True)
		activeView.set_name("Your Pastes")
		activeView.replace(edit=edit, r=sublime.Region(0, 0), text=content)
		activeView.sel().clear()


class DoubleClickCommand(sublime_plugin.TextCommand):

	def run_(self, view, args):
		if self.view.id() is statusId:
			jumper = self.view.line(self.view.sel()[0])
			jumper = self.view.substr(jumper)
			if "[[r]]" in jumper and "[[h]]" in jumper:
				goTo = jumper.partition(" ")[0]
				webbrowser.open_new("http://ix.io/" + goTo)
				print(goTo)
			return
		else:
			return


def plugin_loaded():
	global settings
	global username
	global password
	settings = sublime.load_settings(SETTINGS_FILE)
	username = settings.get("ixioUn")
	password = settings.get("ixioPw")

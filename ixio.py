import sublime, sublime_plugin
import sublime-ixio.sublime-package.requests as requests
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
	# here's how it's gonna work
	# first, we need to either get the selection or the window if there is no selection
	# next we need to make an http request with the text as in the body
	# when that returns we need to copy the url in the response to the clipboard
# notify the user of success
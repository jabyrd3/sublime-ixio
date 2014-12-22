import sublime
import sublime_plugin
from . import html2text
from . import requests
import re

SETTINGS_FILE = "ixio.sublime-settings"
settings = None
username = None
password = None


class IxioCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            s = ""
            if not region.empty():
                s = self.view.substr(region)
            else:
                s = self.view.substr(sublime.Region(0, self.view.size()))
            if username == None:
                s = sublime.window
                r = requests.post("http://ix.io", data={"f:1": s})
            else:
                r = requests.post(
                    "http://ix.io", auth=(username, password), data={"f:1": s})
            sublime.set_clipboard(
                re.search("(?P<url>https?://[^\s]+)", r.text).group("url"))
            print("ix.io post success: " + r.text)


class DebugCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print("here we debug")


class StatusCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        r = requests.get("http://ix.io/user/" + username)
        newWindow = self.view.window().new_file()
        activeView = self.view.window().active_view()
        activeView.set_scratch(True)
        activeView.set_name("Your Pastes")
        activeView.replace(edit=edit, r=sublime.Region(0, 0), text=html2text.html2text(r.text))


def plugin_loaded():
    global settings
    global username
    global password
    settings = sublime.load_settings(SETTINGS_FILE)
    username = settings.get("ixioUn")
    password = settings.get("ixioPw")

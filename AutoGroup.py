"""
AutoGroup v0.1
by Diego Marques
https://github.com/dmosantos/sublime-AutoGroup
"""
import sublime
import sublime_plugin
import logging

def getLogger():
	logging.basicConfig(format='%(message)s')
	logger = logging.getLogger('test')
	logger.setLevel(logging.DEBUG)
	return logger

class openFileCommand(sublime_plugin.EventListener):

	settings = None

	def on_load(self, view):
		self.view = view

		l = getLogger().info

		if self.settings == None:
			self.settings = sublime.load_settings("AutoGroup.sublime-settings")

		config = self.settings.get("ext-map")

		file_ext = view.file_name().split('.')[-1]

		selected_group = -1

		for group in config:
			if file_ext in config[group]:
				selected_group = int(group)
				break

		if selected_group >= 0:
			window = self.view.window()
			index = len(window.views_in_group(selected_group))
			window.set_view_index(window.active_view(), selected_group, index)

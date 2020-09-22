import wx
from typing import List
from mvc.models.entities.note import Note
from mvc.controllers.main_controller import MainController
from mvc.views.base_view import BaseView


class MainView(BaseView):

    def __init__(self, controller: MainController):
        BaseView.__init__(self, "MVC Note Application")
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        new_note_label = wx.StaticText(panel, label="New Note:")
        note_input = wx.TextCtrl(panel)
        add_note_button = wx.Button(panel, label="Add Note")
        clear_all_button = wx.Button(panel, label="Clear All")
        note_list_label = wx.StaticText(panel, label="Note List:")

        vbox.Add(new_note_label)
        vbox.AddSpacer(8)
        vbox.Add(note_input, 0, wx.EXPAND)
        vbox.AddSpacer(8)
        vbox.Add(add_note_button, 0, wx.EXPAND)
        vbox.AddSpacer(8)
        vbox.Add(clear_all_button, 0, wx.EXPAND)
        vbox.AddSpacer(8)
        vbox.Add(note_list_label)

        add_note_button.Bind(wx.EVT_BUTTON, self.on_add_note_button_clicked)
        clear_all_button.Bind(wx.EVT_BUTTON, self.on_clear_all_button_clicked)

        panel.SetSizer(vbox)

        self.note_list_label = note_list_label
        self.note_input = note_input

        self.update_view(self.controller.get_all_notes())

    def update_view(self, items: List[Note]):
        self.note_list_label.SetLabel(
            "Note List:\n" + "\n".join([f"{i + 1}. {note.content}" for i, note in enumerate(items)]))

    def on_clear_all_button_clicked(self, e):
        # Clear all note
        # Your code here
        self.controller.clear_all()
        # Update view
        # Your code here
        self.update_view(self.controller.get_all_notes())
        pass

    def on_add_note_button_clicked(self, e):
        content = self.note_input.GetValue()
        self.note_input.SetValue("")
        # Add new note
        # Your code here
        self.controller.add_note(content)
        # Update view
        # Your code here
        self.update_view(self.controller.get_all_notes())
        pass

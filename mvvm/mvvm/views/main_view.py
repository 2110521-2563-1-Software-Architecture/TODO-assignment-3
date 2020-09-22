import wx
from typing import List
from mvvm.models.entities.note import Note
from mvvm.view_models.main_view_model import MainViewModel
from mvvm.views.base_view import BaseView


class MainView(BaseView):

    def __init__(self):
        BaseView.__init__(self, "MVVM Note Application")
        # Create view model
        self.view_model = MainViewModel()

        self.init_ui()

        # Bind observable
        self.bind_observable()

    def bind_observable(self):
        # Subscribe to the notes behavior subject and update the view when the data change
        self.view_model.note_behavior_subject.subscribe(lambda note: self.update_view(note))
        pass

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

    def update_view(self, items: List[Note]):
        self.note_list_label.SetLabel(
            "Note List:\n" + "\n".join([f"{i + 1}. {note.content}" for i, note in enumerate(items)]))

    def on_clear_all_button_clicked(self, e):
        # Clear all notes
        self.view_model.clear_all()
        pass

    def on_add_note_button_clicked(self, e):
        content = self.note_input.GetValue()
        self.note_input.SetValue("")
        # Add new note
        self.view_model.add_note(content)

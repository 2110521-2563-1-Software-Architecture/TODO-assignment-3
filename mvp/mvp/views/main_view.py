import wx
from typing import List
from mvp.contracts.main_contract import MainContract
from mvp.models.entities.note import Note


class MainView(MainContract.View):

    def __init__(self):
        MainContract.View.__init__(self, "MVP Note Application")

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

        if self.presenter:
            self.presenter.get_all_notes()

    def update_view(self, items: List[Note]):
        self.note_list_label.SetLabel(
            "Note List:\n" + "\n".join([f"{i + 1}. {note.content}" for i, note in enumerate(items)]))

    def on_clear_all_button_clicked(self, e):
        # Clear all notes
        # Your code here
        if self.presenter:
            self.presenter.clear_all()
        pass

    def on_add_note_button_clicked(self, e):
        content = self.note_input.GetValue()
        self.note_input.SetValue("")
        # Add note
        # Your code here
        if self.presenter:
            self.presenter.add_note(content)

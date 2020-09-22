from typing import List
from mvp.contracts.main_contract import MainContract
from mvp.models.repositories.note_repository import NoteRepository
from mvp.models.entities.note import Note


class MainPresenter(MainContract.Presenter):

    def __init__(self, view: MainContract.View, note_repository: NoteRepository):
        MainContract.Presenter.__init__(self, view)
        self.note_repository = note_repository

    # Your code here
    def add_note(self, note: str):
        self.note_repository.add_note(note)
        if self.view:
            self.view.update_view(self.get_all_notes())
        pass

    def get_all_notes(self):
        return self.note_repository.get_all_notes()
        pass

    def clear_all(self):
        self.note_repository.clear_all_notes()
        if self.view:
            self.view.update_view(self.get_all_notes())
        pass

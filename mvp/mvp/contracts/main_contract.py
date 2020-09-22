from typing import List
from mvp.views.base_view import BaseView
from mvp.presenters.base_presenter import BasePresenter
from mvp.models.entities.note import Note


class MainContract:

    class View(BaseView):

        # Your code here
        def update_view(self, items: List[Note]):
            pass

        pass

    class Presenter(BasePresenter):

        # Your code here
        def add_note(self, note: str):
            pass

        def get_all_notes(self):
            pass

        def clear_all(self):
            pass

        pass

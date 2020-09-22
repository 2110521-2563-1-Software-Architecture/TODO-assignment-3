from mvc.models.repositories.note_repository import NoteRepository

class MainController:
    def __init__(self):
        # Create note repository here
        # Your code here
        self.noteRepo = NoteRepository()
        pass
    
    def get_all_notes(self):
        # Return all notes
        # Your code here
        return self.noteRepo.get_all_notes()
        pass

    def add_note(self, note: str):
        # Add note
        # Your code here
        self.noteRepo.add_note(note)
        pass

    def clear_all(self):
        # Clear all note
        # Your code here
        self.noteRepo.clear_all_notes()
        pass

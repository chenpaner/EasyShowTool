bl_info = {
    "name": "Easy Node Notes",
    "author": "Atticus",
    "description": "Adds notes to your node editor",
    "blender": (4, 1, 0),
    "version": (0, 0, 1),
    "location": "",
    "doc_url": "",
    "warning": "",
    "category": "Node"
}

from . import ops_notes


def register():
    ops_notes.register()


def unregister():
    ops_notes.unregister()

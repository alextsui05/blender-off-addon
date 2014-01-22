# 
# http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts/Guidelines/Addons
#
import os
import bpy
from bpy.props import (BoolProperty,
    FloatProperty,
    StringProperty,
    )
from bpy_extras.io_utils import (ImportHelper,
    )

#if "bpy" in locals():
#    import imp
#    if "import_off" in 

bl_info = {
    "name": "OFF format",
    "description": "Import-Export OFF, Import OFF mesh only, for now.",
    "author": "Alex Tsui",
    "version": (0, 1),
    "blender": (2, 69, 0),
    "location": "File > Import-Export",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/"
                "Scripts/My_Script",
    "category": "Import-Export"}

class ImportOFF(bpy.types.Operator, ImportHelper):
    """Load an OFF Mesh file"""
    bl_idname = "import_mesh.off"
    bl_label = "Import OFF Mesh"

    filename_ext = ".off"
    filter_glob = StringProperty(
        default="*.off",
        options={'HIDDEN'},
    )

    def execute(self, context):
        #from . import import_off

        keywords = self.as_keywords()

        load(self, context, self.filepath)

        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(ImportOFF.bl_idname, text="OFF Mesh (.off)")

def register():
    print("Hello world")
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(menu_func_import)

def unregister():
    print("Goodbye world")
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)

def load(operator, context, filepath):
    print("TODO: load file")
    filepath = os.fsencode(filepath)
    file = open(filepath, 'r')
    file.readline()
    vcount, fcount, ecount = [int(x) for x in file.readline().split()]
    verts = []
    facets = []
    for i in range(0, vcount):
        line = file.readline()
        px, py, pz = [float(x) for x in line.split()]
        verts.append((px, py, pz))

    for i in range(0, fcount):
        line = file.readline()
        unused, vid1, vid2, vid3 = [int(x) for x in line.split()]
        facets.append((vid1, vid2, vid3))

# TODO: How do i assemble a mesh object?

if __name__ == "__main__":
    register()

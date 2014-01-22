#####
#
# Copyright 2014 Alex Tsui
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
#####

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
    unpack_list,
    unpack_face_list,
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

        mesh = load(self, context, self.filepath)
        if not mesh:
            return {'CANCELLED'}

        scene = bpy.context.scene
        obj = bpy.data.objects.new(mesh.name, mesh)
        scene.objects.link(obj)
        scene.objects.active = obj
        obj.select = True

        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(ImportOFF.bl_idname, text="OFF Mesh (.off)")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)

def load(operator, context, filepath):
    # Parse mesh from OFF file
    # TODO: Add support for NOFF and COFF
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

    # Assemble mesh
    off_name = bpy.path.display_name_from_filepath(filepath)
    mesh = bpy.data.meshes.new(name=off_name)
    mesh.vertices.add(len(verts))
    mesh.vertices.foreach_set("co", unpack_list(verts))

    mesh.tessfaces.add(len(facets))
    mesh.tessfaces.foreach_set("vertices_raw", unpack_face_list(facets))

    mesh.validate()
    mesh.update()

    return mesh

if __name__ == "__main__":
    register()

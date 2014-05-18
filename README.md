Blender OFF Addon
-----
This addon will add the ability to import and export ascii OFF mesh files in Blender.

Quickstart
-----
1. Clone this project.
2. Open Blender.
3. Go to File > User Preferences... > Addons tab.
4. On the bottom, click Install from File...
5. Select the import_off.py from this project.
6. Check the checkbox by the OFF addon to enable it.
7. Now you should have new import/export menu items to work with OFF files.

License
-----

This addon is licensed under Apache 2.0.

    http://www.apache.org/licenses/LICENSE-2.0

Links
-----

Blender Wiki page: http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/Object_File_Format_%28.off%29


Developer notes
-----

http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts/Guidelines/Addons

To have your script show up in the Add-Ons panel, it needs to:

    be in the addons/ directory
    contain a dictionary called "bl_info"
    define register() / unregister() functions. 

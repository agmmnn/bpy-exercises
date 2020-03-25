bl_info = {
    "name": "imperfect",
    "description": "make imperfect the selected objects.",
    "author": "agmmnn",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View 3D > Toolbar > imperfect",
    "warning": "",
    "wiki_url": "https://github.com/agmmnn/bpy-exercises",
    "category": "Object"
}

import bpy
import random
import math

# -----------------------------------------------------
# UI
# -----------------------------------------------------
class IMP_Panel(bpy.types.Panel):
    bl_label = "Imperfectionism"
    bl_idname = "PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'imperfect'
        
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.7

        row = layout.row()
        row.label(text="Location:",icon='DRIVER_DISTANCE')
        
        row = layout.row()
        row.label(text="Rotation:",icon='OUTLINER_OB_CURVE')
        
        row = layout.row()
        row.label(text="Scale:",icon='UV_FACESEL')
        
        row = layout.row()
        row.operator("make.imp", icon='GHOST_ENABLED')

class MAKE_IMP(bpy.types.Operator):
    bl_label = "Make Imperfect"
    bl_idname = "make.imp"
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            
            #move object a random distance
            obj.location.x += random.uniform(-0.1, 0.1)
            obj.location.y += random.uniform(-0.1, 0.1)
            obj.location.z += random.uniform(0, 0)
            
            #rotate object a random amount
            obj.rotation_euler.x += math.radians(random.uniform(-0, 0))
            obj.rotation_euler.y += math.radians(random.uniform(-0, 0))
            obj.rotation_euler.z += math.radians(random.uniform(-5, 5))

            #scale object a random amount
            obj.scale.x += random.uniform(-0.01, 0.01)
            obj.scale.y += random.uniform(-0.01, 0.01)
            obj.scale.z += random.uniform(0, 0)

        return {'FINISHED'}

# -----------------------------------------------------
# Reg
# -----------------------------------------------------
def register():
    bpy.utils.register_class(IMP_Panel)
    bpy.utils.register_class(MAKE_IMP)
    
def unregister():
    bpy.utils.unregister_class(IMP_Panel)
    bpy.utils.unregister_class(MAKE_IMP)
    
if __name__ == "__main__":
    register()
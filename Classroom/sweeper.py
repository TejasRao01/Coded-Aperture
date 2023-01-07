import os
import bpy
import numpy as np
beg_val = 6.0
end_val = 9.0
x = np.linspace(beg_val, end_val, 31)
output_dir = r"C:\Users\CFI Workstation\Documents\Blender\Cupcakes\Multifocal""\\"
for i in x:
    bpy.context.object.data.dof.focus_distance = i
    bpy.context.scene.render.filepath = os.path.join(output_dir, "Cupcakes_%.2f.png" % i)
    bpy.ops.render.render(write_still = True)
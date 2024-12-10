import maya.cmds as cmds

def create_joints_from_selected_locators():
    selected_objects = cmds.ls(selection=True, transforms=True)
    if not selected_objects:
        cmds.warning("Aucun objet sélectionné. Veuillez sélectionner des locators.")
        return
    
    for obj in selected_objects:
        children = cmds.listRelatives(obj, shapes=True, type="locator")
        if children:
            position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
            cmds.select(clear=True)
            joint = cmds.joint(position=position)
            joint_name = obj + "_joint"
            cmds.rename(joint, joint_name)
        else:
            cmds.warning(f"L'objet '{obj}' n'est pas un locator. Ignoré.")
    
    cmds.select(clear=True)
    print("Joints créés pour tous les locators sélectionnés.")

# Call the function
create_joints_from_selected_locators()

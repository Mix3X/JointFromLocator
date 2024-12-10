Maya Script: Create Joints from Selected Locators

This Python script for Autodesk Maya creates joints at the positions of selected locators. It is designed for riggers and animators who need to streamline the process of generating joints based on locator positions.

Features:
Automatic Joint Creation: For every selected locator, a joint is created at its world-space position.
Custom Naming: Joints are named based on the corresponding locator's name, with _joint appended for easy identification.
Error Handling: Objects that are not locators are automatically skipped with a warning.
Independent Joints: Each joint is created independently, avoiding hierarchical connections.

Requirements:
Autodesk Maya 2022 or newer.
Basic familiarity with Maya's Python scripting environment.

Installation:
Clone this repository or download the script file:
bash
Copy code
git clone https://github.com/your-username/maya-create-joints.git
Open the script editor in Maya (Windows > General Editors > Script Editor).
Paste the code from create_joints_from_locators.py into the Python tab.
Usage
In your Maya scene, select the locators for which you want to create joints.
Run the script in the Maya script editor.
Joints will be created at the position of each selected locator, and they will be renamed to match the locator names.
Example Output
If you select locators named locator1 and locator2, the script will create joints named:

locator1_joint
locator2_joint
Code
python
Copy code
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

import nuke

# Initialize the toggle value.
try:
    toggle
except NameError:
    toggle = 1

# Increment the toggle value when hitting the "Enable/Disable" button
toggle += 1

print(toggle)

# Getting all added node classes as a list.
node_classes = [node.strip() for node in
                nuke.thisNode()["node_classes"].getValue().split(",") if node]


# Getting all added node labels as a list.
node_labels = [node.strip() for node in
               nuke.thisNode()["node_labels"].getValue().split(",") if node]


# Set the process nodes to either all nodes or selected nodes.
if nuke.thisNode()["all_nodes"].getValue():
    process_nodes = nuke.allNodes()
else:
    process_nodes = nuke.selectedNodes()


# Disable/Enable nodes using node class and labels.
for node in process_nodes:
    # Process from node classes list.
    if node.Class() in node_classes and node.knob("disable"):
        node["disable"].setValue(toggle % 2 == 0)

    # Process from node labels list if "include labels" is enabled.
    if node["label"].getValue() in node_labels and node.knob("disable") and nuke.thisNode()["include_labels"].getValue():
        node["disable"].setValue(toggle % 2 == 0)


# Update the label of Toggle Button while toggling.
if toggle % 2 == 0:
    nuke.thisKnob().setLabel("Disabled")
else:
    nuke.thisKnob().setLabel("Enabled")

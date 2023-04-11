import nuke

# Add all already added classes into a list.
node_classes = [node.strip() for node in nuke.thisNode()[
    "node_classes"].getValue().split(",") if node]
# Add selected classes into a list.
selected_classes = [node.Class() for node in nuke.selectedNodes()
                    if node and node.knob("disable")]
# Combine selected classes with existing classes.
node_classes.extend(selected_classes)
# Remove the duplicate classes and sort alphabetically.
all_classes = sorted(set(node_classes))
# Set the combined classes into the "node classes" box separated with comma.
nuke.thisNode()["node_classes"].setValue(", ".join(all_classes))


print(all_classes)

import nuke

# Add all already added labels into a list.
node_labels = [node.strip() for node in
               nuke.thisNode()["node_labels"].getValue().split(",") if node]
# Add selected labels into a list.
selected_node_labels = [node["label"].getValue() for node in
                        nuke.selectedNodes() if node.knob("disable") and node["label"].getValue()]

# or use below snippet-
# selected_node_labels = [node.knob("label").getValue() for node in
#                         nuke.selectedNodes() if node.knob("disable")]

# Combine selected labels with existing labels.
node_labels.extend(selected_node_labels)
# Remove the duplicate labels and sort alphabetically.
all_labels = sorted(set(node_labels))
# Set the combined labels into the "node labels" box separated with comma.
nuke.thisNode()["node_labels"].setValue(", ".join(all_labels))


print(all_labels)

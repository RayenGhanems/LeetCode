# Explenation:
# Function dfs: #
the the soul of this algo. it basically :
. goes right when node we are standing on is lower than the high argument (since if the node is higher than the high then node.right​ is also greater being thatn .right leads to a greater number than node)
. goes left when the node we are standin on is higher than the low argument for the same reason of above
. and boes both ways if the node is in the good reagion. and in this case also out +=node.val

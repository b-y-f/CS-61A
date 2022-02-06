# Add tree
# if not t1:
#     return t2
# if not t2:
#     return t1
# new_label = label(t1) + label(t2)
# t1_children, t2_children = branches(t1), branches(t2)
# length_t1, length_t2 = len(t1_children), len(t2_children)
# if length_t1 < length_t2:
#     t1_children += [None for _ in range(length_t1, length_t2)]
# elif len(t1_children) > len(t2_children):
#     t2_children += [None for _ in range(length_t2, length_t1)]
# return tree(new_label, [add_trees(child1, child2) for child1, child2 in zip(t1_children, t2_children)])

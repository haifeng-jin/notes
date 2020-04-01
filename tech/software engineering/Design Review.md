# Design Review
#tech/software engineering#
The content of a design review doc:
End-to-end Workflows:
Detailed Class Signatures

Two ways to evaluate whether a design is good or not.
1. The complexity of the class communication graph.
2. How intuitive it is when you read the code.

About the class communication graph:
The ideal communication graph of a project would be a hierarchical one, where the classes only communicate with the parents (the classes using the class). If there are too many interconnections between the non-parent-child classes, it is a bad design. The parent and child relation should also be intuitive.

About rewriting a project:
Rewriting a project is a good way to keep the class structures simple. The cost of rewriting is a one time cost. The cost of not rewriting would be the cost of engineering efforts in the future as the project grows. The larger the project grows the more cost there will be. Therefore, for a long term project, we should always try to rewrite the project to keep the class structures simple. It would cost some now but less in the future.
#--- Day 7: Recursive Circus ---

#Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. 
#A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

#One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. 
#At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. 
#At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

#You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, 
#their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. 
#You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, 
#you're not sure which program gave which information.

#For example, if your list is the following:

#pbga (66)
#xhth (57)
#ebii (61)
#havc (66)
#ktlj (57)
#fwft (72) -> ktlj, cntj, xhth
#qoyq (66)
#padx (45) -> pbga, havc, qoyq
#tknk (41) -> ugml, padx, fwft
#jptl (61)
#ugml (68) -> gyxo, ebii, jptl
#gyxo (61)
#cntj (57)
#...then you would be able to recreate the structure of the towers that looks like this:

#                gyxo
#              /     
#         ugml - ebii
#       /      \     
#      |         jptl
#      |        
#      |         pbga
#     /        /
#tknk --- padx - havc
#     \        \
#      |         qoyq
#      |             
#      |         ktlj
#       \      /     
#         fwft - cntj
#              \     
#                xhth
#In this example, tknk is at the bottom of the tower (the bottom program), and is holding up ugml, padx, and fwft. Those programs are, in turn, 
#holding up other programs; in this example, none of those programs are holding up any other programs, and are all the tops of their own towers. 
#(The actual tower balancing in front of you is much larger.)

#Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?

#--- Part Two ---

#The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. 
#Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

#For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, 
#or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

#In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

#However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

#ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
#padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
#fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
#As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: 
#it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

#Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?



from FileReader import read_file
from collections import Counter

#=============================================================================
class ListNode():
#
#-----------------------------------------------------------------------------
    #=============================================================================
    def __init__(self, name, weight):
    #
    #-----------------------------------------------------------------------------
        self.m_weight = int(weight)
        self.m_name = name
        self.m_child_names = []
        self.m_children = []
        self.m_parent = None
        self.m_tower_weight = 0

    #=============================================================================
    def append_child_node(self, child):
    #
    #-----------------------------------------------------------------------------
        self.m_children.append(child)

    #=============================================================================
    def append_child_name(self, name):
    #
    #-----------------------------------------------------------------------------
        self.m_child_names.append(name)

    #=============================================================================
    def add_parent(self, parent):
    #
    #-----------------------------------------------------------------------------
        self.m_parent = parent

    #=============================================================================
    def calculate_tower_weight(self):
    #
    # The tower weight is the node weight plus the weight of all the children
    #
    #-----------------------------------------------------------------------------
        child_weight = 0
        for child in self.m_children:
            if (child.m_tower_weight == 0):
                child.calculate_tower_weight()
            child_weight += child.m_tower_weight
        self.m_tower_weight = self.m_weight + child_weight

    #=============================================================================
    def is_balanced(self):
    #
    # A node is balanced if all of the children have the same weight and are 
    # balanced
    #
    #-----------------------------------------------------------------------------
        if len(self.m_children) == 0:
            return True
        
        first_weight = self.m_children[0].m_tower_weight
        for child in self.m_children:
            if child.m_tower_weight != first_weight:
                return False
            if not child.is_balanced:
                return False
        return True
    
    #=============================================================================
    def find_problem_child(self):
    #
    # Find the unbalanced or overweight child
    #
    #-----------------------------------------------------------------------------
        if len(self.m_children) == 0:
            return None

        for child in self.m_children:
            if not child.is_balanced():
                return [child, False]
        
        # Because only one node needs to change it should not be possible to have 
        # two children in balance who do not weigh the same.
        # Otherwise either one could change and it would then all be balanced

        if (len(self.m_children) == 2):
            print ("Something has gone very wrong")

        # Find the child who's weight does not match
        weights = [child.m_tower_weight for child in self.m_children]
        counting = Counter(weights)
        index = weights.index(min(counting, key=counting.get))
        return [self.m_children[index], True]

#=============================================================================
def line_to_node(line):
#
# Turn the line into a node
# A line has the form abcd (01) 
# Then an optional -> CDEF, GHIJ
#
#-----------------------------------------------------------------------------
    parts = line.split(" ")
    
    stripped_parts = []

    for part in parts:
        if (part == "->"):
            continue
        stripped = part.replace("(","")
        stripped = stripped.replace(")", "")
        stripped = stripped.replace(",","")
        stripped_parts.append(stripped)
    node = ListNode(stripped_parts[0], stripped_parts[1])

    # Add the names of any child node
    for i in range (2, len(stripped_parts)):
        node.append_child_name(stripped_parts[i])

    return node


#=============================================================================
def run_day_7():
#
#-----------------------------------------------------------------------------
    lines = read_file("Day7_Data.txt")
    
    
    list_of_unlinked_nodes = []
    for line in lines:
        list_of_unlinked_nodes.append(line_to_node(line))
    
    # Now link the list
    for parent_node in list_of_unlinked_nodes:
        for child_name in parent_node.m_child_names:
            for child_node in list_of_unlinked_nodes:
                if child_name == child_node.m_name:
                    parent_node.append_child_node(child_node)
                    child_node.add_parent(parent_node)
    

    # We can find the bottom node from any point by going back through parents
    start = list_of_unlinked_nodes[0]
    while (start.m_parent != None):
        start = start.m_parent
    start.calculate_tower_weight()

    # Now find the node that needs to change
    current = start
    while (True):
        results = current.find_problem_child()
        if (results[1]):
            print ("The node that needs to change is " + results[0].m_name)
            # Problems weigth is 
            problem_total_weigth = current.m_tower_weight
            problem_weight = current.m_weight
            #Sibling total weight 
            weights = [child.m_tower_weight for child in current.m_children]
            counting = Counter(weights)
            # Expected weight of the stacks
            common = max(counting, key=counting.get)
            for child in results[0].m_children:
                common -= child.m_tower_weight
            print ("It should weight " + str(common))
            return common
        else :
            current = results[0]
    return 0
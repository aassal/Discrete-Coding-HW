#COMS3203 DISCRETE MATHEMATICS
#CODING ASSIGNMENT 2

#YOUR NAME: Amina Assal, Fernando Perez-Hickman
#YOUR UNI: aa4290, fp2390

import itertools

'''
Returns the proposition, formatted in string form.

Parameters:
prop (list): proposition in nested list form

Returns:
string: 'prop' in string form
'''
def format_prop(prop):
    # BASE CASE: #####################################
    if len(prop) == 1:
        return prop[0]
    ##################################################

    # UNARY OPERATOR (not): ##########################
    if 2 == len(prop):
        # the following two variable declarations are missing LHS #
        op = prop[0] # missing LHS
        p1 = prop[1] # missing LHS
        statement = format_prop(p1)

        if "not" == op:
            formatted_prop = op + " " + "(" + statement + ")"
            return (formatted_prop)
        else:
            raise ValueError("Unary proposition is not not.")
    ##################################################

    # BINARY OPERATOR (and, or, if, iff, xor): #######
    elif 3 == len(prop):
        # the following three variable declarations are missing LHS #
        op = prop[0] # missing LHS
        p1 = prop[1] # missing LHS
        statement1 = format_prop(p1)
        p2 = prop[2] # missing LHS
        statement2 = format_prop(p2)

        if op not in ("if", "iff", "or", "and", "xor"):
            raise ValueError("Binary proposition does not have valid connectives.")

        # change "if" and "iff" representation
        if "if" == op:
            op = "->"
        elif "iff" == op:
            op = "<->"

        # format left and right sides of a binary operation
        left_prop = statement1
        right_prop = statement2
        formatted_prop = "(" + left_prop + ")" + " " + op + " " + "(" + right_prop + ")"
        return formatted_prop
    ####################################################

    # INVALID LENGTH ####################################
    else:
        raise ValueError("Proposition incorrect length.")
    #####################################################

'''
Returns the evaluation (True or False) as an int (1 or 0) of the proposition,
given a proposition in list form and a list of values for each atomic variable.

Parameters:
prop (list): proposition in nested list form.
values (list): list of integers, either 0 or 1 indicating False or True for
each atomic variable in the proposition. 

Returns:
int: 0 for False, 1 for True
'''
def eval_prop(prop, values):
    # BASE CASE: #####################################
    if len(prop) == 1:
        # fill in here # 
        atomic_prop_id =  int(values[0])
        return atomic_prop_id
    ##################################################

    # UNARY OPERATOR (not): ##########################
    elif 2 == len(prop):
        # the following two variable declarations are missing LHS #
        op = prop[0] # missing LHS
        p1 = prop[1] # missing LHS
        statement = eval_prop(p1, values)

        if "not" == op:
            if values[0] == 0:
                return 1
            if values[0] == 1:
                return 0
        else:
            raise ValueError("Unary proposition is not not.")
    ##################################################

    # BINARY OPERATOR (and, or, if, iff, xor): #######
    elif 3 == len(prop):
        # the following three variable declarations are missing LHS #
        op = prop[0] # missing LHS
        p1 = prop[1] # missing LHS
        statement1 = eval_prop(p1, values)
        p2 = prop[2] # missing LHS
        statement2 = eval_prop(p2, values)

        if op not in ("if", "iff", "or", "and", "xor"):
            raise ValueError("Binary proposition does not have valid connectives.")

        # evaluate left and right sides of a binary operation
        left = values[0]
        right = values[1]
        #value of each prop to be evaluated in the end

        # the line here is an example. fill in the rest.
        if "and" == op:
            return int(left and right)
        elif "or" == op:
            return int(left or right)
        elif "if" == op:
            if left == 1 and right == 0:
                return 0
            return 1
        elif "iff" == op:
            if left == 1 and right == 0:
                return 0
            if right == 1 and left == 0:
                return 0
            return 1
        else: # fill in :
            if left == 1 and right == 0:
                return 1
            if right == 1 and left == 0:
                return 1
            return 0

    # INVALID LENGTH ####################################
    else:
        raise ValueError("Proposition incorrect length.")
    #####################################################

'''
Prints a truth table given a proposition in nested list form and 
an integer defining the number of atomic variables. 

Parameters:
prop (list): proposition in nested list form.
n_var (int): the number of atomic variables in prop.  

Returns:
None
'''
def print_table(prop, n_var):
    '''
    fill in here. you will have to use eval_prop and format_prop,
    and will probably have to use the itertools package (already
    imported for you).
    '''
    pass


if __name__ == '__main__':
    print("---------------------------------------")
    print("Coding Assignment 2: Propositional Logic")
    print("---------------------------------------")

    print()
    values = [1]
    prop = ["not", ["p1"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 1]
    prop = ["and", ["p1"], ["p2"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 0]
    prop = ["iff", ["p1"],["p2"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 1, 0]
    prop = ["if", ["and", ["p1"], ["not", ["p2"]]], ["p3"]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    prop_str = format_prop(prop)
    print("Evaluating proposition p =", prop_str)
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 0, 1]
    prop = ["iff", ["p1"], ["or", ["p2"], ["not", ["p3"]]]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    # print("---------------------------------------------------")
    # print("Table:")
    # print_table(["if", ["and", ["p1"], ["not", ["p2"]]], ["p3"]], 3)

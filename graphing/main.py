''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Homework Helper

This program prompts for an input name of an algebraic function then prompts the user for necessary coefficiencts.
It will compute the graph and ask the user if they wish to display the graph or save it to a file.

Authors: Annette Clarke, Nicholas Hodder, Daniel Harris
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import graphing
import numpy
from matplotlib import pyplot as plt




#All available functions to choose from
graph_list = {
            "linear"      : "f(x) = a*x + b", 
            "quadratic"   : "f(x) = a*x^2 + b*x + c", 
            "cubic"       : "f(x) = a*x^3 + b*x^2 + c*x + d", 
            "quartic"     : "f(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e", 
            "exponential" : "f(x) = a * b^(c*x + d)", 
            "logarithmic" : "f(x) = a * log(b*x + c)",
            "sine"        : "f(x) = a * sin(b*x + c)", 
            "cos"         : "f(x) = a * cos(b*x + c)", 
            "squareroot"  : "f(x) = a * sqrt(b*x + c)",
            "cuberoot"    : "f(x) = a * sqrt(b*x + c)"
}


def graph_type():
    '''
        Description: Receives user choice for which function to graph, validates 
        Parameters: None
        Returns: User selected function type
    '''
    while True:
        
        function_type = input("Please select a graph type, or enter 'List' to view available choices: ")
            
        if not function_type.isalpha():
            print("Error: Function name must be one word with all alphabetical characters ONLY.")
            continue
        elif function_type.lower() == "list":
            graph_type_list()
        elif function_type.lower() not in graph_list:
            print("Error: The name provided does not match an available function type.")
            continue
        else:
            print("Graph type selected: {}".format(function_type))
            break
    return function_type.lower()
    
    

#When called, shows a list of all available graph types to select
def graph_type_list():
    print("Here is a list of available graph types, displaying name and function:\n")
    for key,value in graph_list.items():
        print("{}: {}\n".format(key.upper(),value))
    return

#Inputs the range with user prompt returns start and end as separate values.
def get_range():
    while True:
        try:
            range_start = int(input("Input the start of the range: "))
            range_end = int(input("Input the end of the range: "))
            range_spacing = int(input("Input the range spacing (leave blank for default): "))
            if (range_start < -2147483648) or (range_end > 2147483647):
                print("Warning: Extremely large ranges may potentially not work as intended on certain hardware.")
            break
        except:
            print("Error: Must be a number")
            continue
    return range_start, range_end, range_spacing


#Prompts user for their choice on graph features, validates the feature name within a loop until correct value entered.
def feature_choices():
    xlabel = None 
    ylabel = None
    title = None
    features = [xlabel, ylabel, title]
    fname = ["x-axis", "y-axis", "title"]
    counter = 0
    for feature in features:
        while True:
            feature = input("Enter a label for the " + fname[counter] + " or leave blank to skip: ")
            counter = counter + 1
            is_valid = validate(feature)
            if is_valid == "skip":
                feature = False
                break
            elif is_valid == True:
                break
            #If the entry is invalid the loop will restart, so decrement the counter to retry last value.
            counter = counter - 1    
    legend = input("Enter 'Y' to include a legend or submit any other input (including blank) to skip: ")
    if legend.isspace() or legend.lower != 'y' or not legend:
        legend = False
    return xlabel, ylabel, title, legend
 

#Validates the user input for naming standards  
def validate(name, deny_special_chars = False):
    if (name.isspace() or not name) and not deny_special_chars:
        return "skip"
    elif not name[0].isalnum:
        print("Error: Name must begin with an alphanumeric character.")
        return False
    if deny_special_chars:
        if not name.isalnum():
            print("Error: Name must contain only alphanumeric characters.")
            return False
    return True


#Creates the graph
def draw_graph(x,y,graph_type,xlabel,ylabel,legend, title):
    # Set axis of the graph we will be using
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    #Plot the graph and assign it a legend label according to it's type
    plt.plot(x,y, label=graph_type)
    
    #Draw the optional graph features if selected by the user
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if legend:
        plt.legend()
    if title:
        plt.title(title)
    plt.savefig("inside_function_test.png")
    
 
 
#Saves the graph to a filename defined by user
def save_graph():
    file_name = input ("Please name the file (it will save as a .png): ")
    while not validate(file_name, deny_special_chars = True):
        file_name = input("Please try again, enter a valid file name: ")
    plt.savefig(file_name + ".png")
    return    
    


#Program Start
if __name__ == "__main__":
    
    while True:
        #Prompt for graph type
        graph_type = graph_type()
        
        #Assign the range using get_range() NOTE: Start value must be assigned before end value followed by spacing. 
        range_start, range_end, range_spacing = get_range()
        x = numpy.linspace(range_start, range_end, range_spacing)
        
        #Determine graphing function from graphing.py, use get_function() to execute the retrieved function.
        get_function = getattr(graphing, graph_type)
        y = get_function(x)
        
        #Input choices for graph features.
        xlabel, ylabel, title, legend = feature_choices()
        
        #Render the graph in memory
        draw_graph(x,y,graph_type,xlabel,ylabel,legend,title)
        
        #Display or Save
        while True:
            output_type = input("Would you like to save or display the graph? Please enter 'S' or 'D': ")
            
            if not validate(output_type):
                print("Please try again.")
                continue
            
            output_type = output_type.lower()
            
            if output_type == "d":
                plt.show()
                break
                
            elif output_type == "s":
                save_graph()
                break
            else:
                print("Error: Wrong character entered, please select one of the options.")

        #Continue or end
        cont = input("Would you like to make a new graph? Enter 'Y' to continue or any other input to exit.")
        if cont.lower() != "y":
            break
        
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Homework Helper

This program prompts for an input name of an algebraic function then prompts the user for necessary coefficiencts.
It will compute the graph and ask the user if they wish to display the graph or save it to a file.

Authors: Annette Clarke, Nicholas Hodder, Daniel Harris
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import graphing
import matplotlib.pyplot as plt
import matplotlib.image as mp
import numpy


# Create a list for all the different graph names (possibly use for if statement checks)
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


'''Function Definitions'''
#Prompts user for input of which equation to use
def graph_type():
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


#Saves the graph to a filename defined by user
def save_graph():
    file_name = input ("Please name the file: ")
    #validate(file_name) Finish file name validation to block empty names, beginning with special character or including unpermitted characters
    f = open(file_name,"w")
    f.close()
    return 

#Validates the user input for naming standards
def validate(name):
    if name.isspace() or not name:
        name = False
    elif not name[0].isalnum:
        print("Error: Label must begin with an alphanumeric character.")
        return False
    return True

#Creates the graph,
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
    
    #img = mp.imread('graph.png') Trying to display the graph on Cloud9 ignore this if plt.show works - Daniel
    #imgplot = plt.imshow(img)
    plt.show()
    
    


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
        
        
        #Input choices for graph features, ensure the string begins with alphanumeric.
        while True:
            xlabel = input("Enter a label for the x-axis or leave blank to skip: ")
            if xlabel.isspace() or not xlabel:
                xlabel = False
                break
            else:
                if validate(xlabel):
                    break
        while True:    
            ylabel = input("Enter a label for the y-axis or leave blank to skip: ")
            if ylabel.isspace() or not ylabel:
                ylabel = False
                break
            else:
                if validate(ylabel):
                    break
        while True:   
            title = input("Enter a title for the graph or leave blank to skip: ")
            if title.isspace() or not title:
                title = False
                break
            else:
                if validate(title):
                    break
            
        legend = input("Enter 'Y' to include a legend or submit any other input (including blank) to skip: ")
        if str(legend).isspace() or legend.lower != 'y' or not legend:
            legend = False
            
        draw_graph(x,y,graph_type,xlabel,ylabel,legend,title)
        
        
        #Display or Save
        while True:
            output_type = input("Would you like to save or display the graph? Please enter 'S' or 'D': ")
            output_type = output_type.lower()
            
            if output_type == "d":
                draw_graph(x,y,graph_type,xlabel,ylabel,legend,title)
                break
                
            elif output_type == "s":
                save_graph()
                break
            else:
                print("Error: Must be a valid input ('S' or 'D')")


        #Continue or end
        cont = input("Would you like to make a new graph? Enter 'Y' to continue or any other input to exit.")
        if cont.lower() != "y":
            break
        
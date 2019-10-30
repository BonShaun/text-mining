import numpy as np 
import matplotlib.pyplot as plt 

def bar_plot(polarity,  polarity1, subjectivity, subjectivity1):
    n_group = 2
    polarity_data = (polarity, polarity1)
    subjectivity_date = (subjectivity, subjectivity1)

    #create plot 
    fig, ax= plt.subplots()
    index = np.arange(n_group)
    bar_width = 0.35 
    opacity = 0.8 

    rects1 = plt.bar(index, polarity_data, bar_width,
    alpha = opacity,
    color = 'b',
    label = 'User_Input1')
    
    rects2 = plt.bar(index + bar_width, subjectivity_date, bar_width,
    alpha = opacity,
    color = 'r',
    label = 'User_Input2')

    plt.ylabel('Score')
    plt.title('Polarity and Subjectivity Comparison')
    plt.xticks(index + bar_width/2, ('Polarity', 'Subjectivity'))
    plt.legend()

    plt.tight_layout
    plt.show()


bar_plot(0.50, 0.70, 0.45, 0.85)
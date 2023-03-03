from .importData import *
from .modelateData import *
from .tools import *

class Graph:
    
    def __init__(self):
        pass
        
    def load_data(self, path,custom_montage,custom_position, exclude = [None],  electrode_montage_path = None):
        input_data = InputData(path, exclude)
        self.data = input_data.load()
        
        self.ch_names=self.data.ch_names
        if(electrode_montage_path):
            self.ch_names=input_data.set_montage(electrode_montage_path)
        
        input_data.display_info(self.ch_names)
        

    def modelate(self, window_size,custom_montage,custom_position, connectivity, bands = [None], threshold = None):
        print('\033[1m' + 'Model Data.' + '\033[0m')
        print(search(connectivity_measures, connectivity))
        
        model_data = ModelData(self.data, self.ch_names, eval(search(connectivity_measures, connectivity)))  
        connectivity_matrix, G = model_data.connectivity_workflow(bands, window_size, threshold)
        
        return connectivity_matrix, G
        

    def visualize_html(self, graph, name, custom_montage, custom_position, auto_open = True):
        fig = draw_graph(graph,custom_montage, custom_position)
        fig.update_layout(title='', plot_bgcolor='white' ) 
        fig.write_html(str(name) + '_plot.html', auto_open=auto_open, default_height='100%', default_width='100%')
        
        
    def visualize_png(self, graph, name, custom_montage, custom_position,formato='png',height=1000,width=1800):
        fig = draw_graph(graph,custom_montage, custom_position)
        fig.update_layout(title='', plot_bgcolor='white' ) 
        extension = str('.'+formato)
        fig.write_image(str(name) + extension, format=formato,height=1000,width=1800)


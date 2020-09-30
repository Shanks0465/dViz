from graphviz import Digraph
import keras;
from keras.models import Sequential;
from keras.layers import Dense
import random

def viewSimpleNN(model,name,colored=False,cluster=False,labelled=False):
  ''' Returns Architecture Diagram of given Simple Deep Neural Network.

      Parameters:
                    model (Keras Model): A Keras Model Object
                    name (string): Name of the Architecture diagram
                    colored (boolean): Layers to be colored or not
                    cluster (boolean): Display Layer Separation
                    labelled (boolean): Display layer names

            Returns:
                    Model Graph Architecture
  '''
  dense=[]
  units=[]
  layers=[]
  dense.append("input")
  units.append(model.layers[0].input_shape[1])
  m = Digraph(name,format='png')
  m.attr('node',shape='circle')
  if cluster==True:
    layer_name="cluster_"
  else:
    layer_name="layer_"
  for layer in model.layers:
    if(type(layer)==keras.layers.core.Dense):
      dense.append(layer.name)
      units.append(layer.output_shape[1])
  for i in range(len(dense)):
    with m.subgraph(name=layer_name+str(i)) as c:
      if labelled==True:
        c.attr(label="layer_"+str(i),labeljust="l",height="5",width="10",rank='same')
      if colored==True:
        col_value="#"+"%06x" % random.randint(0, 0xFFFFFF)
        c.node_attr.update(style='filled', color=col_value, fontcolor=col_value)
      else:
        c.node_attr.update(fontcolor="white")
      layer=dense[i]
      unit=units[i]
      cache=[]
      for j in range(unit):
        c.node(layer+str(j))
        cache.append(layer+str(j))
      layers.append(cache)
  i=0;
  while i<len(layers)-1:
    j=i+1
    for x in layers[i]:
      for y in layers[j]:
        m.edge(x,y)
    i+=1
  m.render()
  return m
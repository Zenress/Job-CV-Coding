import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))

#In the tf.keras.layers package, layers are objects. To construct a layer,
#simply construct the object. Most layers take as a first argument the number
#of output dimension / channels.
layer = tf.keras.layers.Dense(100)
#The number of input dimensions is often unnecessary, as it can be inferred
#the first time the layer is used, but it can be provided if you want to
#specify it manually, which is useful in some complex models.
layer = tf.keras.layers.Dense(10, input_shape=(None,5))

#To use a layer, simply call it.
layer(tf.zeros([10,5]))

#Layers have many useful methods. For example, you can inspect all variables
#In a layer using 'layer.variables' and trainable variables using
#'layer.trainable_variables'. In this case a fully-connected layer
#will have variables for weights and biases.
print(layer.variables)

#The variables are also accessible through nice accessors
print(layer.kernel, layer.bias)
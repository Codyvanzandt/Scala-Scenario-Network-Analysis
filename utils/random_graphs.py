import numpy

def generate_random_edge_weight():
    mu, std = (4.50, 3.74) # result of analysis.collection_level_analysis.mean_and_std_edge_weight()
    return numpy.log( numpy.random.lognormal(mu, std) )
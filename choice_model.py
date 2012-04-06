"""
Test script for using pandas.SparseDataFrame for choice model data structure
"""

# $Revision:$

from pandas.sparse.api import SparseDataFrame
from pandas.sparse.array import make_sparse
from pandas import DataFrame, MultiIndex
from itertools import product
import numpy as np

n = 5
nalts = 3

ids=zip(*product(xrange(1, n+1), xrange(1, nalts+1)))
agent_id, choice_id = ids
sdata = SparseDataFrame({'agent_id' : agent_id,
                         'choice_id': choice_id},
                        default_fill_value=0.0)

#alt specific variable
int_var1 = np.zeros(n*nalts)
int_var1[1:n*nalts:nalts] = np.random.randn(1)
sdata['int_var1'] = int_var1

#alt specific dummy
int_var2 = np.zeros(n*nalts)
int_var2[2:n*nalts:nalts] = 1
sdata['int_var2'] = int_var2

#interaction variable
int_var3 = np.random.randn(n*nalts).reshape((n, nalts))
sdata['int_var3'] = int_var3.ravel()

#set index
sdata = sdata.set_index(['agent_id', 'choice_id'])

#coefficients
beta = DataFrame({'int_var1': [.5],
                  'int_var2': [-2.0],
                  'int_var3': [-0.5]
                 })
#utility
sdata['utility'] = np.sum([sdata[v] * beta[v].ix[0] for v in beta.columns])
sdata['exp.utility'] = np.exp(sdata['utility']

#calculate probability ##TODO
sdata.join( sdata.groupby(level='agent_id')['exp.utility'], on='agent_id', lsuffix="sum.")
sdata['prob'] = sdata['exp.utility'] / sdata['sum.exp.utility']

if data is None:
    data = SparseDataFrame(data=int_var,

data = 


class TestCase():
    def setUp():
        dataset = Dataset()
        pass 

    def test_load_dataset():
        pass

    def test_multiple_ids():
        pass

    def test_join_datasets():
        pass

    def test_access_attributes():
        dataset.a.attr_a
        dataset['attr_a']

    def test_group_by():
        dataset = Dataset()
        dataset.group_by()

    def test_group_by_full_dimension():
        dataset = Dataset()
        dataset.group_by()

import pycuda.driver as cuda

#

#
# [ start_addr(used for gpu_function) , data_block_sie , end_addr,  ]  -- gpu_block
#
#



# define a class or not
class cudablock:
  input_pool=[]
  output_pool=[]
  static_data=[]
  input_free=[]
  outut_free=[]
  max_output_size= 10
  max_input_size=  10

  total_input_mem=0

  def __init__(self,basic_block=1024):
    total_input_mem=cuda.mem_alloc(basic_block*self.max_input_size)
    total_output_mem=cuda.mem_alloc(basic_block*self.max_output_size)
    init_input_end=int(total_input_mem)+basic_block*self.max_input_size
    init_output_end=int(total_output_mem)_basic_block*self.max_output_sie
    self.input_pool.append([int(total_input_mem),init_input_end])
    self.output_pool.append([int(total_output_mem),init_output_end])
    pass
  
  def set_data(self,arr):
    if len(input_pool)>0:
      current_=input_pool.pop()
    
  

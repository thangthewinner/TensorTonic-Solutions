import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    x_t = np.array(x_t).reshape(-1) 
    h_prev = np.array(h_prev).reshape(-1)
    b = np.array(b).reshape(-1)

    pre_act = x_t @ Wx + h_prev @ Wh + b
    h_t = np.tanh(pre_act)
    
    return h_t

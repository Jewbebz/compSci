import tensorflow as tf
import data_utils
import seq2seq_model

def train():
    #prepare dataset
    enc_train, dec_train = data_utils.prepare_custom_data(
        gConfig['working_directory'])

    train_set = read_data(enc_train, dec_train)
    

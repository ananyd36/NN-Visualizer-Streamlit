
import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
import numpy as np


URL = 'http://127.0.0.1:8501/'

st.title('Neural Network Visualizer')
st.sidebar.markdown('## Input Image')

if st.button('Get random Prediction'):
    response = requests.post(URL,data={})
    response = json.loads(response.text)
    preds = response.get('prediction')
    image = response.get('image')
    image = np.reshape(image,(28*28))
    
    st.sidebar.image(image,width = 150)
    for layer,p in enumerate(preds):
        numbers = np.squeeze(np.array(p))
        plt.figure(figsize = (32,4))
        if layer ==2:
            row=1
            col=10
        else:
            row=1
            col=16
        for i,number in enumerate(numbers):
            plt.subplot(row,col,i+1)
            plt.imshow(number * np.ones((8,8,3)).astype('float32'))
            plt.xticks([])
            plt.yticks([])
            
            if layer == 2:
                plt.xlabel(str(i),fontsize = 40)
        plt.subplots_adjust(wspace - 0.05, hspace = 0.05)
        plt.tight_layout()
        st.text('Layer {}'.format(i+1))
        st.pyplot()

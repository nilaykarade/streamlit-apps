import streamlit as st
import pandas as pd
import pickle
import numpy as np
st.image("car.png",width=80)
st.title("Used cars price - bulk prediction")

data_file = st.file_uploader("Upload cars data (.csv)", type="csv")
#df=pd.DataFrame()
#if data_file is not None:
df = pd.read_csv(data_file)
loaded_df=st.dataframe(df)

model=pickle.load(open('./models/lr_model.pkl','rb'))

predictions=model.predict(df)
predictions=np.round(predictions,0)
predictions_df=pd.DataFrame(predictions,columns=['Prdicted price'])
result_df=pd.concat([predictions_df,df],axis=1)
st.dataframe(result_df)




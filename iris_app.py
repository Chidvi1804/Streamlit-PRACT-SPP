import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("iris prediction")
iris=load_iris()
x=iris.data
y=iris.target
model=RandomForestClassifier()
model.fit(x,y)

sepal_length=st.slider("Sepal length",float(x[:,0].min()),float(x[:,0].max()))
sepal_width=st.slider("Sepal width",float(x[:,0].min()),float(x[:,0].max()))
petal_length=st.slider("Petal length",float(x[:,0].min()),float(x[:,0].max()))
petal_width=st.slider("Petal width",float(x[:,0].min()),float(x[:,0].max()))

input_data=[[sepal_length,sepal_width,petal_length,petal_width]]
prediction=model.predict(input_data)

st.subheader("prediction:")
st.write("flower",iris.target_names[prediction][0])
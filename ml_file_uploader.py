import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

st.write("ML Model Prediction with file-upload")

uploaded_file=st.file_uploaded("Upload your CSV File here", type=["csv"])

if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write("Preview of uploaded CSV File")
    st.write(df.head())

    target=st.selectbox("select target columns",df.columns)

    if st.button("Train Model"):
        X=df.drop(target,axis=1)
        Y=df[target]

        X=X.select_dtypes(include=['int64','float64'])

        X_train,Y_train,X_test,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
        model=LogisticRegression()
        model.fit(X_train,Y_train)

        y_pred=model.predict(X_test)
        acc=accuracy_score(Y_test,y_pred)

        st.success(f"Model trained with accuracy : {acc:.2f}")

        st.subheader("Predict")
        input_data=[]
        for col in X.columns:
            val=st.number_input(f"Enter {col}",value=float(X[col].mean()))
            input_data.append(val)

        if st.button("Predict"):
            prediction=model.predict([input_data])
            st.write(f"prediction: {prediction[0]}")

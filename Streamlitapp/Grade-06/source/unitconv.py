import streamlit as vAR_st

vAR_st.set_page_config(page_title="My Webpage", page_icon="ds.png", layout='wide')
def unitconversion():
    def kilometer(num):
        if select=="Kilometer" and select2=="Hectometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10
                with col3:
                    vAR_st.write("")
                    vAR_st.subheader(num)
        if select=="Kilometer" and select2=="Decameter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Kilometer" and select2=="Meter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Kilometer" and select2=="Decimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Kilometer" and select2=="Centimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*100000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Kilometer" and select2=="Millimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*1000000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)

    def hectometer(num):
        if select=="Hectometer" and select2=="Kilometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Hectometer" and select2=="Decameter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Hectometer" and select2=="Meter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Hectometer" and select2=="Decimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Hectometer" and select2=="Centimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Hectometer" and select2=="Millimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*100000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)

    def decameter(num):
        if select=="Decameter" and select2=="Kilometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decameter" and select2=="Hectometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decameter" and select2=="Meter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decameter" and select2=="Decimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decameter" and select2=="Centimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decameter" and select2=="Millimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)

    def meter(num):
        if select=="Meter" and select2=="Kilometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Meter" and select2=="Hectometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Meter" and select2=="Decameter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Meter" and select2=="Decimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Meter" and select2=="Centimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Meter" and select2=="Millimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)

    def decimeter(num):
        if select=="Decimeter" and select2=="Kilometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decimeter" and select2=="Hectometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decimeter" and select2=="Decameter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decimeter" and select2=="Meter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decimeter" and select2=="Centimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Decimeter" and select2=="Millimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)

    def centimeter(num):
        if select=="Centimeter" and select2=="Kilometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/100000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Centimeter" and select2=="Hectometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Centimeter" and select2=="Decameter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Centimeter" and select2=="Meter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Centimeter" and select2=="Decimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Centimeter" and select2=="Millimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)

    def millimeter(num):
        if select=="Millimeter" and select2=="Kilometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/1000000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Millimeter" and select2=="Hectometer":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/100000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Millimeter" and select2=="Decameter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Millimeter" and select2=="Meter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Millimeter" and select2=="Decimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)
        if select=="Millimeter" and select2=="Centimeter":
            if k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("The answer is")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.subheader(num)


    col1,col2,col3,col4=vAR_st.columns((2,3,2,2))
    with col2:
        vAR_st.write("")
        vAR_st.subheader("Enter input","")
    with col3:
        num=vAR_st.number_input("",key="Clear3")
    with col2:
        vAR_st.write("")
        vAR_st.subheader("Select the Unit")
    with col3:
        select=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Decimeter","Centimeter","Millimeter"),key="Clear")
    with col2:
        vAR_st.write("")
        vAR_st.subheader("Unit to convert")
    with col3:
        if select=="Kilometer":
            select2=vAR_st.selectbox("",("Select the unit","Hectometer","Decameter","Meter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif select=="Hectometer":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Decameter","Meter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif select=="Decameter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Meter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif select=="Meter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif select=="Decimeter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Centimeter","Millimeter"),key="Clear2")
        elif select=="Centimeter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Decimeter","Millimeter"),key="Clear2")
        else:
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Decimeter","Centimeter"),key="Clear2")

    




    def cleartext():
        vAR_st.session_state["Clear"]="Select the unit"
        vAR_st.session_state["Clear2"]="Select the unit"
        vAR_st.session_state["Clear3"]=0


    

    col5, col6, col7,col8=vAR_st.columns((5,2,2,5))

    with col6:
        vAR_st.write("")
        k=vAR_st.button("Submit")

    if k:
        if select and select2=="Select the unit":
            with col3:
                vAR_st.subheader("Select a unit to convert")

    if k:
        if select =="Select the unit" and select2 !="Select the unit":
            with col3:
                vAR_st.subheader("Select the unit of the number")


    with col7:
        vAR_st.write("")
        vAR_st.button("Clear",on_click=cleartext)

    kilometer(num)
    hectometer(num)
    decameter(num)
    meter(num)
    decimeter(num)
    centimeter(num)
    millimeter(num)













    



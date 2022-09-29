
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px1

from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from PIL import Image






st.set_page_config(layout='wide')


hide_streamlit_style = """
            <style>
    
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


# def layout(*args):

#     style = """
#     <style>
#       footer {visibility: hidden;}
#      .stApp { bottom: 100px; }
#     </style>
#     """

#     style_div = styles(
#         position="fixed",
#         left=0,
#         bottom=0,
#         margin=px(10, 0, 0, 0),
#         width=percent(100),
#         color="black",
#         text_align="center",
#         height="auto",
#         opacity=1
#     )

#     style_hr = styles(
#         margin=px("auto", "auto", "auto", "auto"),

#     )

#     body = p()
#     foot = div(
#         style=style_div
#     )(
#         hr(
#             style=style_hr
#         ),
#         body
#     )

#     st.markdown(style, unsafe_allow_html=True)

#     for arg in args:
#         if isinstance(arg, str):
#             body(arg)

#         elif isinstance(arg, HtmlElement):
#             body(arg)

#     st.markdown(str(foot), unsafe_allow_html=True)


# def footer():
#     myargs = [
        
#         " Made with ❤️ by ",
#         link("https://www.linkedin.com/in/hicham-benabdelkader-5655a5212/", "Benabdelkader Hicham"),
#     ]
#     layout(*myargs)


# if __name__ == "__main__":
#     footer()


st.sidebar.image("gpc.png")




holder1 = st.sidebar.empty()
holder2=st.sidebar.empty()
uploaded_file1 = holder1.file_uploader("Gestion des affectation:",type='xlsx',key=2) 
uploaded_file2=holder2.file_uploader("Gestion des absences:",type='xlsx',key=3)





if uploaded_file1 is  None or uploaded_file2 is  None:
    def layout(*args):

        style = """
        <style>
        footer {visibility: hidden;}
        .stApp { bottom: 100px; }
        </style>
        """

        style_div = styles(
            position="fixed",
            left=0,
            bottom=0,
            margin=px(10, 0, 0, 0),
            width=percent(100),
            color="black",
            text_align="center",
            height="auto",
            opacity=1
        )

        style_hr = styles(
            margin=px("auto", "auto", "auto", "auto"),

        )

        body = p()
        foot = div(
            style=style_div
        )(
            hr(
                style=style_hr
            ),
            body
        )

        st.markdown(style, unsafe_allow_html=True)

        for arg in args:
            if isinstance(arg, str):
                body(arg)

            elif isinstance(arg, HtmlElement):
                body(arg)

        st.markdown(str(foot), unsafe_allow_html=True)


    def footer():
        myargs = [
            
            " Made with ❤️ by ",
            link("https://www.linkedin.com/in/hicham-benabdelkader-5655a5212/", "Benabdelkader Hicham"),
        ]
        layout(*myargs)


    if __name__ == "__main__":
        footer()
    col7,col8,col9=st.columns([1,2,1])
    with col8:
        st.title("GPC-Data_Visualise")
    col1,col2=st.columns(2)
    with col1:
        st.header("C'est quoi GPC-DATA VISUALISE ?" )
        st.write("-"+" "+"GPC-DATA VUSIALISE est une platforme dediée pour les utilisatuers de GPC CARTON, elle permet d'assurer la mission de gestion des affectations des employées et leurs absences en fonction de plusieurs facteurs ainsi de faire un bilan global avec des sections detaillées de visualisation et de filtrage des informations... .")
    with col2:
        st.header("Comment fonctionne-t-elle ?")    
        st.write("-"+" "+"Pour passer à votre page home veuillez uploder vos deux fichiers de type XLSX ci-contre: ( Gestion des affectations et Gestion des absences) .")
        st.write("-"+" "+"Veuillez voir la structure de fichier excel à respecter si-dessous pour éviter tout problème d'importation .")
    st.header("Structure des fichiers")
    col3,col4=st.columns(2)
    with col3:
        with st.expander("Gestion des affectations"):
            st.image('https://raw.githubusercontent.com/gpccarton/data_visualize/main/cap-2.PNG')
    with col4:
        with st.expander("Gestion des absences"):
            st.image('https://raw.githubusercontent.com/gpccarton/data_visualize/main/cap-1.PNG')

elif uploaded_file1 is not None and uploaded_file2 is not None:
    
    data = pd.read_excel(uploaded_file1,index_col=False)
    dfv = pd.read_excel(uploaded_file2,index_col=False)
    holder1.empty()
    holder2.empty()
    col14,col15,col16=st.columns([1,2,1])
    with col15:
        st.title("GPC-DATA VISUALISE")

    #df.index = pd.Series(df.index).fillna(method='ffill')
    Fam=["Famille"]
    Aff=["Affec"]
    data=data.replace('nan','-',regex=True)
    data.loc[:,Fam]=data.loc[:,Fam].fillna(method='ffill')
    # dd=[]
    # for h in data["Famille"].unique():
    #     data79=data[data["Famille"]==h]
    #     dd=dd+[data79["Famille"].to_list()]

    # for p in range(len(dd)):
    #     st.write(dd[p+1][0])

    data.loc[:,Aff]=data.loc[:,Aff].fillna(method='ffill')
    data=data.astype(str)
    data=data.replace(np.nan,'-',regex=True)
    data=data.replace('','-',regex=True)

    data=data.replace('nan','-',regex=True)
    data=data.replace('NaT','-',regex=True)
    data=data.replace('-','-',regex=True)
    data=data.astype(str)
    data=data.replace('NaT','-',regex=True)

    Fam=['Famille']
    dfv.loc[:,Fam]=dfv.loc[:,Fam].fillna(method='ffill')
    datav=dfv.astype(str)
    datavv=datav.replace(np.nan,'',regex=True)
    datavv=datav.replace('nan','',regex=True)
    datavvv=datavv.replace('NaT','',regex=True)
    datavvv=datavv.replace('-','',regex=True)
    datavvv=datavvv.astype(str)
    #st._legacy_dataframe(datavvv)
    datavvv=datavv.replace('NaT','',regex=True)

    
    



    options=st.sidebar.radio(
        "Pages:",
        ('Rapport','Details'))
    if options=='Details':
        options=st.sidebar.radio(
            "Sections:",
            ('Visualiser la Data','Filtrer la Data'))
        if options=='Filtrer la Data':
            data2=data.copy()
            data=data
    
            a=st.sidebar.selectbox("Type des filtres:",["Filter par Famille","Filter par Affectation","Filter par Mle","Filter par name","Filter par Time"])
            
        #     if a=="Filter par Mle":
        #         data['Matricule_1'] = df['Matricule_1'].fillna('-')
        #         data['Matricule_2'] = df['Matricule_2'].fillna('-')
        #         data['Matricule_3'] = df['Matricule_3'].fillna('-')
        #         data1=data[data.Matricule_1 != '-']
        #         data2=data[data.Matricule_2 != '-']
        #         data3=data[data.Matricule_3 != '-']
        #         b=st.sidebar.selectbox("equipe of mle",data1["Matricule_1"].append(data2["Matricule_2"].append(data3["Matricule_3"])))
        #         if b in data["Matricule_1"].to_list():
        #             st.sidebar.write("ok")
            
            if a=="Filter par Famille":
                data_a=data.copy()
                data_a=data_a["Famille"].unique()


                container = st.sidebar.container()
                all = st.sidebar.checkbox("Toutes les familles")
                
                if all:
                    Famille = container.multiselect("Famille:",
                        data["Famille"].iloc[1:,].unique(),data["Famille"].iloc[1:,].unique())
                    
                else:
                    Famille =  container.multiselect("Famille:",
                        data["Famille"].iloc[1:,].unique()
                        )

                df_selection1=data.query(
                    "Famille==@Famille"
                    # & Mle==@id"
                )



                col11,col12,col13, = st.columns([1,19,1])

                with col12:
                    st._legacy_dataframe(df_selection1.astype(str))
    
            
            elif a=="Filter par Affectation":
                container1 = st.sidebar.container()
                all1 = st.sidebar.checkbox("Toutes les affectation")
                
                if all1:
                    Affec = container1.multiselect("Affectation:",
                        data["Affec"].iloc[1:,].unique(),data["Affec"].iloc[1:,].unique())
                else:
                    Affec =  container1.multiselect("Affectation:",
                        data["Affec"].iloc[1:,].unique())
                
                df_selection1=data.query(
                    "Affec==@Affec"
                    # & Mle==@id"
                )
                col11,col12,col13, = st.columns([1,19,1])

                with col12:
                    st._legacy_dataframe(df_selection1.astype(str))
            elif a=="Filter par Mle":
                data_c=data.copy()
                data_c['Matricule_1'] = data_c['Matricule_1'].fillna('-')
                data_c['Matricule_2'] = data_c['Matricule_2'].fillna('-')
                data_c['Matricule_3'] = data_c['Matricule_3'].fillna('-')
                data1=data_c[data_c.Matricule_1 != '-']
                data2=data_c[data_c.Matricule_2 != '-']
                data3=data_c[data_c.Matricule_3 != '-']
                b=st.sidebar.selectbox("Choisir un Matricule:",data1["Matricule_1"].append(data2["Matricule_2"].append(data3["Matricule_3"])))

                
                if b in data1["Matricule_1"].to_list()  :
                    data00=data[data.Matricule_1 != '-']
                    container1 = st.sidebar.container()
                    all1 = st.sidebar.checkbox("Toutes les Matricule_1")
                    
                    if all1:
                        Matricule_1 = container1.multiselect("Matricule_1:",
                            data00["Matricule_1"].to_list(),data00["Matricule_1"].to_list())
                    else:
                        Matricule_1 =  container1.multiselect("Matricule_1:",
                            data00["Matricule_1"].to_list(),
                            default=b
                            )

                            
                    
                    df_selection1=data.query(
                        "Matricule_1==@Matricule_1"
                        # & Mle==@id"
                    )
                    col11,col12,col13, = st.columns((1,19,1))
                    


                    with col12:
                        data55=df_selection1.drop(columns=["Poste_3","Poste_2","Matricule_3","Matricule_2","hd2","hf2"]).copy()
                        st._legacy_dataframe(data55.astype(str))




    

                elif b in data_c["Matricule_2"].to_list() :
                    data00=data[data.Matricule_2 != '-']
                    container1 = st.sidebar.container()
                    all1 = st.sidebar.checkbox("Toutes les Matricule_2")
                    
                    if all1:
                        Matricule_2 = container1.multiselect("Matricule_2:",
                            data00["Matricule_2"].iloc[1:,].to_list(),data00["Matricule_2"].iloc[1:,].to_list())
                    else:
                        Matricule_2 =  container1.multiselect("Matricule_2:",
                            data00["Matricule_2"].iloc[1:,].to_list(),
                            default=b
                            )
                    
                    df_selection1=data.query(
                        "Matricule_2==@Matricule_2"
                        # & Mle==@id"
                    )



                    col1122,col1222,col1322, = st.columns([1,19,1])

                    with col1222:
        
                        st._legacy_dataframe(df_selection1.drop(columns=["Poste_1","Poste_3","Matricule_1","Matricule_3","hd1","hd2","hf1","hf2"]).astype(str))

                else:        
                    data00=data_c[data.Matricule_3 != '-']
                    container1 = st.sidebar.container()
                    all1 = st.sidebar.checkbox("Toutes les Matricule_3")
                    
                    if all1:
                        Matricule_3 = container1.multiselect("Matricule_3:",
                            data00["Matricule_3"].iloc[1:,].to_list(),data00["Matricule_3"].iloc[1:,].to_list())
                    else:
                        Matricule_3 =  container1.multiselect("Matricule_3:",
                            data00["Matricule_3"].iloc[1:,].to_list(),
                            default=b
                        )
                    
                    df_selection1=data.query(
                        "Matricule_3==@Matricule_3"
                        # & Mle==@id"
                    )



                    col1122,col1222,col1322, = st.columns([1,19,1])

                    with col1222:
        
                        st._legacy_dataframe(df_selection1.drop(columns=["Poste_1","Poste_2","Matricule_1","Matricule_2","hd1","hf1"]).astype(str))

            elif a=="Filter par name":
                data_c=data.copy()           
                data1=data[data.Poste_1 != '-']
                data2=data[data.Poste_2 != '-']
                data3=data[data.Poste_3 != '-']
                b=st.sidebar.selectbox("Name",data1["Poste_1"].iloc[1:,].append(data2["Poste_2"].append(data3["Poste_3"])))
                data000=data["Famille"].iloc[1:,].unique()

                # from st_clickable_images import clickable_images

                # clicked = clickable_images(
                #     [
                #         "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
                #         "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
                #         "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
                #         "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
                #         "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
                #     ],
                #     titles=[f"Image #{str(i)}" for i in range(5)],
                #     div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                #     img_style={"margin": "5px", "height": "200px"},
                # )

                # st.markdown(f"Image #{clicked} clicked"
                #  if clicked=="https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700"
                #     st.write("ok")
                #  else:
                #      "No image clicked")

                if b in data_c["Poste_1"].to_list():
                    df_selection1=data.query(
                        "Poste_1==@b"
                        # & Ml
                        # e==@id"
                    )
                    col1122,col1222,col1322, = st.columns([1,19,1])       
                    with col1222:
        
                        st._legacy_dataframe(df_selection1.drop(columns=["Poste_3","Poste_2","Matricule_3","Matricule_2","hd2","hf2"]).astype(str))                        

                elif b in data_c["Poste_2"].to_list():
                    df_selection1=data.query(
                        "Poste_2==@b"
                        # & Ml
                        # e==@id"
                    )
                    col1122,col1222,col1322, = st.columns([1,19,1])       
                    with col1222:
        
                        st._legacy_dataframe(df_selection1.drop(columns=["Poste_1","Poste_3","Matricule_1","Matricule_3","hd1","hf1","hd2","hf2"]).astype(str))

                elif b in data_c["Poste_3"].to_list():
                    df_selection1=data.query(
                        "Poste_3==@b"
                        # & Ml
                        # e==@id"
                    )
                    col1122,col1222,col1322, = st.columns([1,19,1])       
                    with col1222:
        
                        st._legacy_dataframe(df_selection1.drop(columns=["Poste_1","Poste_2","Matricule_1","Matricule_2","hd1","hf1"]).astype(str)) 

            elif a=="Filter par Time":
                # data_c=data.copy()           

                b=st.sidebar.selectbox("Type d'horaire:",["Horaires standards","Horaire particuliers"])
                if b == "Horaires standards":
                    data1=data[data.Poste_1 != '-']
                    data2=data[data.Poste_2 != '-']
                    data3=data[data.Poste_3 != '-']
                    c=st.sidebar.radio("select time",("Du 06H00 à 14H00","Du 14H00 à 22H00","Du 22H00 à 6H00"))
                    if c=="Du 06H00 à 14H00":
                        st._legacy_dataframe(data1[["Matricule_1","Poste_1"]].iloc[1:,])
                    elif c=="Du 14H00 à 22H00":
                        st._legacy_dataframe(data2[["Matricule_2","Poste_2"]].iloc[1:,])
                    elif c=="Du 22H00 à 6H00":
                        st._legacy_dataframe(data3[["Matricule_3","Poste_3"]].iloc[1:,])
                elif b == "Horaire particuliers":
                    d=st.sidebar.radio("Postes:",("Poste_1 ( Du 06H00 à 14H00 )","Poste_3 ( Du 14H00 à 22H00 )"))
                    if d=="Poste_1 ( Du 06H00 à 14H00 )":
                        data1=data.copy()
                        data1['hd1'] = data1['hd1'].fillna('-')
                        data1=data[data.hd1 != '-']
                        data2=data.copy()
                        data2['hf1'] = data1['hf1'].fillna('-')
                        data2=data[data.hf1 != '-']
                        x=st.sidebar.selectbox("Heure de début:",data1['hd1'].iloc[1:,].unique())
                        y=st.sidebar.selectbox("Heure de fin:",data2['hf1'].iloc[1:,].unique())
                        data1=data1[data1["hd1"].astype(str) == str(x) ]
                        data1=data1[data1["hf1"].astype(str) == str(y)]
                        st._legacy_dataframe(data1.drop(columns=["Poste_3","Poste_2","Matricule_3","Matricule_2","hd2","hf2"]).astype(str))
                        #

                    elif d=="Poste_3 ( Du 14H00 à 22H00 )":
                        data1=data.copy()
                        data1['hd2'] = data1['hd2'].fillna('-')
                        data1=data[data.hd2 != '-']
                        data2=data.copy()
                        data2['hf2'] = data1['hf2'].fillna('-')
                        data2=data[data.hf2 != '-']
                        x=st.sidebar.selectbox("Heure de début:",data1['hd2'].iloc[1:,].unique())
                        y=st.sidebar.selectbox("Heure de fin:",data2['hf2'].iloc[1:,].unique())
                        data1=data1[data1["hd2"] ==x]
                        data1=data1[data1["hf2"] ==y]
                        st._legacy_dataframe(data1.drop(columns=["Poste_1","Poste_2","Matricule_1","Matricule_2","hd1","hf1"]).astype(str))
                    # data1=data.copy()
                    # data22=data.copy()
                    # data1['hd1'] = data1['hd1'].fillna('-')
                    # data1=data[data.hd1 != '-']
                    # #st.dataframe(data1["hd1"].iloc[1:,])
                    # data1=data1.iloc[1:,]
                    # data2['hf1'] = data2['hf1'].fillna('-')
                    # data2=data[data.hf1 != '-']
                    # #st.dataframe(data2["hf1"].iloc[1:,])
                    # data2=data2.iloc[1:,]
                    # valuess = st.sidebar.slider(
                    #     'Select a range of values',
                    #     min(data1["hd1"].tolist()),max(data2["hf1"].tolist()),
                    #     value=[min(data1["hd1"].tolist()),max(data2["hf1"].tolist())]
                    #     #, (25.0, 75.0)
                    #     )
                    # st.write('Values:', valuess)

                    # data11=data.copy()
                    # data22=data.copy()
                    # data11['hd2'] = data11['hd2'].fillna('-')
                    # data11=data[data.hd2 != '-']
                    # #st.dataframe(data1["hd1"].iloc[1:,])
                    # data11=data11.iloc[1:,]
                    # data22['hf2'] = data22['hf2'].fillna('-')
                    # data22=data[data.hf2 != '-']
                    # #st.dataframe(data22["hf2"].iloc[1:,])
                    # data22=data22.iloc[1:,]
                    # valuess = st.sidebar.slider(
                    #     'Select a range of valuess',
                    #     max(data22["hf2"].tolist()),min(data11["hd2"].tolist()),
                    #     value=[min(data22["hf2"].tolist()),max(data11["hd2"].tolist())]
                    #     #, (25.0, 75.0)
                    #     )
                    # st.write('Values:', valuess)

                    # st.sidebar.slider(
                    #     'Select a range of valuesss',
                    #     min_value=10,
                    #     #max_value=0
                    #     )
                                    
    
    
            # else:
            #     container = st.sidebar.container()
            #     all = st.sidebar.checkbox("Toutes les familles")
                
            #     if all:
            #         Famille = container.multiselect("Famille:",
            #             ['ONDULEUSE', 'MMP'],['ONDULEUSE', 'MMP'])
            #     else:
            #         Famille =  container.multiselect("Famille:",
            #             ['ONDULEUSE', 'MMP'])


            #     container1 = st.sidebar.container()
            #     all1 = st.sidebar.checkbox("Toutes les affectation")
                
            #     if all1:
            #         Affec = container1.multiselect("Affectation:",
            #             ["Chef d'équipe", 'SF','MF', 'DF','AS', 'Chaudière','Déchets', 'MMP'],["Chef d'équipe", 'SF','MF', 'DF','AS', 'Chaudière','Déchets', 'MMP'])
            #     else:
            #         Affec =  container1.multiselect("Affectation:",
            #             ["Chef d'équipe", 'SF','MF', 'DF','AS', 'Chaudière','Déchets', 'MMP'])


            







                equipe1 = st.sidebar.multiselect(
                    "Noms des employés: ",
                    options=df["Poste_1"].iloc[1:,].unique(),
                )




                df_selection=data.query(
                    "Famille==@Famille & Affec==@Affec & Poste_1==@equipe1"
                    # & Mle==@id"
                )
                df_selection0=data.query(
                    "Famille==@Famille & Affec==@Affec"
                    # & Mle==@id"
                )
                with st.expander("Tableu complet"):

                    col11,col12,col13, = st.columns([1,10,1,])
                    with col11:
                        st.write('')
                    with col12:
                        st._legacy_dataframe(data.iloc[1:,].astype(str))
                        st._legacy_dataframe(df_selection)
                    with col13:
                        st.write('')

                with st.expander("Tableu complet0"):

                    col11,col12,col13, = st.columns([1,10,1,])
                    with col11:
                        st.write('')
                    with col12:
                        st.dataframe(df_selection0.astype(str))
                        st.sidebar.write("hello")
                    with col13:
                        st.write('')

                fig=px1.bar(
                    data,
                    x="Famille",
                    orientation="v",
                    title="<b>nombre des employés par affectations</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )
                
                st.plotly_chart(fig)     


                fig1=px1.bar(
                    data,
                    x="Affec",
                    orientation="v",
                    title="<b>nombre des employés par affectations</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )



                fig.update_xaxes(showgrid=False)

                st.plotly_chart(fig1)


                # left_column, right_column=st.columns(2)
                # left_column.plotly_chart(fig,use_container_width=True)
                # right_column.plotly_chart(fig1,use_container_width=True)



                st._legacy_table(df_selection)
        elif options=='Visualiser la Data':
            bf=pd.DataFrame()
            for c in data["Famille"].iloc[1:,].unique():
                fd=data[data["Famille"]==c]
                fd0 = fd[fd.Poste_1 != '-']
                fd1 = fd[fd.Poste_2 != '-']
                fd2 = fd[fd.Poste_3 != '-']

                # st.write(fd0.Poste_1)
                # st.write(fd1.Poste_2)
                # st.write(fd2.Poste_3)
                # fd123=fd0.append(fd1.append(fd2))
                # st.write(fd123)
                fd123=fd0.Poste_1.append(fd1.Poste_2.append(fd2.Poste_3))
                data_f=[[c,len(fd0.index)+len(fd1.index)+len(fd2.index)]]
                df0001=pd.concat([bf,pd.DataFrame(data_f, columns=['Famille', 'Count'])])
                bf=df0001
            bf=pd.DataFrame()
            for c in data["Affec"].iloc[1:,].unique():
                fd=data[data["Affec"]==c]
                fd0 = fd[fd.Poste_1 != '-']
                fd1 = fd[fd.Poste_2 != '-']
                fd2 = fd[fd.Poste_3 != '-']

                # st.write(fd0.Poste_1)
                # st.write(fd1.Poste_2)
                # st.write(fd2.Poste_3)
                # fd123=fd0.append(fd1.append(fd2))
                # st.write(fd123)
                fd123=fd0.Poste_1.append(fd1.Poste_2.append(fd2.Poste_3))
                data_f=[[c,len(fd0.index)+len(fd1.index)+len(fd2.index)]]
                df0002=pd.concat([bf,pd.DataFrame(data_f, columns=['Affec', 'Count'])])
                bf=df0002
            
            
            ch=st.sidebar.selectbox(
                'Options:',
                ('Tableaux  et Graphes',' Tableaux','Graphes'),
                #default=list(['Tableaux  et Graphes',' Tableaux','Graphes'])
            )
            if ch=='Graphes':
                

    
                df156 = data[data.Famille != '-']
                fig=px1.bar(
                    df0001,
                    x="Famille",
                    y="Count",
                    #orientation="v",
                    title="<b>nombre des employés par Famille</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    

                
                )


                df522=data[data.Affec != '-']
                fig1=px1.bar(
                    df0002,
                    x="Affec",
                    y="Count",
                    orientation="v",
                    title="<b>nombre des employés par affectations</b>",
                    color_discrete_sequence=["#0083B8"] * len(df522),
                    template="plotly_white"
                )


                fig4=px1.bar(
                    data.iloc[1:,],
                    x="hd1",
                    orientation="v",
                    title="<b>heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                fig3=px1.bar(
                    data,
                    x="hf1",
                    orientation="v",
                    title="<b>heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                df52=data[data.hd1 != '-']
                fig23=px1.bar(
                    data.iloc[1:,],
                    x=df52["hd1"],
                    y=df52["Poste_1"],
                    orientation="h",
                    title="<b>heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )

                df53=data[data.hf1 != '-']
                fig24=px1.bar(
                    data.iloc[1:,],
                    x=df53["hf1"],
                    y=df53["Poste_1"],
                    orientation="h",
                    title="<b>heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )

                df521=data[data.hd2 != '-']
                fig231=px1.bar(
                    data.iloc[1:,],
                    x=df521["hd2"],
                    y=df521["Poste_3"],
                    orientation="h",
                    title="<b>heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )

                df531=data[data.hf2 != '-']
                fig241=px1.bar(
                    data.iloc[1:,],
                    x=df531["hf2"],
                    y=df531["Poste_3"],
                    orientation="h",
                    title="<b>heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )
        


                # col111,col122,col133, = st.columns([1,10,1,])
                # with col111:
                #     st.write('')
                # with col122:
                #     st.plotly_chart(fig)
                # with col133:
                #     st.write('')

                # col11,col12,col13, = st.columns([1,10,1,])
                # with col11:
                #     st.write('')
                # with col12:
                #     st.plotly_chart(fig1)
                # with col13:
                #     st.write('')

                df1 = data[data.Matricule_1 != '-']
                df1["Poste_1"]="Poste_1"
                newdf1=(df1[['Poste_1']].iloc[1:,].copy())

                df1 = data[data.Matricule_2 != '-']
                df1["Poste_2"]="Poste_2"
                newdf2=(df1[['Poste_2']].iloc[1:,].copy())

                df1 = data[data.Matricule_3 != '-']
                df1["Poste_3"]="Poste_3"
                newdf3=(df1[['Poste_3']].iloc[1:,].copy())
                df1[['Poste_1']].append(df1[['Poste_1']])


                newdf4=newdf1.Poste_1.append(newdf2.Poste_2.append(newdf3.Poste_3))


                dff=newdf4.to_frame(name="Equipe")


                df1 = data[data.Poste_1 != '-']
                df1["Poste_1"]="Poste_1"
                newdf1=(df1.iloc[1:,].copy())

                df1 = data[data.Poste_2 != '-']
                df1["Poste_2"]="Poste_2"
                newdf2=(df1[['Poste_2']].iloc[1:,].copy())

                df1 = data[data.Poste_3 != '-']
                df1["Poste_3"]="Poste_3"
                newdf3=(df1[['Poste_3']].iloc[1:,].copy())
                df1[['Poste_1']].append(df1[['Poste_1']])


                newdf4=newdf1.Poste_1.append(newdf2.Poste_2.append(newdf3.Poste_3))
                
                data_f=[["Poste_1",len(newdf1.index)],["Poste_2",len(newdf2.index)],["Poste_3",len(newdf3.index)]]
                df0=pd.DataFrame(data_f, columns=['Equipe', 'len'])
                # st.write("Nombre des employés par equipes")
                fig20 = px1.bar(
                    df0,
                    x="Equipe",
                    y="len",
                    orientation="v",
                    title="<b>nombre des employés par Equipe</b>",
                    color_discrete_sequence=["#0083B8"] * len(dff),
                    template="plotly_white"
                    )
                fig201 = px1.pie(
                    dff,
                    names='Equipe',
                    #title='Pourcentage des employés par équipes',
                )
                #fig20.update_layout(margin=dict(t=0, b=0, l=0, r=0))
                
                
                


                left_column1, right_column1=st.columns(2)
                left_column1.plotly_chart(fig,use_container_width=False)
                right_column1.plotly_chart(fig1,use_container_width=False)

                col1112,col1223, = st.columns([1,1])

                with col1112:
                    st.plotly_chart(fig20)
                with col1223:
                    st.plotly_chart(fig201)






                # left_column12, right_column12=st.columns(2)
                # left_column12.plotly_chart(fig23,use_container_width=True)
                # right_column12.plotly_chart(fig24,use_container_width=True)

                # right_column121, left_column121=st.columns(2)
                # left_column121.plotly_chart(fig241,use_container_width=True)
                # right_column121.plotly_chart(fig231,use_container_width=True)


                fig51=px1.bar(
                    data.iloc[1:,],
                    x="hd1",
                    orientation="v",
                    title="<b>Nombre des employés pour heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                fig61=px1.bar(
                    data,
                    x="hf1",
                    orientation="v",
                    title="<b>Nombre des employés pour heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )
                
                


                fig5=px1.bar(
                    data.iloc[1:,],
                    x="hd2",
                    orientation="v",
                    title="<b>Nombre des employés pour heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                fig6=px1.bar(
                    data,
                    x="hf2",
                    orientation="v",
                    title="<b>Nombre des employés pour heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


            
            elif ch=='Tableaux  et Graphes':
                with st.expander("Tableu complet"):

                    col11,col12,col13, = st.columns([1,10,1,])
                    with col11:
                        st.write('')
                    with col12:
                        st.dataframe(data.iloc[1:,].astype(str))
                    with col13:
                        st.write('')
                # col201,col20,col30,col301 = st.columns([4,5,5,4])
                # with col20:
                #     st.write("Famille")
                #     st._legacy_dataframe(data["Famille"].iloc[1:,].unique())
                # with col30:
                #     st.write("Affectation")
                #     st._legacy_dataframe(data["Affec"].iloc[1:,].unique())
                col4,col5,col6,col7=st.columns(4)


                with col4:
                    st.write("Famille")
                    st._legacy_dataframe(data["Famille"].iloc[1:,].unique())
                with col5:
                    st.write("Affectation")
                    st._legacy_dataframe(data["Affec"].iloc[1:,].unique())
                with col6:
                    bf=pd.DataFrame()

                    st.write("Employés par Famille")
                    st._legacy_dataframe(df0001)

                with col7:
                    # for b in data["Famille"].iloc[1:,].unique():
                    #     data44=data[data["Famille"]==b]
                    bf=pd.DataFrame()

                    st.write("Employés par Affectation")
                    st._legacy_dataframe(df0002)               

                col1, col2,col3 = st.columns([1,1,1])
                with col1:
                    st.write("Du 06H00 à 14H00")
                    df1 = data[data.Matricule_1 != '-']
                    st._legacy_dataframe(df1[['Matricule_1','Poste_1']].iloc[1:,])
                with col2:
                    st.write("Du 14H00 à 22H00")
                    df1 = data[data.Matricule_2 != '-']
                    st._legacy_dataframe(df1[['Matricule_2','Poste_2']].iloc[1:,])
                with col3:
                    st.write("Du 22H00 à 06H00")
                    df1 = data[data.Matricule_3 != '-']
                    st._legacy_dataframe(df1[['Matricule_3','Poste_3']].iloc[1:,])
                    

                fig=px1.bar(
                    df0001,
                    x="Famille",
                    y="Count",
                    #y=data['Famille'].value_counts(),
                    orientation="v",
                    title="<b>nombre des employés par Famille</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    

                
                )

                df522=data[data.Affec != '-']
                fig1=px1.bar(
                    df0002,
                    x="Affec",
                    y="Count",
                    #y=data['Affec'].value_counts(),
                    orientation="v",
                    title="<b>nombre des employés par affectations</b>",
                    color_discrete_sequence=["#0083B8"] * len(df522),
                    template="plotly_white"
                )



                fig4=px1.bar(
                    data.iloc[1:,],
                    x="hd1",
                    orientation="v",
                    title="<b>heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                fig3=px1.bar(
                    data,
                    x="hf1",
                    orientation="v",
                    title="<b>heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                df52=data[data.hd1 != '-']
                fig23=px1.bar(
                    data.iloc[1:,],
                    x=df52["hd1"],
                    y=df52["Poste_1"],
                    orientation="h",
                    title="<b>heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )

                df53=data[data.hf1 != '-']
                fig24=px1.bar(
                    data.iloc[1:,],
                    x=df53["hf1"],
                    y=df53["Poste_1"],
                    orientation="h",
                    title="<b>heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )

                df521=data[data.hd2 != '-']
                fig231=px1.bar(
                    data.iloc[1:,],
                    x=df521["hd2"],
                    y=df521["Poste_3"],
                    orientation="h",
                    title="<b>heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )

                df531=data[data.hf2 != '-']
                fig241=px1.bar(
                    data.iloc[1:,],
                    x=df531["hf2"],
                    y=df531["Poste_3"],
                    orientation="h",
                    title="<b>heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white",
                    width=1000,
                )
        


                # col111,col122,col133, = st.columns([1,10,1,])
                # with col111:
                #     st.write('')
                # with col122:
                #     st.plotly_chart(fig)
                # with col133:
                #     st.write('')

                # col11,col12,col13, = st.columns([1,10,1,])
                # with col11:
                #     st.write('')
                # with col12:
                #     st.plotly_chart(fig1)
                # with col13:
                #     st.write('')

                df1 = data[data.Poste_1 != '-']
                df1["Poste_1"]="Poste_1"
                newdf1=(df1.iloc[1:,].copy())

                df1 = data[data.Poste_2 != '-']
                df1["Poste_2"]="Poste_2"
                newdf2=(df1[['Poste_2']].iloc[1:,].copy())

                df1 = data[data.Poste_3 != '-']
                df1["Poste_3"]="Poste_3"
                newdf3=(df1[['Poste_3']].iloc[1:,].copy())
                df1[['Poste_1']].append(df1[['Poste_1']])


                newdf4=newdf1.Poste_1.append(newdf2.Poste_2.append(newdf3.Poste_3))
                data_f=[["Poste_1",len(newdf1.index)],["Poste_2",len(newdf2.index)],["Poste_3",len(newdf3.index)]]
                df0=pd.DataFrame(data_f, columns=['Equipe', 'len'])
                # st.write("Nombre des employés par equipes")
                # st._legacy_dataframe(df0)


                dff=newdf4.to_frame(name="Equipe")


                fig20 = px1.bar(
                    df0,
                    x="Equipe", 
                    y="len", 
                    orientation="v",
                    title="<b>nombre des employés par Equipes</b>",
                    color_discrete_sequence=["#0083B8"] * len(dff),
                    template="plotly_white"
                    )
                fig201 = px1.pie(
                    dff,
                    names='Equipe',
                    title='Pourcentage des employés par équipes',
                )
                #fig20.update_layout(margin=dict(t=1, b=1, l=1, r=1))
                #st.plotly_chart(fig20)
                #fig.update_layout(margin=dict(t=0.1, b=0.1, l=0.1, r=0.1))
                
                


                left_column1, right_column1=st.columns(2)
                left_column1.plotly_chart(fig,use_container_width=False)
                right_column1.plotly_chart(fig1,use_container_width=False)



                col1112,col1223, = st.columns([1,1])

                with col1112:
                    st.plotly_chart(fig20)

                with col1223:
                    st.plotly_chart(fig201)






                # left_column12, right_column12=st.columns(2)
                # left_column12.plotly_chart(fig23,use_container_width=True)
                # right_column12.plotly_chart(fig24,use_container_width=True)

                # right_column121, left_column121=st.columns(2)
                # left_column121.plotly_chart(fig241,use_container_width=True)
                # right_column121.plotly_chart(fig231,use_container_width=True)


                fig51=px1.bar(
                    data.iloc[1:,],
                    x="hd1",
                    orientation="v",
                    title="<b>Nombre des employés pour heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                fig61=px1.bar(
                    data,
                    x="hf1",
                    orientation="v",
                    title="<b>Nombre des employés pour heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )
                
                


                fig5=px1.bar(
                    data.iloc[1:,],
                    x="hd2",
                    orientation="v",
                    title="<b>Nombre des employés pour heure debut</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


                fig6=px1.bar(
                    data,
                    x="hf2",
                    orientation="v",
                    title="<b>Nombre des employés pour heure fin</b>",
                    color_discrete_sequence=["#0083B8"] * len(data),
                    template="plotly_white"
                )


            else:

                with st.expander("Tableu complet"):

                    col11,col12,col13, = st.columns([1,10,1,])
                    with col11:
                            st.write('')
                    with col12:
                            st.dataframe(data.iloc[1:,].astype(str))
                    with col13:
                            st.write('')
                    # col201,col20,col30,col301 = st.columns([4,5,5,4])
                    # with col20:
                    #     st.write("Famille")
                    #     st._legacy_dataframe(data["Famille"].iloc[1:,].unique())
                    # with col30:
                    #     st.write("Affectation")
                    #     st._legacy_dataframe(data["Affec"].iloc[1:,].unique())
                col4,col5,col6,col7=st.columns(4)


                with col4:
                    st.write("Famille")
                    st._legacy_dataframe(data["Famille"].iloc[1:,].unique())
                with col5:
                    st.write("Affectation")
                    st._legacy_dataframe(data["Affec"].iloc[1:,].unique())
                with col6:
                    st.write("Occurrence par famille")
                    st._legacy_dataframe(data["Famille"].iloc[1:,].value_counts())
                with col7:
                    df1 = data[data.Affec != '-']
                    st.write("Occurrence par Affectation")
                    st._legacy_dataframe(df1["Affec"].value_counts())               

                col1, col2,col3 = st.columns([1,1,1])
                with col1:
                    st.write("Du 06H00 à 14H00")
                    df1 = data[data.Matricule_1 != '-']
                    st._legacy_dataframe(df1[['Matricule_1','Poste_1']].iloc[1:,])
                with col2:
                    st.write("Du 14H00 à 22H00")
                    df1 = data[data.Matricule_2 != '-']
                    st._legacy_dataframe(df1[['Matricule_2','Poste_2']].iloc[1:,])
                with col3:
                    st.write("Du 22H00 à 06H00")
                    df1 = data[data.Matricule_3 != '-']
                    st._legacy_dataframe(df1[['Matricule_3','Poste_3']].iloc[1:,])

                df1 = data[data.Poste_1 != '-']
                df1["Poste_1"]="Poste_1"
                newdf1=(df1.iloc[1:,].copy())

                df1 = data[data.Poste_2 != '-']
                df1["Poste_2"]="Poste_2"
                newdf2=(df1[['Poste_2']].iloc[1:,].copy())

                df1 = data[data.Poste_3 != '-']
                df1["Poste_3"]="Poste_3"
                newdf3=(df1[['Poste_3']].iloc[1:,].copy())
                df1[['Poste_1']].append(df1[['Poste_1']])


                newdf4=newdf1.Poste_1.append(newdf2.Poste_2.append(newdf3.Poste_3))
                
                data_f=[["Poste_1",len(newdf1.index)],["Poste_2",len(newdf2.index)],["Poste_3",len(newdf3.index)]]
                df0=pd.DataFrame(data_f, columns=['Equipe', 'len'])
                # st.write("Nombre des employés par equipes")
                # st._legacy_dataframe(df0)
    elif options=='Rapport':
        dh=st.sidebar.selectbox("Data:",["Globale","Répartie"])
        if dh=="Répartie":
        
        


        
            # st.title("Rapport Page")
            li0=list(data["Famille"].iloc[1:,].unique())

            

            for j in range(len(li0)):
                
                data0=data[data["Famille"]==li0[j]]
                data_fa=data0[data0["Poste_1"]!='-']
                data_fb=data0[data0["Poste_2"]!='-']
                data_fc=data0[data0["Poste_3"]!='-']


                # data11=data1[data1.Poste_1!='-']
                # data12=data1[data1.Poste_2!='-']
                # data13=data1[data1.Poste_3!='-']

                # data14=data11.Poste_1.append(data12.Poste_2.append(data13.Poste_3)).to_list()
                b=0
                for i in range(len(datavvv["NOM ET PRENOM"])):
                    
                        # if datavvv["Famille"][i]==li0[j]:
                        #     st.write(datavvv["NOM ET PRENOM"][i])
                            if datavvv["Famille"][i]==li0[j]:
                                b=b+1


                st.subheader(li0[j]+" "+"["+" "+str(len(data_fa.Poste_1.append(data_fb.Poste_2.append(data_fc.Poste_3))))+" "+"]"+" / "+" [ "+str(b)+" ABS"+" ] ")
                data00=data[data["Famille"]==li0[j]]
                li=list(data00["Affec"].unique())
                l=li
                a=len(l)//2
                b=l[a:]
                c=l[:a]
                # a=len(l)//2
                
                # st.write
                # t=[]
                # for i in range(len(l)-4):
                #     t=t+[l[i*3:(i*3)+3]]

                # st.write(t)

                st.write("Affectation")
                col1,col2=st.columns(2)
                
                
                
                with col1:
                    
                    for i in range(len(b)):
                        data0=data[data["Famille"]==li0[j]]
                        data1=data0[data0["Affec"]==b[i]]

                        data11=data1[data1.Poste_1!='-']
                        data12=data1[data1.Poste_2!='-']
                        data13=data1[data1.Poste_3!='-']
            
                        data14=data11.Poste_1.append(data12.Poste_2.append(data13.Poste_3)).to_list()
                        data106=data[["Poste_1","hd1","hf1"]]
                        #st.write(data106)
                        with st.expander(b[i]+" "+"("+" "+str(len(data14))+" "+")"):
                            
                            st.write("")
                            for i in range(len(data14)):
                                    # st.button(data14[i])
                                    
                                    if st.button(data14[i]):
                                        if data14[i] in data11["Poste_1"].to_list():
                                            data18=data11[data11.Poste_1==data14[i]]
                                            # st.write("Id:")
                                            data180=data18["Matricule_1"].to_list()
                                            st.write("-"+"     "+"Id: "+data180[0])
                                            # st.write("Heure de début:")
                                            data18=data18.replace('-','none',regex=True)
                                            data189=data18["hd1"].to_list()
                                            for u in data189:
                                                # st.write(u)
                                                if u=='none':
                                                    # st.write(1)
                                                    if data14[i] in data11["Poste_1"].to_list():
                                                        data189[0]="06h"
                                                    elif data14[i] in data12["Poste_2"].to_list():
                                                        data189[0]="14h"
                                                    elif data14[i] in data13["Poste_3"].to_list():
                                                        data189[0]="22h"

                                            
                                            st.write("-"+"     "+"Heure de début: "+data189[0])
                                            # st.write("Heure de fin:")
                                            data18=data18.replace('-','none',regex=True)
                                            data1899=data18["hf1"].to_list()
                                            for u in data1899:
                                                if u=='none':
                                                    # st.write(1)
                                                    if data14[i] in data11["Poste_1"].to_list():
                                                        data1899[0]="14h"
                                                    elif data14[i] in data12["Poste_2"].to_list():
                                                        data1899[0]="22h"
                                                    elif data14[i] in data13["Poste_3"].to_list():
                                                        data1899[0]="06h"
                                            st.write("-"+"     "+"Heure de fin: "+data1899[0])
                                            st.write(" ")
                                        elif data14[i] in data11["Poste_2"].to_list():
                                            data18=data11[data11.Poste_2==data14[i]]

                                            # st.write("Id:")
                                            data180=data18["Matricule_2"].to_list()
                                            st.write("-"+"     "+"Id: "+data180[0])
                                            st.write(" ")
                                        elif data14[i] in data11["Poste_3"].to_list():
                                            data18=data11[data11.Poste_3==data14[i]]

                                            # st.write("Id:")
                                            data180=data18["Matricule_3"].to_list()
                                            st.write("-"+"     "+"Id :"+data180[0])
                                            # st.write("Heure de début:")
                                            data18=data18.replace('-','none',regex=True)
                                            data189=data18["hd2"].to_list()
                                            
                                            #if data189[0]=='none':
                                            for u in data189:
                                                if u=='none':
                                                    # st.write(1)
                                                    if data14[i] in data11["Poste_1"].to_list():
                                                        data189[0]="06h"
                                                    elif data14[i] in data12["Poste_2"].to_list():
                                                        data189[0]="14h"
                                                    elif data14[i] in data13["Poste_3"].to_list():
                                                        data189[0]="22h"
                                            st.write("-"+"     "+"Heure de début: "+data189[0])
                                            # st.write("Heure de fin:")
                                            data18=data18.replace('-','none',regex=True)
                                            data1899=data18["hf2"].to_list()
                                            for uu in data1899:
                                                if u=='none':
                                                    # st.write(1)
                                                    if data14[i] in data11["Poste_1"].to_list():
                                                        data1899[0]="14h"
                                                    elif data14[i] in data12["Poste_2"].to_list():
                                                        data1899[0]="22h"
                                                    elif data14[i] in data13["Poste_3"].to_list():
                                                        data1899[0]="06h"
                                            st.write("-"+"     "+"Heure de fin :"+data1899[0])
                                            st.write(" ")


                # li=list(data00["Affec"].unique())
                # l=li
                # a=len(l)//2
                # b=l[a:]
                # c=l[:a]
                with col2:

                    
                    for i in range(len(c)):
                        data00=data[data["Famille"]==li0[j]]
                        data10=data00[data00["Affec"]==c[i]]

                        data110=data10[data10.Poste_1!='-']
                        data120=data10[data10.Poste_2!='-']
                        data130=data10[data10.Poste_3!='-']
            
                        data140=data110.Poste_1.append(data120.Poste_2.append(data130.Poste_3)).to_list()
                        with st.expander(c[i]+" "+"("+" "+str(len(data140))+" "+")"):
                            
                            st.write("")
                            for i in range(len(data140)):
                                if st.button(data140[i]):
                                    if data140[i] in data110["Poste_1"].to_list():
                                        data18=data110[data110.Poste_1==data140[i]]
                                        # st.write("Id:")
                                        data180=data18["Matricule_1"].to_list()
                                        st.write("-"+"     "+"Id :"+data180[0])
                                        # st.write("Heure de début:")
                                        data18=data18.replace('-','none',regex=True)
                                        data189=data18["hd1"].to_list()
                                        for u in data189:
                                            if u=='none':
                                                # st.write(1)
                                                if data14[i] in data11["Poste_1"].to_list():
                                                    data189[0]="06h"
                                                elif data14[i] in data12["Poste_2"].to_list():
                                                    data189[0]="14h"
                                                elif data14[i] in data13["Poste_3"].to_list():
                                                    data189[0]="22h"
                                        st.write("-"+"     "+"Heure de début: "+data189[0])
                                        # st.write("Heure de fin:")
                                        data18=data18.replace('-','none',regex=True)
                                        data1899=data18["hf1"].to_list()
                                        for u in data1899:
                                            if u=='none':
                                                # st.write(1)
                                                if data14[i] in data11["Poste_1"].to_list():
                                                    data1899[0]="14h"
                                                elif data14[i] in data12["Poste_2"].to_list():
                                                    data1899[0]="22h"
                                                elif data14[i] in data13["Poste_3"].to_list():
                                                    data1899[0]="06h"
                                        st.write("-"+"     "+"Heure de fin: "+data1899[0])
                                        st.write(" ")
                                        
                                    elif data140[i] in data110["Poste_2"].to_list():
                                        data18=data110[data110.Poste_2==data140[i]]

                                        st.write("Id:")
                                        data180=data18["Matricule_2"].to_list()
                                        st.write("-"+"     "+data180[0])
                                        st.write(" ")
                                    elif data140[i] in data110["Poste_3"].to_list():
                                        data18=data110[data110.Poste_3==data140[i]]

                                        # st.write("Id:")
                                        data180=data18["Matricule_3"].to_list()
                                        st.write("-"+"     "+"Id :"+data180[0])
                                        # st.write("Heure de début:")
                                        data18=data18.replace('-','none',regex=True)
                                        data189=data18["hd2"].to_list()
                                        for u in data189:
                                            if u=='none':
                                                # st.write(1)
                                                if data14[i] in data11["Poste_1"].to_list():
                                                    data189[0]="06h"
                                                elif data14[i] in data12["Poste_2"].to_list():
                                                    data189[0]="14h"
                                                elif data14[i] in data13["Poste_3"].to_list():
                                                    data189[0]="22h"
                                        st.write("-"+"     "+"Heure de début: "+data189[0])
                                        #st.write("Heure de fin:")
                                        data18=data18.replace('-','none',regex=True)
                                        data1899=data18["hf2"].to_list()
                                        for u in data1899:
                                            if u=='none':
                                                # st.write(1)
                                                if data14[i] in data11["Poste_1"].to_list():
                                                    data1899[0]="14h"
                                                elif data14[i] in data12["Poste_2"].to_list():
                                                    data1899[0]="22h"
                                                elif data14[i] in data13["Poste_3"].to_list():
                                                    data1899[0]="06h"
                                        st.write("-"+"     "+"Heure de fin: "+data1899[0])
                                        st.write(" ")



                li=list(data00["Affec"].unique())
                l=li
                a=len(l)//2
                b=l[a:]
                c=l[:a]

                st.write("Poste")                    
                col3,col4,col5=st.columns(3)
                
                with col3:
                    data11=data0[data0.Poste_1!='-']
                    data11=data11.Poste_1.to_list()
                    with st.expander("Du 06H00 à 14H00"+" "+"["+" "+str(len(data11))+" "+"]"):
                        # data1=data0[data0["Affec"]=="chef déquipe"]

                        st.write("")
                        for i in range(len(data11)):
                            st.write("-"+" "+data11[i])
                with col4:
                    data11=data0[data0.Poste_2!='-']
                    data11=data11.Poste_2.to_list()
                    with st.expander("Du 14H00 à 22H00"+" "+"["+" "+str(len(data11))+" "+"]"):
                        
                        # data1=data0[data0["Affec"]=="chef déquipe"]

                        st.write("")
                        for i in range(len(data11)):
                            st.write("-"+" "+data11[i])
                        
                with col5:
                    data11=data0[data0.Poste_3!='-']
                    data11=data11.Poste_3.to_list()
                    with st.expander("Du 22H00 à 06H00"+" "+"["+" "+str(len(data11))+" "+"]"):
                        # data1=data0[data0["Affec"]=="chef déquipe"]

                        st.write("")
                        for i in range(len(data11)):
                            st.write("-"+" "+data11[i])

                st.write("Absence")
                #for j in range(len(li0)):*
                a=0
                for i in range(len(datavvv["NOM ET PRENOM"])):
                    
                        # if datavvv["Famille"][i]==li0[j]:
                        #     st.write(datavvv["NOM ET PRENOM"][i])
                            if datavvv["Famille"][i]==li0[j]:
                                a=a+1

                with st.expander("Les Employés absents"+" "+"["+" "+str(a)+" "+"]"):
                    st.write(" ")

                    for i in range(len(datavvv["NOM ET PRENOM"])):
                        
                            # if datavvv["Famille"][i]==li0[j]:
                            #     st.write(datavvv["NOM ET PRENOM"][i])
                                if datavvv["Famille"][i]==li0[j]:
                                    
                                    if st.button(datavvv["NOM ET PRENOM"][i]):
                                        st.write(datavvv["MOTIF"][i])
                

                                    
        else:
            data2080=data[data["hd1"]!="-"]
            data2081=data[data["hf1"]!='-']
            data2082=data[data["hd2"]!='-']
            data2083=data[data["hf2"]!='-']
            #dg=pd.concat([data2080["hd1"].unique(),data2081["hf1"].unique()],axis=1)
            wc=data2080["hd1"].to_list()
            # st.write(wc)
           
            wd=data2081["hf1"].to_list()
            # st.write(wd)
            # l=[]
            # d01=[]
            # d02=[]
            # for i in range(len(wc)):
            #     d01=d01+[wc[i]]
            #     d02=d02+[wd[i]]
            #     l=l+[["Du "+str(wc[i])+"H à "+str(wd[i])+"H"]]
            # st.write(l)
            # # st.write(d01)
            # # st.write(d02)
            # # l1=list(dict.fromkeys(l[0]))
            # # st.write(l)

            wc0=data2082["hd2"].to_list()
            wd0=data2083["hf2"].to_list()
            r0=wc+wc0
            q0=wd+wd0
            # st.write(r0)
            # st.write(q0)
            l=[]
            for aa0 in r0:
                for bb0 in q0:
                    l=l+[["Du "+str(aa0)+"H à "+str(bb0)+"H"]]
            # st.write(l)


            # l00=[]
            # d1=[]
            # d2=[]
            # for i in range(len(wc0)):
            #     d1=d1+[wc0[i]]
            #     d2=d2+[wd0[i]]
                
            #     l00=l00+[["Du "+str(wc0[i])+"H à "+str(wd0[i])+"H"]]
            # hd=d1+d01
            # hf=d2+d02
            hdf=[]
            # hf0=[]
            for x in l:
                if x not in hdf:
                    hdf.append(x)
            # st.write(hdf)
            # for y in hf:
            #     if y not in hf0:
            #         hf0.append(y)
            # st.write(hf0)


            # ll0=list(dict.fromkeys(l00[0]))
            # st.write(l00)
            # ll001=l+l00
            # st.write(ll001)
            # lt=[]
            # for t in ll001:
            #     if t not in lt:
            #         lt.append(t)
            # uu=lt
            # st.write(uu)
            # st.write(str(uu))
            ff=[]
            data1010=data[data["hd1"]!="-"]
            data1011=data[data["hd2"]!="-"]
            data1012=data[data["hf1"]!="-"]
            data1013=data[data["hf2"]!="-"]
            lh1a=list(data1010["hd1"])
            lh1b=list(data1011["hd2"])
            lh1=lh1a+lh1b
            # st.write(lh1)
            lh2a=list(data1012["hf1"])
            lh2b=list(data1013["hf2"])
            lh2=lh2a+lh2b
            # st.write(lh2)
            lkj=[]
            for i in range(len(lh1)):
                    lkj=lkj+[["Du "+str(lh1[i])+"H à "+str(lh2[i])+"H"]]
            # st.write(lkj)

            for i in range(len(hdf)):
                if hdf[i] in lkj:
                    ff.append(hdf[i][0])
            # st.write(ff)

            # for i in range(len(ll001)-1):
            #     if ll001[i]!=ll001[i+1]:
            #         ltt=l+ll001[i]
            # st.write(lt)
            
            ll001=[[1, 2], [4], [5, 6, 2], [1, 2], [3], [4]]
            q=[]
            for j in ll001:
                if j not in q:
                    q.append(j)
            lif=q
            

            # lif=list(set(ll001))
            # st.write(lif)


                 


            
            
            #dg=pd.concat([wc,wd],axis=1)
            #st.write(dg)
            q=st.sidebar.radio("Global:",
            ('Rapport Global ( tous les horaires )','Du 06H00 à 14H00','Du 14H00 à 22H00','Du 22H00 à 06H00',"Plus d'horaires"))




            # for i in range(len(lif)):

  
            # st.write(str(list(data1163["Poste_3"])))



            
            
            li0=list(data["Famille"].iloc[1:,].unique())
            li=list(data["Famille"].iloc[1:,].unique())
            l=li
            a=len(l)//2
            b=l[a:]
            c=l[:a]
            if q=="Rapport Global ( tous les horaires )":
    

                x=0
                for i in range(len(b)):
                    data1=data[data["Famille"]==b[i]]

                    data11=data1[data1.Poste_1!='-']
                    data12=data1[data1.Poste_2!='-']
                    data13=data1[data1.Poste_3!='-']
        
                    data14=data11.Poste_1.append(data12.Poste_2.append(data13.Poste_3)).to_list()
                    
                    x=x+len(data14)
                y=0
                for i in range(len(c)):
                    data10=data[data["Famille"]==c[i]]

                    data110=data10[data10.Poste_1!='-']
                    data120=data10[data10.Poste_2!='-']
                    data130=data10[data10.Poste_3!='-']
        
                    data140=data110.Poste_1.append(data120.Poste_2.append(data130.Poste_3)).to_list()
                    y=y+len(data140)
                    
                    

                bf=pd.DataFrame()
                for cc in data["Famille"].iloc[1:,].unique():
                    fd=data[data["Famille"]==cc]
                    fd0 = fd[fd.Poste_1 != '-']
                    fd1 = fd[fd.Poste_2 != '-']
                    fd2 = fd[fd.Poste_3 != '-']

                    # st.write(fd0.Poste_1)
                    # st.write(fd1.Poste_2)
                    # st.write(fd2.Poste_3)
                    # fd123=fd0.append(fd1.append(fd2))
                    # st.write(fd123)
                    fd123=fd0.Poste_1.append(fd1.Poste_2.append(fd2.Poste_3))
                    data_f=[[cc,len(fd0.index)+len(fd1.index)+len(fd2.index)]]
                    df0001=pd.concat([bf,pd.DataFrame(data_f, columns=['Famille', 'Count'])])
                    bf=df0001
                bf=pd.DataFrame()
                for cc in data["Affec"].iloc[1:,].unique():
                    fd=data[data["Affec"]==cc]
                    fd0 = fd[fd.Poste_1 != '-']
                    fd1 = fd[fd.Poste_2 != '-']
                    fd2 = fd[fd.Poste_3 != '-']

                    # st.write(fd0.Poste_1)
                    # st.write(fd1.Poste_2)
                    # st.write(fd2.Poste_3)
                    # fd123=fd0.append(fd1.append(fd2))
                    # st.write(fd123)
                    fd123=fd0.Poste_1.append(fd1.Poste_2.append(fd2.Poste_3))
                    data_f=[[cc,len(fd0.index)+len(fd1.index)+len(fd2.index)]]
                    df0002=pd.concat([bf,pd.DataFrame(data_f, columns=['Affec', 'Count'])])
                    bf=df0002
                    df00021=df0002[df0002["Affec"]!="-"]
                    df00011=df0001[df0001["Famille"]!="-"]

                fig=px1.bar(
                    df00011,
                    x="Famille",
                    y="Count",
                    #orientation="v",
                    title="<b>nombre des employés par Famille</b>",
                    color_discrete_sequence=["#0083B8"] * len(df00011),
                    template="plotly_white")
                fig1=px1.bar(
                    df00021,
                    x="Affec",
                    y="Count",
                    orientation="v",
                    title="<b>nombre des employés par affectations</b>",
                    color_discrete_sequence=["#0083B8"] * len(df00021),
                    template="plotly_white"
                )
                col1547,col1548=st.columns(2)
                    
                    
                with col1547:
                    with st.expander("Nombre des EMP / Famille"):
                        st.plotly_chart(fig)
                with col1548:
                    with st.expander("Nombre des EMP / Affectation"):
                        st.plotly_chart(fig1)
                        


                


                df1 = data[data.Matricule_1 != '-']
                df1["Poste_1"]="Poste_1"
                newdf1=(df1[['Poste_1']].iloc[1:,].copy())

                df1 = data[data.Matricule_2 != '-']
                df1["Poste_2"]="Poste_2"
                newdf2=(df1[['Poste_2']].iloc[1:,].copy())

                df1 = data[data.Matricule_3 != '-']
                df1["Poste_3"]="Poste_3"
                newdf3=(df1[['Poste_3']].iloc[1:,].copy())
                df1[['Poste_1']].append(df1[['Poste_1']])


                newdf4=newdf1.Poste_1.append(newdf2.Poste_2.append(newdf3.Poste_3))


                dff=newdf4.to_frame(name="Equipe")


                df1 = data[data.Poste_1 != '-']
                df1["Poste_1"]="Poste_1"
                newdf1=(df1.iloc[1:,].copy())

                df1 = data[data.Poste_2 != '-']
                df1["Poste_2"]="Poste_2"
                newdf2=(df1[['Poste_2']].iloc[1:,].copy())

                df1 = data[data.Poste_3 != '-']
                df1["Poste_3"]="Poste_3"
                newdf3=(df1[['Poste_3']].iloc[1:,].copy())
                df1[['Poste_1']].append(df1[['Poste_1']])


                newdf4=newdf1.Poste_1.append(newdf2.Poste_2.append(newdf3.Poste_3))
                
                data_f=[["Poste_1",len(newdf1.index)],["Poste_2",len(newdf2.index)],["Poste_3",len(newdf3.index)]]
                df0=pd.DataFrame(data_f, columns=['Equipe', 'len'])    

                fig20 = px1.bar(
                    df0,
                    x="Equipe",
                    y="len",
                    orientation="v",
                    title="<b>nombre des employés par Equipe</b>",
                    color_discrete_sequence=["#0083B8"] * len(dff),
                    template="plotly_white"
                    )
                fig201 = px1.pie(
                    dff,
                    title="<b>pourcentage des employés par Equipe</b>",
                    names='Equipe')

                col111200,col122301=st.columns(2)
                with col111200:
                    with st.expander("nombre des employés par Equipe"):
                        st.plotly_chart(fig20)
                with col122301:
                    with st.expander("pourcentage des employés par Equipe"):
                        st.plotly_chart(fig201)



                st.subheader("Famille"" "+"["+" "+str(x+y)+" "+"]"+" / "+" [ "+str(len(datavvv["NOM ET PRENOM"]))+" ABS"+" ] ")
                

                    




                col1,col2=st.columns(2)
                
                
                
                with col1:
                    k=0
                    for i in range(len(b)):
                        data1=data[data["Famille"]==b[i]]

                        #data11=data1[data1.Affec!='']
                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data101.Poste_1.append(data102.Poste_2.append(data103.Poste_3))
                        

                        with st.expander(b[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            st.write('')
                            


                            for t in range(len(data1489)):
                                k=k+1
                            
                            
                                if data1489[t]!=[]:
                                    k=k+1

                                    

                                
                                    data26=data[data["Famille"]==b[i]]
                                    k=k+1
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    k=k+1
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2771.Poste_1.append(data2772.Poste_2.append(data2773.Poste_3)).unique())
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        k=k+1
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        k=k+1
                                        for g in range(len(li0)):
                                            k=k+1
                                            #st.write(li0[g])
                                        
                                            data26=data[data["Famille"]==b[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2771.Poste_1.append(data2772.Poste_2.append(data2773.Poste_3)).unique())
                                            k=k+1
                                        k=k+1
                                        for p in range(len(fin)):

                                            k=k+1
                                            if fin[p]in data2772["Poste_2"].to_list():
                                                k=k+1
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():

                                                k=k+1
                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():

                                                k=k+1
                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    
                                                    
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                        k=k+1

                                    k=k+1


                                        

                                        

 

                with col2:

                    
                    #k=0
                    for i in range(len(c)):
                        data1=data[data["Famille"]==c[i]]

                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data101.Poste_1.append(data102.Poste_2.append(data103.Poste_3))
                        

                        with st.expander(c[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            st.write('')
                            


                            for t in range(len(data1489)):
                            
                            
                                if data1489[t]!=[]:

                                    

                        
                                    data26=data[data["Famille"]==c[i]]
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2771.Poste_1.append(data2772.Poste_2.append(data2773.Poste_3)).unique())                                    
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        for g in range(len(li0)):
                                        
                                            data26=data[data["Famille"]==c[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2771.Poste_1.append(data2772.Poste_2.append(data2773.Poste_3)).unique())
                                        for p in range(len(fin)):

                                            if fin[p]in data2772["Poste_2"].to_list():
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():

                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():

                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                    k=k+1

                                    

            

                
                st.write("Poste")                    
                col3,col4,col5=st.columns(3)
                data=data.iloc[1:,]
                    
                with col3:
                    data11=data[data.Poste_1!='-']
                    data11=data11.Poste_1.to_list()
                    with st.expander("Du 06H00 à 14H00"+" "+"["+" "+str(len(data11))+" "+"]"):
                        # data1=data0[data0["Affec"]=="chef déquipe"]

                        st.write("")
                        for i in range(len(data11)):
                            st.write("-"+" "+data11[i])
                with col4:
                    data11=data[data.Poste_2!='-']
                    data11=data11.Poste_2.to_list()
                    with st.expander("Du 14H00 à 22H00"+" "+"["+" "+str(len(data11))+" "+"]"):
                        
                        # data1=data0[data0["Affec"]=="chef déquipe"]

                        st.write("")
                        for i in range(len(data11)):
                            st.write("-"+" "+data11[i])
                        
                with col5:
                    data11=data[data.Poste_3!='-']
                    data11=data11.Poste_3.to_list()
                    with st.expander("Du 22H00 à 06H00"+" "+"["+" "+str(len(data11))+" "+"]"):
                        # data1=data0[data0["Affec"]=="chef déquipe"]

                        st.write("")
                        for i in range(len(data11)):
                            st.write("-"+" "+data11[i])


                st.write("Absence")

                with st.expander("Absences"+" "+"[ "+str(len(datavvv["NOM ET PRENOM"]))+" ]"):
                    for i in range(len(datavvv["NOM ET PRENOM"])):
                        data33389=datavvv[datavvv["NOM ET PRENOM"]==datavvv["NOM ET PRENOM"][i]]
                        
                        fff=data33389["MOTIF"].to_list()
                        dff0=data33389["DATE DEPART"].to_list()
                        dff1=data33389["DATE REPRISE"].to_list()
                        #st.write(str(datavvv["NOM ET PRENOM"][i])+"[ MOTIF= "+fff[0]+" ]")
                        if dff0[0]=="" and dff1[0]!="" :
                            dff0[0]="None"
                            # st.write(str(datavvv["NOM ET PRENOM"][i]))
                            # st.write("-"+"   "+"MOTIF= "+fff[0])
                            # st.write("-"+"   "+"DATE DEBUT= "+dff0[0])
                            # st.write("-"+"   "+"DATE REPRISE= "+dff1[0])
                            # st.write(" ")
                            # st.write(" ")
                            st.write(str(datavvv["NOM ET PRENOM"][i])+" : "+fff[0]+" [ "+dff0[0]+" - "+dff1[0]+" ] ")

                        elif dff1[0]=="" and dff0[0]!="":
                            dff1[0]="None"
                            # st.write(str(datavvv["NOM ET PRENOM"][i])+"-"+" "+"[ MOTIF= "+fff[0]+" ]"+"    "+"d1= "+dff0[0]+" "+"d2= "+dff1[0])
                            # st.write("-"+"   "+"hi")
                            # st.write(str(datavvv["NOM ET PRENOM"][i]))
                            # st.write("-"+"   "+"MOTIF= "+fff[0])
                            # st.write("-"+"   "+"DATE DEBUT= "+dff0[0])
                            # st.write("-"+"   "+"DATE REPRISE= "+dff1[0])
                            # st.write(" ")
                            # st.write(" ")
                            st.write(str(datavvv["NOM ET PRENOM"][i])+" : "+fff[0]+" [ "+dff0[0]+" - "+dff1[0]+" ] ")
                        elif dff0[0]=="" and dff1[0]=="":
                            dff0[0]="None"
                            dff1[0]="None"
                            # st.write(str(datavvv["NOM ET PRENOM"][i])+"-"+" "+"[ MOTIF= "+fff[0]+" ]"+"    "+"d1= "+dff0[0]+" "+"d2= "+dff1[0])
                            # st.write("-"+"   "+"hi")
                            # st.write(str(datavvv["NOM ET PRENOM"][i]))
                            # st.write("-"+"   "+"MOTIF= "+fff[0])
                            # st.write("-"+"   "+"DATE DEBUT= "+dff0[0])
                            # st.write("-"+"   "+"DATE REPRISE= "+dff1[0])   
                            # st.write(" ")  
                            # st.write(" ")
                            st.write(str(datavvv["NOM ET PRENOM"][i])+" : "+fff[0]+" [ "+dff0[0]+" - "+dff1[0]+" ] ")                   
                        
                        else:
                            # st.write("-"+"   "+"hi")
                            st.write(str(datavvv["NOM ET PRENOM"][i])+" : "+fff[0]+" [ "+dff0[0]+" --------> "+dff1[0]+" ] ")
                            #st.write(str(datavvv["NOM ET PRENOM"][i]))
                            # st.write("-"+"   "+"MOTIF= "+fff[0])
                            # st.write("-"+"   "+"DATE DEBUT= "+dff0[0])
                            # st.write("-"+"   "+"DATE REPRISE= "+dff1[0])
                            # st.write(" ")
                            # st.write(" ")
                    st.write(" ")
                    st.write(" ")


            elif q=="Du 06H00 à 14H00":
                x=0
                for i in range(len(b)):
                    data1=data[data["Famille"]==b[i]]

                    data11=data1[data1.Poste_1!='-']
                    data12=data1[data1.Poste_2!='-']
                    data13=data1[data1.Poste_3!='-']
        
                    data14=data11.Poste_1.to_list()
                    
                    x=x+len(data14)
                y=0
                for i in range(len(c)):
                    data10=data[data["Famille"]==c[i]]

                    data110=data10[data10.Poste_1!='-']
                    data120=data10[data10.Poste_2!='-']
                    data130=data10[data10.Poste_3!='-']
        
                    data140=data110.Poste_1.to_list()
                    y=y+len(data140)
                    
                    

                

                st.subheader("Famille"" "+"["+" "+str(x+y)+" "+"]")
                    




                col1,col2=st.columns(2)
                
                
                
                with col1:
                    k=0
                    for i in range(len(b)):
                        k=k+1
                        data1=data[data["Famille"]==b[i]]

                        #data11=data1[data1.Affec!='']
                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data101.Poste_1
                        

                        with st.expander(b[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            st.write('')
                            


                            for t in range(len(data1489)):
                                k=k+1
                            
                            
                                if data1489[t]!=[]:
                                    k=k+1

                                    

                                
                                    data26=data[data["Famille"]==b[i]]
                                    k=k+1
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2771.Poste_1)
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        k=k+1
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        for g in range(len(li0)):
                                            k=k+1
                                            #st.write(li0[g])
                                        
                                            data26=data[data["Famille"]==b[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2771.Poste_1)
                                        for p in range(len(fin)):
                                            k=k+1

                                            if fin[p]in data2772["Poste_2"].to_list():
                                                k=k+1
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():
                                                k=k+1

                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():
                                                k=k+1

                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            k=k+1
                                        k=k+1
                                    k=k+1


                                        

                                        

 

                with col2:

                    
                    #k=0
                    for i in range(len(c)):
                        data1=data[data["Famille"]==c[i]]

                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data101.Poste_1
                        

                        with st.expander(c[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            st.write('')
                            


                            for t in range(len(data1489)):
                            
                            
                                if data1489[t]!=[]:

                                    

                        
                                    data26=data[data["Famille"]==c[i]]
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2771.Poste_1)                                    
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        for g in range(len(li0)):
                                        
                                            data26=data[data["Famille"]==c[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2771.Poste_1)
                                        for p in range(len(fin)):

                                            if fin[p]in data2772["Poste_2"].to_list():
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():

                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():

                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                    k=k+1


            elif q=="Du 14H00 à 22H00":
                x=0
                for i in range(len(b)):
                    data1=data[data["Famille"]==b[i]]

                    data11=data1[data1.Poste_1!='-']
                    data12=data1[data1.Poste_2!='-']
                    data13=data1[data1.Poste_3!='-']
        
                    data14=data12.Poste_2.to_list()
                    
                    x=x+len(data14)
                y=0
                for i in range(len(c)):
                    data10=data[data["Famille"]==c[i]]

                    data110=data10[data10.Poste_1!='-']
                    data120=data10[data10.Poste_2!='-']
                    data130=data10[data10.Poste_3!='-']
        
                    data140=data120.Poste_2.to_list()
                    y=y+len(data140)
                    
                    

                

                st.subheader("Famille"+" "+"["+" "+str(x+y)+" "+"]")

                col1,col2=st.columns(2)
                
                
                
                with col1:
                    k=0
                    for i in range(len(b)):
                        k=k+1
                        data1=data[data["Famille"]==b[i]]

                        #data11=data1[data1.Affec!='']
                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data102.Poste_2
                        

                        with st.expander(b[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            k=k+1
                            st.write('')
                            


                            for t in range(len(data1489)):
                                k=k+1
                            
                            
                                if data1489[t]!=[]:
                                    k=k+1

                                    

                                
                                    data26=data[data["Famille"]==b[i]]
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2772.Poste_2)
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        k=k+1
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        for g in range(len(li0)):
                                            k=k+1
                                            #st.write(li0[g])
                                        
                                            data26=data[data["Famille"]==b[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2772.Poste_2)
                                        for p in range(len(fin)):
                                            k=k+1

                                            if fin[p]in data2772["Poste_2"].to_list():
                                                k=k+1
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():
                                                k=k+1

                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():
                                                k=k+1

                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    k=k+1
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")

                                    k=k+1


                                        

                                        

 

                with col2:

                    
                    #k=0
                    for i in range(len(c)):
                        data1=data[data["Famille"]==c[i]]

                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data102.Poste_2
                        

                        with st.expander(c[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            st.write('')
                            


                            for t in range(len(data1489)):
                            
                            
                                if data1489[t]!=[]:

                                    

                        
                                    data26=data[data["Famille"]==c[i]]
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2772.Poste_2)                                    
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        for g in range(len(li0)):
                                        
                                            data26=data[data["Famille"]==c[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2772.Poste_2)
                                        for p in range(len(fin)):

                                            if fin[p]in data2772["Poste_2"].to_list():
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():

                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():

                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                    k=k+1

            elif q=="Du 22H00 à 06H00":
                x=0
                for i in range(len(b)):
                    data1=data[data["Famille"]==b[i]]

                    data11=data1[data1.Poste_1!='-']
                    data12=data1[data1.Poste_2!='-']
                    data13=data1[data1.Poste_3!='-']
        
                    data14=data13.Poste_3.to_list()
                    
                    x=x+len(data14)
                y=0
                for i in range(len(c)):
                    data10=data[data["Famille"]==c[i]]

                    data110=data10[data10.Poste_1!='-']
                    data120=data10[data10.Poste_2!='-']
                    data130=data10[data10.Poste_3!='-']
        
                    data140=data130.Poste_3.to_list()
                    y=y+len(data140)
                    
                    

                

                st.subheader("Famille"+" "+"["+" "+str(x+y)+" "+"]")

                col1,col2=st.columns(2)
                
                
                
                with col1:
                    k=0
                    for i in range(len(b)):
                        k=k+1
                        data1=data[data["Famille"]==b[i]]

                        #data11=data1[data1.Affec!='']
                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data103.Poste_3
                        

                        with st.expander(b[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            k=k+1
                            st.write('')
                            


                            for t in range(len(data1489)):
                                k=k+1
                            
                            
                                if data1489[t]!=[]:
                                    k=k+1

                                    

                                
                                    data26=data[data["Famille"]==b[i]]
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2773.Poste_3)
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        k=k+1
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        for g in range(len(li0)):
                                            #st.write(li0[g])
                                        
                                            data26=data[data["Famille"]==b[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2773.Poste_3)
                                        for p in range(len(fin)):

                                            if fin[p]in data2772["Poste_2"].to_list():
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():

                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():

                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            
                                    k=k+1


                                        

                                        

 

                with col2:

                    
                    #k=0
                    for i in range(len(c)):
                        data1=data[data["Famille"]==c[i]]

                        data11=data1[data1.Affec!='']


                        
                        
                        data1489=list(data11["Affec"].unique())
                        data101=data1[data1.Poste_1!='-']
                        data102=data1[data1.Poste_2!='-']
                        data103=data1[data1.Poste_3!='-']
                        data176=data103.Poste_3
                        

                        with st.expander(c[i]+" "+"("+" "+str(len(data1489))+" AFFECT"+" )"+" / "+"( "+str(len(data176))+" EMP"+" )"):
                            st.write('')
                            


                            for t in range(len(data1489)):
                            
                            
                                if data1489[t]!=[]:

                                    

                        
                                    data26=data[data["Famille"]==c[i]]
                                    data277=data26[data26["Affec"]==data1489[t]]
                                    data2771=data277[data277.Poste_1!='-']
                                    data2772=data277[data277.Poste_2!='-']
                                    data2773=data277[data277.Poste_3!='-']
                                    fin=list(data2773.Poste_3)                                    
                                    if st.button(data1489[t]+" ( "+str(len(fin))+" EMP )",key=k):
                                        li0=list(data["Famille"].iloc[1:,].unique())
                                        for g in range(len(li0)):
                                        
                                            data26=data[data["Famille"]==c[i]]
                                            data277=data26[data26["Affec"]==data1489[t]]
                                            data2771=data277[data277.Poste_1!='-']
                                            data2772=data277[data277.Poste_2!='-']
                                            data2773=data277[data277.Poste_3!='-']
                                            fin=list(data2773.Poste_3)
                                        for p in range(len(fin)):

                                            if fin[p]in data2772["Poste_2"].to_list():
                                                #st.write("ok")
                                                st.write(fin[p]+" ( 14h-22h ) ")
                                            elif fin[p] in data2771["Poste_1"].to_list():

                                                data509=data2771[data2771["Poste_1"]==fin[p]]
                                                ww=data509["hd1"].to_list()
                                                zz=data509["hf1"].to_list()

                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"06h"+" - "+"14h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                            elif fin[p] in data2773["Poste_3"].to_list():

                                                data509=data2773[data2773["Poste_3"]==fin[p]]
                                                ww=data509["hd2"].to_list()
                                                zz=data509["hf2"].to_list()
                                                if ww[0]=='-' and zz[0]=='-':
                                                    st.write(fin[p]+" ( "+"22h"+" - "+"06h"+" ) ")
                                                else:
                                                    st.write(fin[p]+" ( "+str(ww[0])+"h"+" - "+str(zz[0])+"h"+" ) ")
                                    k=k+1
        

            elif q=="Plus d'horaires":
                q0=st.sidebar.radio("Horaires:",
                (ff),key=i)
                lh1t=[]
                for hhh in lh1:
                    if hhh not in lh1t:
                        lh1t.append(hhh)
                # st.write(6)
                lih0=lh1t
                # st.write(lih0)
                lh2t=[]
                for hhh0 in lh2:
                    if hhh0 not in lh2t:
                        lh2t.append(hhh0)
                # st.write(7)
                lih=lh2t
                # st.write(lih)
            
                for i in lh1t:
                    for j in lh2t:
                        if q0=="Du "+i+"H à "+j+"H":
                            data_a=data[data["hd1"]==i]
                            data_aa=data_a[data_a["hf1"]==j]
                            data_b=data[data["hd2"]==i]
                            data_bb=data_b[data_b["hf2"]==j]
                            
                            data_t=data_aa.Poste_1.append(data_bb.Poste_3)
                            
                            st.subheader("Famille"+" [ "+str(len(data_t))+" ] ")

                            
                            data1162=data[data["hd2"]==i]
                            data1163=data1162[data1162["hf2"]==j]
                            data11620=data[data["hd1"]==i]
                            data11630=data11620[data11620["hf1"]==j]
                            li0=list(data11630["Famille"].unique())
                            # st.write(li0)
                            a=len(li0)//2
                            b=li0[a:]
                            c=li0[:a]


                            li00=list(data1163["Famille"].unique())
                            # st.write(li00)
                            a0=len(li00)//2
                            b0=li00[a0:]
                            c0=li00[:a0]

                            if i in data["hd1"].to_list() and j in data["hf1"].to_list() :
                                col1,col2=st.columns(2)
                                tt=0
                                for q in range(len(b)):
                                    tt=tt+1
                                    with col1:
                                        data447=data[data["Famille"]==str(b[q])]
                                        data14890=list(data447["Affec"].unique())
                                            
                                        for t in range(len(data14890)):
                                            tt=tt+1
                                            
                                            data154=data447[data447["Affec"]==data14890[t]]
                                            data2288=data154[data154["Poste_1"]!="-"]
                                            data2289=data154[data154["Poste_3"]!="-"]
                                            data_ac1=data2288[data2288["hd1"]==i]
                                            data_ac2=data2289[data2289["hf1"]==j]
                                            data2288=data447[data447["Poste_1"]!="-"]
                                            data1302=data2288[data2288["hd1"]==i]
                                            data1303=data1302[data1302["hf1"]==j]

                                            data13302=data1303.Poste_1

                                        with st.expander(str(b[q])+" ( "+str(len(data14890))+" Affec )"+" / "+" ( "+str(len(data13302))+" EMP ) "):
                                            tt=tt+1
                                            data447=data[data["Famille"]==str(b[q])]
                                            data14890=list(data447["Affec"].unique())
                                            # st.write(data14890)
                                            
                                            for t in range(len(data14890)):
                                                tt=tt+1
                                                # st.write(data14890)
                                                
                                                data154=data447[data447["Affec"]==data14890[t]]
                                                data2288=data154[data154["Poste_1"]!="-"]
                                                data2289=data154[data154["Poste_3"]!="-"]
                                                data_ac1=data2288[data2288["hd1"]==i]
                                                data_ac2=data_ac1[data_ac1["hf1"]==j]
                                                data_to=data_ac1.append(data_ac2)


                                                if st.button(data14890[t]+" ( "+str(len(data_ac2))+" EMP )",key=tt):
                                                    tt=tt+1


                                                    data154=data447[data447["Affec"]==data14890[t]]
                                                    data1302=data154[data154["hd1"]==i]
                                                    data1303=data1302[data1302["hf1"]==j]
                                                    # llp=list(data1303["Poste_1"])
                                                    lk=list(data1303["Poste_1"])
                                                    for k in range(len(data1303)):
                                                        st.write(lk[k])
                                                    # st.write(len(lk))

                                                tt=tt+1
                                            tt=tt+1
                                        tt=tt+1
                                    tt=tt+1
  
                            
                                # tt=tt+1
                                for q in range(len(c)):
                                    with col2:
                                        data447=data[data["Famille"]==str(c[q])]
                                        data14890=list(data447["Affec"].unique())
                                        data2288=data447[data447["Poste_1"]!="-"]
                                        data1302=data2288[data2288["hd1"]==i]
                                        data1303=data1302[data1302["hf1"]==j]
                                        data13302=data1303.Poste_1
                                        with st.expander(str(c[q])+" ( "+str(len(data14890))+" Affec )"+" / "+" ( "+str(len(data13302))+" EMP ) "):
                                            data447=data[data["Famille"]==str(c[q])]
                                            data14890=list(data447["Affec"].unique())
                                            for t in range(len(data14890)):
                                                # st.write(data14890)
                                                data154=data447[data447["Affec"]==data14890[t]]
                                                data2288=data154[data154["Poste_1"]!="-"]
                                                data2289=data154[data154["Poste_3"]!="-"]
                                                data_ac1=data2288[data2288["hd1"]==i]
                                                data_ac2=data_ac1[data_ac1["hf1"]==j]

                                                if st.button(data14890[t]+" ( "+str(len(data_ac2))+" EMP )",key=tt):

                                                    data154=data447[data447["Affec"]==data14890[t]]
                                                    data1302=data154[data154["hd1"]==i]
                                                    data1303=data1302[data1302["hf1"]==j]
                                                    # llp=list(data1303["Poste_1"])
                                                    lk=list(data1303["Poste_1"])
                                                    for k in range(len(data1303)):
                                                        st.write(lk[k])
                                                tt=tt+1
                                
                            elif i in data["hd2"].to_list() and j in data["hf2"].to_list():
                                col1,col2=st.columns(2)
                                tt0=0
                                for q in range(len(b0)):
                                    tt0=tt0+1
                                    with col1:
                                        tt0=tt0+1
                                        data447=data[data["Famille"]==str(b0[q])]
                                        data14890=list(data447["Affec"].unique())
                                        data2288=data447[data447["Poste_3"]!="-"]
                                        data1302=data2288[data2288["hd2"]==i]
                                        data1303=data1302[data1302["hf2"]==j]
                                        data13302=data1303.Poste_3
                                        with st.expander(str(b0[q])+" ( "+str(len(data14890))+" Affec )"+" / "+" ( "+str(len(data13302))+" EMP ) "):
                                            tt0=tt0+1

                                            for t in range(len(data14890)):
                                                tt0=tt0+1
                                                data154=data447[data447["Affec"]==data14890[t]]
                                                data2288=data154[data154["Poste_1"]!="-"]
                                                data2289=data154[data154["Poste_3"]!="-"]
                                                data_ac1=data2289[data2289["hd2"]==i]
                                                data_ac2=data_ac1[data_ac1["hf2"]==j]
                                                # st.write(data_ac2)
                                                if st.button(data14890[t]+" ( "+str(len(data_ac2))+" EMP )",key=tt0):
                                                    tt0=tt0+1

                                                    data154=data447[data447["Affec"]==data14890[t]]
                                                    data1302=data154[data154["hd2"]==i]
                                                    data1303=data1302[data1302["hf2"]==j]
                                                    tt0=tt0+1
                                                    # llp=list(data1303["Poste_1"])
                                                    lk=list(data1303["Poste_3"])
                                                    for k in range(len(data1303)):
                                                        tt0=tt0+1
                                                        st.write(lk[k])
                                                tt0=tt0+1
                                            tt0=tt0+1
                                        tt0=tt0+1
                                for q in range(len(c0)):
                                    with col2:
                                        data447=data[data["Famille"]==str(c0[q])]
                                        data14890=list(data447["Affec"].unique())
                                        data2288=data447[data447["Poste_1"]!="-"]
                                        data1302=data2288[data2288["hd2"]==i]
                                        data1303=data1302[data1302["hf2"]==j]
                                        data13302=data1303.Poste_3
                                        with st.expander(str(c0[q])+" ( "+str(len(data14890))+" Affec )"+" / "+" ( "+str(len(data13302))+" EMP ) "):
                                            tt0=tt0+1

                                            for t in range(len(data14890)):
                                                tt0=tt0+1
                                                data154=data447[data447["Affec"]==data14890[t]]
                                                data2288=data154[data154["Poste_1"]!="-"]
                                                data2289=data154[data154["Poste_3"]!="-"]
                                                data_ac1=data2289[data2289["hd2"]==i]
                                                data_ac2=data_ac1[data_ac1["hf2"]==j]

                                                if st.button(data14890[t]+" ( "+str(len(data_ac2))+" EMP )",key=tt0):
                                                    tt0=tt0+1

                                                    data154=data447[data447["Affec"]==data14890[t]]
                                                    data1302=data154[data154["hd2"]==i]
                                                    data1303=data1302[data1302["hf2"]==j]
                                                    # llp=list(data1303["Poste_1"])
                                                    lk=list(data1303["Poste_3"])
                                                    for k in range(len(data1303)):
                                                        st.write(lk[k])
                                                tt0=tt0+1
                                            tt0=tt0+1
                                        tt0=tt0+1






















                # i=0
                # j=0
                # for j in range(len(l)-2):
                #     col1,col2,col3=st.columns(3)
                #     if j!=len(l):
    
                #         with col1:
                #             with st.expander(l[i]):
                #                 st.write("hi")
                #     else:
                #         break
                #     i=i+1
                #     if j!=len(l):
                #         with col2:
                #             with st.expander(l[i]):
                #                 st.write("hi")
                #     else:
                #         break
                #     i=i+1
                #     if j!=len(l):

                #         with col3:
                #             with st.expander(l[i]):
                #                 st.write("hi")
                    
                #     i=i+1
    

















    # else:     ---1446---
    #     st.title("GPC-DATA VISUALISE")
    #     st.write("Cette plateforme est dédié pour GPCCARTON qui permet de visualiser les données de types (.xlsx) de gestion des employés et leurs abscences sous format graphique sous ce quand l'appele Dashboard , ainsi quelle permet d'effectuer des recherches personnalisées et des filtrages avancés ")

  



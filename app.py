import gradio as gr
import pandas as pd
import sqlite3

def inser_data_to_sqlite(nome,cognome,eta):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("INSERT INTO my_table(nome,cognome,eta)VALUES(?,?,?)",(nome, cognome, eta))
    conn.commit()
    conn.close()

def visualize_data():
    conn = sqlite3.connect("test.db")
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()    
    return df

insert_interface = gr.Interface(fn=inser_data_to_sqlite, 
                                inputs=["text", "text", "number"], 
                                outputs=None,
                                title="SQLite Data Insertion Interface",
                                description="Enter data to insert into SQLite database",
                                #examples=[["Papà", "DiGim", "25"]],
                                allow_flagging='never',
                                )
#insert_interface.launch()

visualize_interface  = gr.Interface(fn=visualize_data,
                                    inputs=None, 
                                    outputs=gr.Dataframe(visualize_data()), 
                                    allow_flagging='never',
                                    )
#visualize_interface.launch()

app = gr.TabbedInterface(interface_list=[insert_interface, visualize_interface], 
                         tab_names = ["Insert", "Read"]
                         )

app.launch()
if __name__ == "__main__":
    app.launch()
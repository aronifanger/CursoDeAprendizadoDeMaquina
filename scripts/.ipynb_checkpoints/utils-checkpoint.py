from IPython.core.display import display, HTML

def html(code):
    return display(HTML(code))

def introduction():
    html("""
        <img id="top" src="imagens/semantix.png">
        <center><h1>EDUTECH</h1></center>
        <center><h2>Curso de Aprendizado de Máquina </h2></center>
    """)

introduction()
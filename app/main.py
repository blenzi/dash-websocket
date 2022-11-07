from dash_extensions.enrich import DashProxy, html, dcc, Input, Output
from dash_extensions import WebSocket

# Create example app.
app = DashProxy(prevent_initial_callbacks=True)
app.title = "Dash-websocket"
server = app.server  # Gunicorn will be looking for the server attribute of this module
app.layout = html.Div([
    html.H1("Dash application with websocket"),
    html.H3("Connected to websocket, waiting for message"),
    # dcc.Input(id="input", autoComplete="off"),
    html.Div(id="message"),
    # WebSocket(url="ws://127.0.0.1:5000/ws", id="ws")
    # WebSocket(url='wss://demo.piesocket.com/v3/channel_123?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self', id="ws")
    # WebSocket(url='wss://user-blenzi-486459-user.user.lab.sspcloud.fr/sample', id="ws")
    WebSocket(url='wss://user-blenzi-486459-user.user.lab.sspcloud.fr/ws', id="ws")
])


# @app.callback(Output("ws", "send"), [Input("input", "value")])
# def send(value):
#     return value

@app.callback(Output("message", "children"), [Input("ws", "message")])
def message(e):
    return f"Message from websocket: {e['data']}"

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)

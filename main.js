let img = document.getElementById('video');

ws = new WebSocket('ws://localhost:8081')
ws.onmessage = (event) => {
    img.setAttribute(
      'src', `data:image/png;base64,${event.data}`
    );
};
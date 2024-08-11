document.addEventListener('DOMContentLoaded', () => {
    fetchMessages();

    document.getElementById('messageForm').addEventListener('submit', event => {
        event.preventDefault();
        const content = document.getElementById('messageContent').value;
        fetch('/messages', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content }),
        })
        .then(response => response.json())
        .then(message => {
            addMessage(message);
            document.getElementById('messageContent').value = '';
        });
    });
});

function fetchMessages() {
    fetch('/messages')
        .then(response => response.json())
        .then(messages => {
            messages.forEach(addMessage);
        });
}

function addMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${message.content} [${message.spam ? 'SPAM' : 'NOT SPAM'}]`;
    document.getElementById('messages').appendChild(messageElement);
}
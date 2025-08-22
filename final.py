from flask import Flask, request, render_template, redirect, url_for, send_from_directory, session
from flask_socketio import SocketIO, emit, join_room, leave_room
import os
import base64

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Set a secret key for session handling
socketio = SocketIO(app)  # Enable WebSocket communication

# Store uploaded files and user sessions
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create upload directory if it doesn't exist
users = {}  # Dictionary to store users with their session IDs

# Clear uploaded files on server restart
for file in os.listdir(UPLOAD_FOLDER):
    file_path = os.path.join(UPLOAD_FOLDER, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

@app.route("/", methods=["GET", "POST"])
def message_board():
    # Check if the username is in the session; if not, ask for it
    if "username" not in session:
        if request.method == "POST" and "username" in request.form:
            session["username"] = request.form.get("username")  # Set the username in the session
            return redirect(url_for("message_board"))  # Redirect to the main message board
        else:
            # Display the name input form if username is not set
            return render_template("username.html")

    # Main message board display
    
    return render_template("home.html", username=session["username"])

# SocketIO events for message and file handling
@socketio.on('register')
def register_user(username):
    """ Register the user with their session ID when they connect """
    users[username] = request.sid
    print(f"User {username} connected with session ID {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    """ Remove user from users dictionary when they disconnect """
    for username, sid in users.items():
        if sid == request.sid:
            del users[username]
            print(f"User {username} disconnected")
            break

@socketio.on('group_message')
def handle_group_message(data):
    sender = session["username"]
    emit('group_message', {'sender': sender, 'message': data['message']}, broadcast=True)

@socketio.on('private_message')
def handle_private_message(data):
    sender = session["username"]
    recipient = data['recipient']
    
    # Emit the message to the recipient (private chat)
    if recipient in users:
        emit('private_message', {'sender': sender, 'message': data['message']}, room=users[recipient])

    # Emit the message back to the sender (private chat)
    emit('private_message', {'sender': sender, 'message': data['message']}, room=request.sid)


@socketio.on('upload_group_file')
def handle_group_file_upload(data):
    file_name = data['fileName']
    file_data = base64.b64decode(data['fileData'])  # Decode the base64 string to binary data
    file_path = os.path.join(UPLOAD_FOLDER, file_name)

    # Save the file to the uploads directory
    with open(file_path, "wb") as f:
        f.write(file_data)

    # Generate the file URL
    file_url = url_for('uploaded_file', filename=file_name)
    sender = session["username"]

    # Notify all clients (broadcast) about the uploaded file
    emit("group_file_uploaded", {'fileName': file_name, 'fileUrl': file_url, 'sender': sender}, broadcast=True)

@socketio.on('upload_private_file')
def handle_private_file_upload(data):
    recipient = data['recipient']
    file_name = data['fileName']
    file_data = base64.b64decode(data['fileData'])  # Decode the base64 string to binary data
    file_path = os.path.join(UPLOAD_FOLDER, file_name)

    # Save the file to the uploads directory
    with open(file_path, "wb") as f:
        f.write(file_data)

    # Generate the file URL
    file_url = url_for('uploaded_file', filename=file_name)
    sender = session["username"]

    # Emit the file message to the recipient
    if recipient in users:
        recipient_sid = users[recipient]
        emit("private_file_uploaded", {'fileName': file_name, 'fileUrl': file_url, 'sender': sender}, room=recipient_sid)

    # Emit the file message back to the sender as well
    emit("private_file_uploaded", {'fileName': file_name, 'fileUrl': file_url, 'sender': sender}, room=request.sid)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    socketio.run(app, debug=True)

# Real-Time Chat Application 💬 

A modern, real-time chat application built with Flask and Socket.IO that supports both group and private messaging with file sharing capabilities.

## ✨ Features

- **Real-time Messaging**: Instant messaging using WebSocket connections
- **Group Chat**: Public chat room where all users can participate
- **Private Messaging**: One-on-one private conversations between users
- **File Sharing**: Upload and share files in both group and private chats
- **User Sessions**: Persistent user sessions with username management
- **Responsive Design**: Modern, mobile-friendly user interface
- **File Management**: Automatic file cleanup on server restart

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Real-time Communication**: Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Base64 encoding/decoding
- **Session Management**: Flask sessions

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SyedAneesAshraf/Real-Time-Chat-Application.git
   cd Real-Time-Chat-Application
   ```

2. **Install required dependencies**
   ```bash
   pip install flask flask-socketio
   ```

3. **Run the application**
   ```bash
   python final.py
   ```

4. **Access the application**
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## 🎯 How to Use

### Getting Started
1. When you first visit the application, you'll be prompted to enter your username
2. After setting your username, you'll be redirected to the main chat interface

### Group Chat
- Type your message in the input field at the bottom
- Click "Send" or press Enter to send the message to all users
- All messages appear in the main chat area

### Private Chat
- Select a user from the online users list (if implemented)
- Send private messages that only the selected user can see
- Private messages are distinguished from group messages

### File Sharing
- Click the file upload button to select a file
- Files can be shared in both group and private chats
- Uploaded files are temporarily stored and can be downloaded by recipients

## 📁 Project Structure

```
Real-Time-Chat-Application/
├── final.py                 # Main Flask application
├── templates/
│   ├── home.html           # Main chat interface
│   └── username.html       # Username input page
├── uploads/                # Temporary file storage
└── README.md              # Project documentation
```

## 🔧 Configuration

### Environment Variables
You can customize the following settings in `final.py`:

- **SECRET_KEY**: Change the secret key for production use
- **UPLOAD_FOLDER**: Modify the file upload directory
- **DEBUG**: Set to `False` for production deployment

### Security Considerations
- The current secret key is for development only
- Implement proper authentication for production use
- Add file type validation for uploads
- Set file size limits for uploads

## 🌐 API Endpoints

### HTTP Routes
- `GET/POST /` - Main application route with username handling
- `GET /uploads/<filename>` - File download endpoint

### Socket.IO Events
- `register` - Register user with session ID
- `disconnect` - Handle user disconnection
- `group_message` - Send message to all users
- `private_message` - Send private message to specific user
- `upload_group_file` - Upload file to group chat
- `upload_private_file` - Upload file to private chat

## 🔄 How It Works

1. **User Registration**: Users set their username which is stored in Flask sessions
2. **WebSocket Connection**: Socket.IO establishes real-time connection between client and server
3. **Message Broadcasting**: Group messages are broadcast to all connected users
4. **Private Messaging**: Direct messages are sent only to specific users using session IDs
5. **File Handling**: Files are encoded in Base64, uploaded to server, and shared via URLs

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Authors

- **Syed Anees Ashraf** - *Initial work* - [SyedAneesAshraf](https://github.com/SyedAneesAshraf)

## 📞 Support

If you have any questions or run into issues, please feel free to:
- Open an issue on GitHub
- Contact the development team

## 🙏 Acknowledgments

- Flask and Socket.IO communities for excellent documentation
- Contributors who help improve this project
- Users who provide feedback and suggestions

---

**Happy Chatting! 🎉**

Check it out at: https://real-time-web-chatting-application-5.onrender.com

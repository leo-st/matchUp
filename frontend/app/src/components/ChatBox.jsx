import './ChatBox.css';
import MessageList from './messages/MessageList';
import { IoIosCloseCircleOutline } from "react-icons/io";
function ChatBox({onShowOverlay, friend}){
  console.log("ChatBox received friendChat:", friend); // Debug
    const messages = [
      { sender: "Alice", content: "Hello, how are you?1", timestamp: "2024-01-17T10:00:00Z" },
        { sender: "Bob", content: "I'm good, thanks! How about you?1", timestamp: "2025-11-17T10:01:00Z" },
        { sender: "Alice", content: "I'm doing great!1", timestamp: "2025-11-17T10:02:00Z" },
        { sender: "Alice", content: "Hello, how are you?2", timestamp: "2025-01-17T10:00:00Z" },
        { sender: "Bob", content: "I'm good, thanks! How about you?2", timestamp: "2025-01-17T10:01:00Z" },
        { sender: "Alice", content: "I'm doing great!2", timestamp: "2025-01-17T10:02:00Z" },
      ];
    return <>
        <div className="floating-overlay">
        <div className="chat-container">
      {/* Top Row Bar */}
      <div className="chat-top-bar">
        <div>
          <strong>{friend}</strong> - <span>Status</span>
        </div>
        <button onClick={onShowOverlay}>
        <IoIosCloseCircleOutline/>
        </button>
      </div>

      {/* Message Content */}
      <MessageList messages={messages}/>

      {/* Free Text Space */}
      <div className="chat-textarea-container">
        <textarea placeholder="Type your message here..."></textarea>
      </div>

      {/* Bottom Row Bar */}
      <div className="chat-bottom-bar">
        <button>Send</button>
      </div>
    </div>
          
        <button onClick={onShowOverlay}>Close</button>
        </div>
    </>
}

export default ChatBox;
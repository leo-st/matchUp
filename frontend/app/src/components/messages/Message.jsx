import './Message.css'

function Message({ name, creationTimestamp, content }) {
    return (
      <div className="message-container">
        <div className="message-top-bar">
          <strong className="message-name">{name}</strong>
          <span className="message-timestamp">
            {new Date(creationTimestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </span>
        </div>
        <div className="message-content">{content}</div>
      </div>
    );
  }

export default Message;
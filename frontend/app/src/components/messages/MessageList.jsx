import "./MessageList.css";
import Message from "./Message";

function MessageList({ messages }) {
  // Helper function to format a date
  const formatDate = (timestamp) => {
    const options = { year: "numeric", month: "short", day: "numeric" };
    return new Date(timestamp).toLocaleDateString(undefined, options);
  };

  return (
    <div className="chat-messages">
      {messages.map((message, index) => {
        const currentMessageDate = formatDate(message.timestamp);
        const previousMessageDate =
          index > 0 ? formatDate(messages[index - 1].timestamp) : null;

        return (
          <div key={index}>
            {/* Show the date separator if the date changes */}
            {currentMessageDate !== previousMessageDate && (
              <div className="date-separator">
                <div className="separator-line"></div>
                <span className="separator-date">{currentMessageDate}</span>
                <div className="separator-line"></div>
              </div>
            )}

            {/* Render the message */}
            <div className="chat-message">
              <Message
                name={message.sender}
                creationTimestamp={message.timestamp}
                content={message.content}
              />
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default MessageList;

import React, { useState, useEffect } from "react";
import "./Feed.css";
import SportCard from "../SportCard";
import ChatBox from "../ChatBox";
import FeedList from "./FeedList";
function Feed({ friendChat }) {
  console.log("feed rendered");
  console.log(friendChat);
  const [showOverlay, setShowOverlay] = useState(friendChat ? true : false);

  function hideChatBox() {
    setShowOverlay(false);
  }

  useEffect(() => {
    setShowOverlay(friendChat ? true : false);
  }, [friendChat]); // Run whenever `friendChat` changes

  const sports = [
    { description: "Football", url: "/images/football.png" },
    { description: "Basketball", url: "/images/basketball.png" },
    { description: "Badminton", url: "/images/badminton.png" },
    { description: "Padel", url: "/images/padel.png" },
    { description: "Table Tenis", url: "/images/table_tenis.png" },
    { description: "Tenis", url: "/images/tenis.png" },
    { description: "Voleyball", url: "/images/voleyball.png" },
  ];

  return (
    <div className="feed">
      <h1>Sports</h1>
      <div>
        <div className="list-categories-container">
          <button className="categories-button">Open all categories</button>
        </div>
        <div className="sport-card-container">
          <ul>
            {sports.map((sport) => (
              <li>
                <SportCard image={sport.url} description={sport.description} />
              </li>
            ))}
          </ul>
        </div>
      </div>
      <FeedList />

      {showOverlay && (
        <ChatBox onShowOverlay={hideChatBox} friend={friendChat} />
      )}

      {!showOverlay && (
        <button className="reopen-button" onClick={() => setShowOverlay(true)}>
          Open Chatbox
        </button>
      )}
    </div>
  );
}

export default Feed;

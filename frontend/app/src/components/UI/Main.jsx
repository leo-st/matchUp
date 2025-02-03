import "./Main.css";
import { GiHamburgerMenu } from "react-icons/gi";
import Sidebar from "./Sidebar";
import { useState } from "react";
import Feed from "../feed/Feed";
import Chat from "./Chat";

function Main() {
  const [sidebarShow, setSidebarShow] = useState(false);
  const [friendChat, setFriendChat] = useState(undefined); //for now we work with strings, later will be id's
  
  function handleSelectedFriend(name){
    setFriendChat(name);
  }

  return (
    <div className="main">
      <div className={`sidebar ${sidebarShow ? "open" : ""}`}>
        {sidebarShow && <Sidebar />}
      </div>
      <div className={`content`}>
        <div className="top-row" onClick={() => setSidebarShow(!sidebarShow)}>
          <GiHamburgerMenu />
        </div>
        <div className="feed-wrapper">
          <Feed friendChat={friendChat}/>
        </div>
      </div>
      <div className="chat">
        <Chat selectedFriendInChat={handleSelectedFriend}/>
      </div>
    </div>
  );
}

export default Main;

import './Chat.css';
import SearchBox from './SearchBox';
import FriendList from '../friends/FriendList';
import { useState } from 'react';

const friends = [
    { name: 'Alice', status: 'online' },
    { name: 'Bob', status: 5 },
    { name: 'Charlie', status: 'online' },
  ];

  function Chat({ selectedFriendInChat }) {
    const [friendsList, setFriendList] = useState(friends);

    function handleSelectedFriend(name) {
        selectedFriendInChat(name); // Pass the name up
    }

    return (
        <div className="chat-container">
            <div className="search-box-wrapper">
                <SearchBox onSearch={(text) => {
                    setFriendList(friends.filter(
                        friend => friend.name.toLowerCase().includes(text.toLowerCase())
                    ));
                }} />
            </div>
            <h2>Friends</h2>
            <FriendList friends={friendsList} selectFriend={handleSelectedFriend} />
        </div>
    );
}

export default Chat;
import './FriendList.css';
import Friend from './Friend';

function FriendList({ friends, selectFriend }) {
    return (
      <div className="friend-list">
        {friends.map((friend, index) => (
          <Friend 
            key={index} 
            name={friend.name} 
            status={friend.status} 
            onClick={() => selectFriend(friend.name)} 
          />
        ))}
      </div>
    );
}
export default FriendList;
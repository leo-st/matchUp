import { PiCursorClickFill } from "react-icons/pi";
import { FaEye } from "react-icons/fa";
import "./FeedPost.css";

function FeedPost({ image, image_description,user_image, place, time, username, clicks, views, description }) {
    return (
      <div className="feed-post-main">
        <img className="feed-post-image" src={image} alt={image_description} />
        <div className="feed-post-text">
          <div className="feed-post-info">
            <div className="user-info">
              <img className="user-icon" src={user_image} alt="User icon" />
              <label className="username">{username}</label>
            </div>
            <div className="post-stats">
              <PiCursorClickFill className="icon" />
              <label>{clicks}</label>
              <FaEye className="icon" />
              <label>{views}</label>
            </div>
          </div>
          <div className="feed-post-description">
            <p>{description}</p>
            <div className="post-details">
              <label className="place"><strong>Place:</strong> {place}</label>
              <label className="time"><strong>Time:</strong> {time}</label>
            </div>
          </div>
        </div>
      </div>
    );
  }
  
export default FeedPost;

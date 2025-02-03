import FeedPost from "./FeedPost";
import './FeedList.css'
function FeedList() {
    return (
      <div className="feed-list">
        <div className="feed-list-header">
          <text className="recent-posts">Recent posts</text>
          <div className="feed-list-buttons">
            <button className="feed-button">Latest</button>
            <button className="feed-button">Popular</button>
          </div>
        </div>
        <FeedPost
          image="/images/futsal_stadium.jpg"
          image_description="test"
          user_image="/images/user_pic.jpg"
          place="Krempijevo"
          time="21:00"
          username="Leo Ivas"
          clicks={5}
          views={15}
          description="Za osrednju ekipu tražimo bilo koga samo da popuni misto!"
        />
      </div>
    );
  }

export default FeedList;

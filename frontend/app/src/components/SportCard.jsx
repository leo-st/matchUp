import './SportCard.css';

function SportCard({ image, description }) {
    return (
        <div className="card">
            <img src={image} alt={description} />
            <p>{description}</p>
        </div>
    );
}

export default SportCard;
import React from 'react';
import './SearchBox.css';

const SearchBox = ({ placeholder = "Search", onSearch }) => {
  return (
    <div className="search-box-container">
      <input
        type="text"
        className="search-box-input"
        placeholder={placeholder}
        onChange={(e) => onSearch && onSearch(e.target.value)}
      />
      <svg
        className="search-box-icon"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M21 21l-4.35-4.35m-2.65 0A7.5 7.5 0 1117.5 7.5a7.5 7.5 0 010 15z"
        />
      </svg>
    </div>
  );
};

export default SearchBox;
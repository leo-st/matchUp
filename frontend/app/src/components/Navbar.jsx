import './Navbar.css'
import { IoIosNotifications } from "react-icons/io";
import { BsChatDots } from "react-icons/bs";
import { FaUser } from "react-icons/fa";
//import { GiHamburgerMenu } from "react-icons/gi";

function Navbar() {
  return <nav className="navbar">
    <div className="navbar-left">
        <a href="/" className='logo'>matchUp</a>
    </div>
    <div className="navbar-right">
        <ul className="nav-links">
            <li>
                <a href="/account"><IoIosNotifications /></a>
                <a href="/account"><BsChatDots /></a>
                <a href="/account" className="user-icon"> 
                <FaUser />
                </a>
            </li>
        </ul>
    </div>
  </nav>;
}

export default Navbar;

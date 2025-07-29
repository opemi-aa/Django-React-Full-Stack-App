import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ACCESS_TOKEN } from '../constants';
import '../styles/Navbar.css'; // We'll create this CSS file next

function Navbar() {
    const navigate = useNavigate();
    const isLoggedIn = localStorage.getItem(ACCESS_TOKEN);

    const handleLogout = () => {
        localStorage.clear();
        navigate('/login');
    };

    return (
        <nav className="navbar-container">
            <div className="navbar-brand">
                <Link to="/">Note App</Link>
            </div>
            <div className="navbar-links">
                {!isLoggedIn ? (
                    <>
                        <Link to="/login">Login</Link>
                        <Link to="/register">Register</Link>
                    </>
                ) : (
                    <button onClick={handleLogout} className="navbar-logout-button">
                        Logout
                    </button>
                )}
            </div>
        </nav>
    );
}

export default Navbar;

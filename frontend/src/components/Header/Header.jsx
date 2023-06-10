import React from 'react';
import { Link } from 'react-router-dom';

import './Header.scss';

const Header = () => {
  return (
    <header className="header">
        <Link to='/' className="site-logo">SiPiX</Link>
        <div className="navlinks">
            <Link to='cart' className="navlink">Cart</Link>
            <Link to='login' className="navlink">Login</Link>
        </div>
    </header>
  )
}

export default Header

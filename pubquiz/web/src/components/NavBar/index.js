import React from 'react';
import {Link} from 'react-router-dom';
import './style.scss';

const NavBar = () => {
  return (
    <div className='nav-container' id='navbar'>
      <div className='empty'></div>
      <div className='nav-brand font-bold'>
        <Link to='/'>PubQuiz</Link>
      </div>
      <div className='nav-menu'>
        <span className='nav-item'>Register Team</span>
        <span className='nav-item'>Admin</span>
      </div>
    </div>
  );
};

export default NavBar;

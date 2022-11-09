import React from 'react';
import NavBar from '../components/NavBar';
import './StandardLayout.scss';

const StandardLayout = ({children}) => {
  return (
    <div>
      <NavBar />
      <main>{children}</main>
    </div>
  );
};

export default StandardLayout;

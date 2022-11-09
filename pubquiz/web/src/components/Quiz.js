import React from 'react';

const Quiz = (props) => {
  const {quiz_name, starts_at, ends_at, teams_registered} = props;

  return <div>{quiz_name}</div>;
};

export default Quiz;

import React from 'react';
import './styles.scss';

const Quiz = (props) => {
  let {quiz_name, starts_at, ends_at, teams_registered} = props;
  starts_at = new Date(starts_at);
  ends_at = new Date(ends_at);
  return (
    <div className='quiz-container'>
      <p className='quiz-title font-bold'>{quiz_name}</p>
      <div className='quiz-info'>
        <InfoCard title={'Teams Registered'} value={teams_registered} />
        <InfoCard
          title={'Starts At'}
          value={starts_at.toLocaleDateString()}
          value_extra={starts_at.toLocaleTimeString()}
        />
        <InfoCard
          title={'Ends At'}
          value={ends_at.toLocaleDateString()}
          value_extra={ends_at.toLocaleTimeString()}
        />
      </div>
    </div>
  );
};

const InfoCard = (props) => {
  const {title, value, value_extra} = props;

  return (
    <div className='info-card'>
      <div className='info-title'>{title}</div>
      <div className='info-value'>{value}</div>
      {value_extra && <div className='info-value'>{value_extra}</div>}
    </div>
  );
};

export default Quiz;

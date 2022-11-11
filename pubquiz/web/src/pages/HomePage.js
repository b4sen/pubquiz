import axios from 'axios';
import React, {useEffect, useState} from 'react';
import {NavLink} from 'react-router-dom';
import Quiz from '../components/Quiz';
import './HomePage.scss';

const HomePage = () => {
  const [upcomingQuizes, setUpcomingQuizes] = useState([]);
  const [pastQuizes, setPastQuizes] = useState([]);

  const now = Date.now;

  useEffect(() => {
    axios
      .get('/api/quiz/')
      .then((res) => res.data)
      .then((response) => {
        let _upcomingQuizes = [];
        let _pastQuizes = [];
        if (response) {
          response.forEach((quiz) => {
            let end_date = new Date(quiz.ends_at);
            if (end_date > now) {
              _upcomingQuizes.push(quiz);
            } else {
              _pastQuizes.push(quiz);
            }
          });
          setUpcomingQuizes(_upcomingQuizes);
          setPastQuizes(_pastQuizes);
        }
      });
  }, [now]);

  return (
    <div className='quiz-list'>
      <p className=''>Upcoming Quizes</p>
      {upcomingQuizes &&
        upcomingQuizes.map((quiz) => {
          return (
            <NavLink to={`/quiz/${quiz.id}`}>
              <Quiz
                quiz_name={quiz.quiz_name}
                key={quiz.id}
                starts_at={quiz.starts_at}
                ends_at={quiz.ends_at}
                teams_registered={quiz.teams_registered}
              />
            </NavLink>
          );
        })}

      <p className=''>Past Quizes</p>
      {pastQuizes &&
        pastQuizes.map((quiz) => {
          return (
            <NavLink to={`/quiz/${quiz.id}`}>
              <Quiz
                quiz_name={quiz.quiz_name}
                key={quiz.id}
                starts_at={quiz.starts_at}
                ends_at={quiz.ends_at}
                teams_registered={quiz.teams_registered}
              />
            </NavLink>
          );
        })}
    </div>
  );
};

export default HomePage;

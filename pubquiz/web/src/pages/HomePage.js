import axios from 'axios';
import React, {useEffect, useState} from 'react';
import Quiz from '../components/Quiz';

const HomePage = () => {
  const [quizes, setQuizes] = useState([]);

  useEffect(() => {
    axios
      .get('/api/quiz/')
      .then((res) => res.data)
      .then((response) => {
        setQuizes(response);
      });
  }, []);

  return (
    <div>
      <ul>
        {quizes &&
          quizes.map((quiz) => {
            return (
              <li>
                <Quiz quiz_name={quiz.quiz_name} key={quiz.id} />
              </li>
            );
          })}
      </ul>
    </div>
  );
};

export default HomePage;

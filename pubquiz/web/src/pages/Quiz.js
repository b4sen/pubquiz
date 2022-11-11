import axios from 'axios';
import React, {useEffect, useState} from 'react';
import {useParams} from 'react-router-dom';

const Quiz = () => {
  const params = useParams();
  let id = params.id;
  const [quiz, setQuiz] = useState({});
  const [isEnded, setIsEnded] = useState(false);
  const [startsAtTime, setStartsAtTime] = useState(null);
  const [startsAtDate, setStartsAtDate] = useState(null);
  const [endsAtTime, setEndsAtTime] = useState(null);
  const [endsAtDate, setEndsAtDate] = useState(null);

  useEffect(() => {
    axios
      .get(`/api/quiz/${id}`)
      .then((res) => {
        return res.data;
      })
      .then((data) => {
        if (data) {
          let ends_at = new Date(data['ends_at']);
          let starts_at = new Date(data['starts_at']);

          setStartsAtTime(starts_at.toLocaleTimeString());
          setStartsAtDate(starts_at.toLocaleDateString());
          setEndsAtTime(ends_at.toLocaleTimeString());
          setEndsAtDate(ends_at.toLocaleDateString());

          if (ends_at > Date.now) {
            setIsEnded(false);
          } else {
            setIsEnded(true);
          }
          setQuiz(data);
        }
      });
  }, []);

  if (isEnded) {
    return (
      <div className=''>
        <p>{quiz.quiz_name}</p>
        <p>
          Ended at: {endsAtTime} - {endsAtDate}
        </p>
        <p>{JSON.stringify(quiz.teams_registered)}</p>
        <p>{JSON.stringify(quiz.questions)}</p>
      </div>
    );
  }
  return <div>{JSON.stringify(quiz)}</div>;
};

export default Quiz;

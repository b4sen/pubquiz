import {BrowserRouter, Routes, Route, Outlet} from 'react-router-dom';
import StandardLayout from './layouts/StandardLayout';
import HomePage from './pages/HomePage';
import Quiz from './pages/Quiz';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          element={
            <StandardLayout>
              <Outlet />
            </StandardLayout>
          }
        >
          <Route index element={<HomePage />} />
          <Route path='/quiz/:id' element={<Quiz />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

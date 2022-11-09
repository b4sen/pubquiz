import {BrowserRouter, Routes, Route, Outlet} from 'react-router-dom';
import StandardLayout from './layouts/StandardLayout';
import HomePage from './pages/HomePage';

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
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

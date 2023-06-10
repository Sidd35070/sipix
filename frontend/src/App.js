import './App.scss';

import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './pages/Home/Home';
import Layout from './pages/Layout/Layout';
import Cart from './pages/Cart/Cart';
import Login from './pages/Login/Login';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout />} >
          <Route index element={<Home />} />
          <Route path='cart' element={<Cart />} />
          <Route path='login' element={<Login />} />

        </Route>
      </Routes>
    </BrowserRouter>

  );
}

export default App;

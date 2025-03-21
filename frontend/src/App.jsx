import './App.css'
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import { AnimatePresence } from 'framer-motion';
import AboutUs from './pages/AboutUs';
import NotFound from './pages/404';
import { useEffect } from 'react';
import axios from 'axios';
import { useState } from 'react';
import Login from './components/Login';
//To do
//componente home




/* Conexión DJANGO */
function Home() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/users/api/')
    .then((response)=> {
      setData(response.data);
      setLoading(false);
    })
    .catch((error) => {
      setError("Error al conectar al back: "+error);
      setLoading(false);
    });
  }, []);
  if (loading) return <p>Cargando...</p>
  if (error) return <p>{error}</p>
  return (
    <div>
      <h1>Datos de usuarios desde Django</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{item.username} - {item.email}</li>
        ))}
      </ul>
    </div>
  )
};

const AnimatedRoutes = () => {
  const location = useLocation();

  return (
    <AnimatePresence mode = 'wait'>
      <Routes location={location} key={location.pathname}>
        <Route path='/login' element={<Login />}/>
        <Route path='/about' element={<AboutUs />}/>
        <Route path='/' element={<Home />}/>
        <Route path='*' element={<NotFound />}/>
      </Routes>
    </AnimatePresence>
  )
};

function App() {

  return (
    <>
    <Router>
      <Navbar />
      <div className='container mt-4'>
        <div className="row">
          <div className="col">
            <AnimatedRoutes />
          </div>
        </div>
      </div>
    </Router>
    </>
  )
}

export default App

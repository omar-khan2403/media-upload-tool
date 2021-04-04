//mport logo from './logo.svg';
import './App.css';
import Header from './components/Header' ;
import UploadTool from './components/UploadComponents/UploadTool';
import Map from './components/MapComponents/Map';
import MapList from './components/MapList';
import About from './components/About';
import User from './components/User';

import {
  BrowserRouter as Router, 
  Switch,
  Route
} from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <Header />
      <Router>
        <Switch>
          <Route path='/' component={MapList} />
          <Route path='/map/:id' component={Map} />
          <Route path='/about' component={About} />
          <Route path='/user/:id' component={User} />
        </Switch>
      </Router>
      <UploadTool/>
    </div>
  );
}

export default App;

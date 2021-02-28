//mport logo from './logo.svg';
import './App.css';
import Header from './components/Header' ;
import {
  BrowserRouter as Router, 
  Switch,
  Route
} from 'react-router-dom';
import Map from './components/MapComponents/Map';
import MapList from './components/MapList';
import Upload from './components/Upload';

function App() {
  return (
    <div className="App">
      <Header />
      <Router>
        <Switch>
          <Route path='/' component={MapList} />
          <Route path='/map/:id' component={Map} />
          <Route path='/upload' component={Upload} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;

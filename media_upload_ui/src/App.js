//mport logo from './logo.svg';
import './App.css';
import Header from './components/Header' ;
import {
  BrowserRouter as Router, 
  Switch,
  Route
} from 'react-router-dom';
import Map from './components/Map'

function App() {
  return (
    <div className="App">
      <Header />
      <Router>
        <Switch>
          <Route path='/map/:id' component={Map}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;

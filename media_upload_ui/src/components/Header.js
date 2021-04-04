import React from 'react';

import { Link, BrowserRouter as Router } from 'react-router-dom';
import Typography from '@material-ui/core/Typography';  
import { withStyles } from '@material-ui/core/styles';
import Toolbar from '@material-ui/core/Toolbar';
import ExploreIcon from '@material-ui/icons/Explore';
import IconButton from '@material-ui/core/IconButton';
import AppBar from '@material-ui/core/AppBar';
import Box from '@material-ui/core/Box';
import Fab from '@material-ui/core/Fab';
import Grow from '@material-ui/core/Grow';

import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';

import GoogleLogin from 'react-google-login'; 

import API from '../api/axios';

//import Button from '@material-ui/core/Button';

const useStyles = theme => ({
    root: {
      flexGrow: 1
    },
    menuButton: {
      marginRight: theme.spacing(2),
    },
    title: {
      flexGrow: 1,
      marginRight: theme.spacing(2)
    },
  });

class Header extends React.Component {
  // define state of isLoggedIn that will be conditionally changed
  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: localStorage.getItem('is_auth'),
      u_name: localStorage.getItem('u_name'),
      u_email: localStorage.getItem('u_email'),
      u_id: localStorage.getItem('u_id'),
      anchorEl: false, 
    };

    this.handleClick = this.handleClick.bind(this);
    this.handleClose = this.handleClose.bind(this);
    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);    

  }


  handleClick = (event) => {
      this.setState({ anchorEl: event.currentTarget});
  };

  handleClose() {
    this.setState({ anchorEl: null});
  };

  async handleLogin(googleData) {
    const res = await API.post("/api/auth/google", {
        body: JSON.stringify({
        token: googleData.tokenId,
        user: googleData.profileObj
      }),
      headers: {
        "Content-Type": "application/json"
      }
    })
    const response = await res;

    if (response.status === 400) {
      console.log('error')
    }

    else {
      const data = res.data
      // store returned user somehow
      localStorage.setItem('u_id', data.u_id);
      localStorage.setItem('is_auth', data.is_auth);
      localStorage.setItem('u_name', data.u_name); 
      localStorage.setItem('u_email', data.u_email); 
      this.setState({ isLoggedIn: 'true', u_name: data.u_name, u_email: data.email, u_id: data.u_id })

      window.location.reload()

    }
  }

  handleLogout() {
    localStorage.removeItem('u_id');
    localStorage.removeItem('is_auth');
    localStorage.removeItem('u_name');
    localStorage.removeItem('u_email'); 
    this.setState({ isLoggedIn: 'false', u_name: null, u_email: null, u_id: null  })

    window.location.reload()
  }

  renderLoggedIn() {
    if (this.state.isLoggedIn === null || this.state.isLoggedIn === 'false') {
      return (
        <Box 
        position="absolute"
        alignContent="right"
        left="80%"
        >
          <GoogleLogin
          clientId="1090840640392-a6gsdncuceimq1s1e8blurhuvh5d4ole.apps.googleusercontent.com"
          buttonText="Log in with Google"
          onSuccess={this.handleLogin}
          onFailure={this.handleLogin}
          cookiePolicy={'single_host_origin'}
        />
        </Box>
      )
    }
    else {

      return (
        <Box 
        position="absolute"
        alignContent="right"
        left="90%"
        >
          <Fab 
          size="small"
          color="primary" 
          aria-label="add" 
          aria-controls="simple-menu" 
          aria-haspopup="true" 
          onClick={this.handleClick}
          >
            {this.state.u_name[0]}
          </Fab>
          <Menu
          id="simple-menu"
          anchorEl={this.state.anchorEl}
          open={Boolean(this.state.anchorEl)}
          onClose={this.handleClose}
          TransitionComponent={Grow}
          //anchorOrigin={{ vertical: "top", horizontal: "center" }}
          //transformOrigin={{ vertical: "bottom", horizontal: "center" }}
          >
            <MenuItem>{this.state.u_email}</MenuItem>
            <Router>
            <Link to="/user/" style={{ textDecoration: 'none', color: 'black' }}>
              <MenuItem>My maps</MenuItem>
            </Link>   
            </Router>
            
            <MenuItem onClick={this.handleLogout}>Logout</MenuItem>
          </Menu>
        </Box>
      )
    }
  }

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <script src="https://apis.google.com/js/platform.js" async defer></script>
        <meta name="google-signin-client_id" content="1090840640392-a6gsdncuceimq1s1e8blurhuvh5d4ole.apps.googleusercontent.com.apps.googleusercontent.com"></meta>
        <AppBar position="static" color="transparent">
          <Toolbar>
            <Router>
              <Link to="/" style={{ textDecoration: 'none', color: 'black' }}> 
                <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
                  <ExploreIcon />
                </IconButton>
              </Link>
              <Link to="/" style={{ textDecoration: 'none', color: 'black' }}>
                <Typography variant="h6" className={classes.title}>
                    Maps
                  </Typography>
              </Link>              
              <Link to="/about" style={{ textDecoration: 'none', color: 'black' }}>
                <Typography variant="h6" className={classes.title}>
                  About
                </Typography>
              </Link>
            </Router>
            {this.renderLoggedIn()}
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

export default withStyles(useStyles)(Header);
  
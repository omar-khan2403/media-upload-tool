import React from 'react';
import { Link, BrowserRouter as Router } from 'react-router-dom';
import Typography from '@material-ui/core/Typography';  
import { makeStyles } from '@material-ui/core/styles';
import Toolbar from '@material-ui/core/Toolbar';
import ExploreIcon from '@material-ui/icons/Explore';
import IconButton from '@material-ui/core/IconButton';
import AppBar from '@material-ui/core/AppBar';
//import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
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
  }));

export default function Header() {
    const classes = useStyles();
  
    return (
      <div className={classes.root}>
        <AppBar position="static" color="white">
          <Toolbar>
            <Router>
              <Link to="/" style={{ textDecoration: 'none', color: 'black' }}> 
                <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
                  <ExploreIcon />
                </IconButton>
              </Link>
              <Link to="/" style={{ textDecoration: 'none', color: 'black' }}>
                <Typography variant="h8" className={classes.title}>
                    Maps
                  </Typography>
              </Link>              
              <Link to="/upload" style={{ textDecoration: 'none', color: 'black' }}>
                <Typography variant="h8" className={classes.title}>
                  Upload
                </Typography>
              </Link>
            </Router>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
  
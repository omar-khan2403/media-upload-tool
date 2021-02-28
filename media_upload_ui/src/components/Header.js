import React from 'react';
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
    },
  }));

export default function Header() {
    const classes = useStyles();
  
    return (
      <div className={classes.root}>
        <AppBar position="static" color="white">
          <Toolbar>
            <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
              <ExploreIcon />
            </IconButton>
            Map Upload Tool
          </Toolbar>
        </AppBar>
      </div>
    );
  }
  
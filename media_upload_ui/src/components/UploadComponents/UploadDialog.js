import React from 'react';
import API from '../../api/axios';

import Button from '@material-ui/core/Button';
import MenuItem from '@material-ui/core/MenuItem';
import Divider from '@material-ui/core/Divider';
import TextField from '@material-ui/core/TextField';
import CircularProgress from '@material-ui/core/CircularProgress';

import DialogTitle from '@material-ui/core/DialogTitle';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText'
import DialogActions from '@material-ui/core/DialogActions';

import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

import MapOutlinedIcon from '@material-ui/icons/MapOutlined';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';

const styles = (theme) => ({
  root: {
    margin: 0,
    padding: theme.spacing(2),
  },
});


export default function UploadDialog() {
    
    const [open, setOpen] = React.useState(false);
    const [uploadFile, setUploadFile] = React.useState(null);
    const [uploadName, setUploadName] = React.useState(null);
    const [progress, setProgress] = React.useState();

    const handleClickOpen = () => {
      setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    const handleFile = (event) => {
      console.log(event.target.files[0]);
      setUploadFile(event.target.files[0]);
    }

    const handleName = (event) => {
      setUploadName(event.target.value)
    }
    
    const handleUpload = async () => {
      const data = new FormData();
      data.append('file', uploadFile);
      data.append('name', uploadName);
      data.append('user_id', localStorage.u_id);
      
      const res = await API.post("/api/map", data, {
        headers: {
        "Content-Type": "multipart/form-data",
      },
      onUploadProgress: data => {
        console.log(Math.round((100 * data.loaded) / data.total ));
        setProgress(Math.round((100 * data.loaded) / data.total ));
      },
    });

      const response = await res;

      console.log(response);
  
      if (response.status === 400) {
        console.log('error')
      }
  
      else {
        //window.location.reload()
      }
    }

    return (
        <div>
          <MenuItem onClick={handleClickOpen}>
            <ListItemIcon>
                <CloudUploadIcon fontSize="small" />
            </ListItemIcon>
            <ListItemText primary="Upload Map (CSV)" />
            </MenuItem>
            <Divider />
            <MenuItem onClick={handleClickOpen}>
            <ListItemIcon>
                <CloudUploadIcon fontSize="small" />
            </ListItemIcon>
            <ListItemText primary="Upload Map (Excel)" />
          </MenuItem>

        <Dialog 
        onClose={handleClose} 
        aria-labelledby="customized-dialog-title" 
        open={open}
        fullWidth={true}
        >
        <DialogTitle id="customized-dialog-title" onClose={handleClose}>
          Upload Map <MapOutlinedIcon fontSize="small" />
        </DialogTitle>
        <form noValidate autoComplete="off">
          <DialogContent dividers>
            <DialogContentText>
              <TextField id="standard-basic" label="Map Name" onChange={handleName} />
            </DialogContentText>
            <DialogContentText style={{'padding-top': '1rem'}}>
              <input type="file" onChange={handleFile} />
            </DialogContentText>
            {progress && <CircularProgress value={progress} />}
          </DialogContent>
        </form>
        <DialogActions>
          <Button autoFocus onClick={handleUpload} color="primary">
            Upload Map File
          </Button>
        </DialogActions>
      </Dialog>
    </div>
    )
}
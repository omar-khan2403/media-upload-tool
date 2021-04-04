import React from 'react';
import UploadDialog from './UploadDialog';

import Box from '@material-ui/core/Box';
import Fab from '@material-ui/core/Fab';
import Grow from '@material-ui/core/Grow';
import AddIcon from '@material-ui/icons/Add'
import Menu from '@material-ui/core/Menu';


export default function UploadTool() {
    const [anchorEl, setAnchorEl] = React.useState(null);

    const handleClick = (event) => {
        console.log(event.currentTarget);
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    return (
        <div>
            <Box 
            position="absolute"
            alignContent="right"
            bottom={40}
            left="90%"
            >
                <Fab 
                size="large"
                color="primary" 
                aria-label="add" 
                aria-controls="simple-menu" 
                aria-haspopup="true" 
                onClick={handleClick}
                >
                    <AddIcon />
                </Fab>
                <Menu
                id="simple-menu"
                anchorEl={anchorEl}
                TransitionComponent={Grow}
                getContentAnchorEl={null}
                anchorOrigin={{ vertical: "top", horizontal: "center" }}
                transformOrigin={{ vertical: "bottom", horizontal: "center" }}
                open={Boolean(anchorEl)}
                onClose={handleClose}
                >
                    <UploadDialog />
                </Menu>
            </Box>
        </div>
    )
}